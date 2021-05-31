# User-defined LaTeX snippets for Vim

This repository contains the following custom snippets:

| Template snippets          | Description                     |
| -------------------------- | ------------------------------- |
| `note` + <kbd>tab</kbd>    | Inserts a note template         |
| `toc` + <kbd>tab</kbd>     | Inserts a TOC block             |

| Section and block snippets | Description                     |
| -------------------------- | ------------------------------- |
| `beg` + <kbd>tab</kbd>     | Inserts a begin/end block       |
| `sec` + <kbd>tab</kbd>     | Inserts a section block         |
| `sub` + <kbd>tab</kbd>     | Inserts a subsection block      |
| `enum` + <kbd>tab</kbd>    | Inserts an enum list block      |
| `item` + <kbd>tab</kbd>    | Inserts an item list block      |
| `fig` + <kbd>tab</kbd>     | Inserts a figure/label block    |
| `tabl` + <kbd>tab</kbd>    | Inserts a table block           |
| `ref` + <kbd>tab</kbd>     | Inserts a reference block       |
| `apdx` + <kbd>tab</kbd>    | Inserts an appendix block       |

| Math snippets              | Description                     |
| -------------------------- | ------------------------------- |
| `//` + <kbd>tab</kbd>      | Inserts a formatted fraction    |
| `sr` + <kbd>tab</kbd>      | Inserts a formatted square      |
| `cb` + <kbd>tab</kbd>      | Inserts a formatted cube        |
| `compl` + <kbd>tab</kbd>   | Inserts a complement            |
| `_` + <kbd>tab</kbd>       | Formats and inserts a subscript |

| Include snippet            | Description                     |
| -------------------------- | ------------------------------- |
| `pdf` + <kbd>tab</kbd>     | Inserts an `includepdf` line    |

## How snippets work

Type a pre-defined keyword, say, `fig` and press <kbd>tab</kbd>, and it produces a full block of figure LaTeX code. See a demo below.

https://user-images.githubusercontent.com/177423/118755310-398e4980-b89b-11eb-9167-746a98af80d3.mov

Place `*.snippets` files under, say, `~/.vim/UltiSnips/` (and reload `~/.vimrc` with `source ~/.vimrc` if appropriate). 

## Requirements

To be able to use these, the following is assumed: 

- Vim version is `vim-nox` that supports python3 bindings (check `vim --version` and it should have `+python3` in the listing)
- [UltiSnips][us] is installed and working (I use [vim-plug][vp] to manage plug-ins) as below in `.vimrc` file:

```vim
call plug#begin('~/.vim/plugged')

" UltiSnips for snippets
Plug 'sirver/ultisnips'

call plug#end()

let g:UltiSnipsExpandTrigger = '<tab>'
let g:UltiSnipsJumpForwardTrigger = '<c-j>'
let g:UltiSnipsJumpBackwardTrigger = '<c-k>'

```

[us]: https://github.com/SirVer/ultisnips
[vp]: https://github.com/junegunn/vim-plug
