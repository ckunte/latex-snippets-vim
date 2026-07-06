#!/usr/bin/env python3
"""
Validate UltiSnips (.snippets) files for latex-snippets-vim.

Checks performed on every file under UltiSnips/*.snippets:
  1. Every `snippet` block has a matching `endsnippet`.
  2. The snippet header line matches:
         snippet <trigger> "<description>" [flags]
  3. Flags (if present) only use recognised UltiSnips flag letters
     (b, i, w, r, e, A, m).
  4. No duplicate triggers, either within one file or across files.
  5. No trailing whitespace on any line.

Prints GitHub Actions-style `::error file=...,line=...::message`
annotations (so issues show up inline on the PR diff), and writes a
plain-text summary to validation_errors.txt for posting as a PR
comment. Exits non-zero if any errors were found.
"""
import re
import sys
from pathlib import Path

SNIPPETS_DIR = Path("UltiSnips")
HEADER_RE = re.compile(r'^snippet\s+(\S+)\s+"([^"]*)"\s*([A-Za-z]*)\s*$')
VALID_FLAGS = set("biwreAm")


def check_file(path):
    """Return (errors, triggers) for a single .snippets file.

    errors: list of (line_no, message)
    triggers: dict trigger -> first line_no it was defined on
    """
    errors = []
    triggers_seen = {}
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()

    in_snippet = False
    header_line_no = None
    header_trigger = None

    for i, raw_line in enumerate(lines, start=1):
        line = raw_line.rstrip("\n")

        if line != line.rstrip():
            errors.append((i, "Trailing whitespace at end of line."))

        if line.startswith("snippet "):
            if in_snippet:
                errors.append((
                    header_line_no,
                    f"'snippet {header_trigger}' is missing an 'endsnippet' "
                    f"before the next snippet starts at line {i}.",
                ))

            m = HEADER_RE.match(line)
            if not m:
                errors.append((
                    i,
                    f"Malformed snippet header: {line!r}. Expected format: "
                    'snippet <trigger> "<description>" [flags]',
                ))
                in_snippet = True
                header_line_no = i
                header_trigger = "?"
                continue

            trigger, desc, flags = m.groups()
            in_snippet = True
            header_line_no = i
            header_trigger = trigger

            if not desc.strip():
                errors.append((i, f"Snippet '{trigger}' has an empty description."))

            bad_flags = set(flags) - VALID_FLAGS
            if bad_flags:
                errors.append((
                    i,
                    f"Snippet '{trigger}' uses unrecognised flag(s): "
                    f"{''.join(sorted(bad_flags))}.",
                ))

            if trigger in triggers_seen:
                errors.append((
                    i,
                    f"Duplicate trigger '{trigger}' (also defined at line "
                    f"{triggers_seen[trigger]} in this file).",
                ))
            else:
                triggers_seen[trigger] = i

        elif line == "endsnippet" or line.startswith("endsnippet"):
            if not in_snippet:
                errors.append((i, "'endsnippet' found with no matching 'snippet'."))
            in_snippet = False

    if in_snippet:
        errors.append((
            header_line_no,
            f"'snippet {header_trigger}' is never closed with 'endsnippet'.",
        ))

    return errors, triggers_seen


def main():
    if not SNIPPETS_DIR.is_dir():
        print(f"::error::Expected a '{SNIPPETS_DIR}' directory, but none was found.")
        sys.exit(1)

    files = sorted(SNIPPETS_DIR.glob("*.snippets"))
    if not files:
        print(f"::error::No .snippets files found in '{SNIPPETS_DIR}'.")
        sys.exit(1)

    all_errors = []  # list of (file, line_no, message)
    all_triggers = {}  # trigger -> (file, line_no)

    for f in files:
        errors, triggers = check_file(f)
        for line_no, msg in errors:
            all_errors.append((f, line_no, msg))
        for trig, line_no in triggers.items():
            if trig in all_triggers:
                other_file, other_line = all_triggers[trig]
                all_errors.append((
                    f, line_no,
                    f"Trigger '{trig}' already defined in {other_file} at "
                    f"line {other_line}.",
                ))
            else:
                all_triggers[trig] = (f, line_no)

    summary_lines = []
    for f, line_no, msg in sorted(all_errors, key=lambda e: (str(e[0]), e[1])):
        print(f"::error file={f},line={line_no}::{msg}")
        summary_lines.append(f"- `{f}:{line_no}` — {msg}")

    Path("validation_errors.txt").write_text("\n".join(summary_lines), encoding="utf-8")

    if all_errors:
        print(f"\n{len(all_errors)} issue(s) found.")
        sys.exit(1)

    print("All snippet files look good.")
    sys.exit(0)


if __name__ == "__main__":
    main()
