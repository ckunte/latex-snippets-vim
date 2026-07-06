# Contributing

Thanks for considering a contribution! A couple of quick guidelines keep the
snippets consistent and let the automated PR check pass on the first try.

## Snippet format

Each snippet lives in a `.snippets` file under `UltiSnips/` and follows this
shape:

```
snippet <trigger> "<description>" <flags>
<body, using $1, $2, ... for placeholders and $0 for the final cursor stop>
endsnippet
```

- `<trigger>` — the text typed before `<tab>` to expand the snippet.
- `"<description>"` — required, shown in completion menus. Keep it short.
- `<flags>` — optional; commonly `b` (only expands at the beginning of a
  line) or `i` (expands inside a word). See the
  [UltiSnips docs](https://github.com/SirVer/ultisnips/blob/master/doc/UltiSnips.txt)
  for the full list.

## Before opening a PR

1. **Test it.** Load the snippet in Vim/Neovim with UltiSnips installed and
   confirm it expands and compiles as expected.
2. **Avoid duplicate triggers.** Check the README table and existing
   `.snippets` files for a trigger that's already taken.
3. **Document it.** Add a row to the snippet table in `README.md` for any
   new or renamed trigger.
4. **Watch for trailing whitespace.** Most editors can strip this
   automatically on save.

## What the automated check does

Opening a PR runs a GitHub Action that:

- Validates snippet syntax (matching `endsnippet`, valid flags, no
  duplicate triggers, no trailing whitespace).
- Confirms any *new* trigger you've added is documented in the README.

If something fails, the bot leaves a comment on your PR pointing at the
exact file and line — fix those and push again; the check re-runs
automatically.
