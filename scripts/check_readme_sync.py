#!/usr/bin/env python3
"""
Confirm every *newly added* snippet trigger is documented in the README's
snippet table. Pre-existing undocumented triggers (documentation debt that
predates this PR) are reported as warnings only, so contributors are never
blocked by drift they didn't introduce - only by drift they did.

Baseline comparison uses the BASE_REF environment variable (e.g.
"origin/master"), which the workflow sets to the PR's target branch. If
BASE_REF isn't set (e.g. running locally with no PR context), every
undocumented trigger is treated as blocking.
"""
import os
import re
import subprocess
import sys
from pathlib import Path

SNIPPETS_DIR = Path("UltiSnips")
README = Path("README.md")

TRIGGER_RE = re.compile(r'^snippet\s+(\S+)\s+"', re.MULTILINE)
# Matches README rows like: | `letter` + <kbd>tab</kbd> | Inserts a letter template |
# (tolerant of the `+ <kbd>tab</kbd>` / `+ \`tab\`` variants, and typos like </tab>)
README_TRIGGER_RE = re.compile(r'\|\s*`([^`]+)`\s*\+\s*(?:`tab`|<kbd>\s*tab\s*</)')


def triggers_from_text(text):
    return set(TRIGGER_RE.findall(text))


def get_current_triggers():
    triggers = {}
    for f in sorted(SNIPPETS_DIR.glob("*.snippets")):
        text = f.read_text(encoding="utf-8", errors="replace")
        for t in triggers_from_text(text):
            triggers.setdefault(t, f)
    return triggers


def get_base_triggers(base_ref):
    """Triggers that existed in UltiSnips/*.snippets at base_ref, or None
    if the baseline can't be determined."""
    if not base_ref:
        return None
    try:
        listed = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", base_ref, "--", str(SNIPPETS_DIR)],
            capture_output=True, text=True, check=True,
        ).stdout.splitlines()
    except subprocess.CalledProcessError:
        return None

    triggers = set()
    for path in listed:
        if not path.endswith(".snippets"):
            continue
        try:
            text = subprocess.run(
                ["git", "show", f"{base_ref}:{path}"],
                capture_output=True, text=True, check=True,
            ).stdout
        except subprocess.CalledProcessError:
            continue
        triggers |= triggers_from_text(text)
    return triggers


def get_documented_triggers():
    text = README.read_text(encoding="utf-8", errors="replace")
    return set(README_TRIGGER_RE.findall(text))


def main():
    if not SNIPPETS_DIR.is_dir():
        print(f"::error::Expected a '{SNIPPETS_DIR}' directory, but none was found.")
        sys.exit(1)
    if not README.is_file():
        print("::error::README.md not found.")
        sys.exit(1)

    current = get_current_triggers()
    documented = get_documented_triggers()
    base_triggers = get_base_triggers(os.environ.get("BASE_REF"))

    undocumented = sorted(set(current) - documented)

    if base_triggers is None:
        newly_undocumented = undocumented
        pre_existing = []
    else:
        newly_undocumented = [t for t in undocumented if t not in base_triggers]
        pre_existing = [t for t in undocumented if t in base_triggers]

    summary = []

    for trig in newly_undocumented:
        msg = (
            f"New trigger '{trig}' (in {current[trig]}) isn't listed in the "
            "README snippet table yet. Please add a row for it."
        )
        print(f"::error file=README.md::{msg}")
        summary.append(f"- {msg}")

    for trig in pre_existing:
        print(
            f"::warning file=README.md::Trigger '{trig}' is undocumented, but "
            "predates this PR, so it's not blocking."
        )

    stale = sorted(documented - set(current))
    for trig in stale:
        msg = (
            f"README documents trigger '{trig}' but it no longer exists in "
            "any .snippets file. Please update or remove that row."
        )
        print(f"::warning file=README.md::{msg}")
        summary.append(f"- (warning) {msg}")

    Path("readme_sync_errors.txt").write_text("\n".join(summary), encoding="utf-8")

    if newly_undocumented:
        sys.exit(1)

    print("README is in sync with newly introduced snippet triggers.")
    sys.exit(0)


if __name__ == "__main__":
    main()
