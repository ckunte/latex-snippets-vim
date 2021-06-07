# LaTeX snippets for Vim

This repository provides LaTeX [UltiSnips][us] snippets for Vim. Sorry that was a mouthful. It simply means these snippets require UltiSnips plug-in pre-installed to work as intended.

## What is are snippets and how do they work?

The concept of a snippet is simple. Think of a block of pre-formatted text (i.e., a template) that one needs to use often. One can of-course type or copy-paste such blocks of text repeatedly the hard way, or one could instead assign such common blocks of text with an abbreviated keyword, which in turn calls the entire block of text. To ensure such blocks do not accidentally appear while typing the actual content of the note, paper, or report, a trigger is required. To illustrate this, see below:

In Vim' insert mode, typing `note` and hitting <kbd>tab</kbd> key on the keyboard inserts the following block, and focuses on the first user input _Title_ in the template. Type the title, and hold <kbd>Ctrl</kbd> and press <kbd>j</kbd> (`C-j` in Vim parlance) to jump to the next placeholder _Author_ to enter. The shortcut to jumping between placeholders can be set in `~/.vimrc` file. 

```latex
%!TeX TS-program = xelatex
%!TeX encoding = utf-8 Unicode
\documentclass[11pt,a4paper]{article}

\title{Title}
\author{Author}

\begin{document}

  \maketitle

\end{document}
```

Whereas when writing this following sentence, the keyword `note` does not expand into a template block like above, since the <kbd>tab</kbd> is not used. (Caveat: Any snippet keyword that is the first word in a file or a line auto-expands without the <kbd>tab</kbd>, and is a smart feature of UltiSnips.)

> I am writing to finish this note by noon.

See a demo of snippets in action.

https://user-images.githubusercontent.com/177423/118755310-398e4980-b89b-11eb-9167-746a98af80d3.mov


This repository contains the following snippets:

| Template snippets          | Description                           |
| -------------------------- | ------------------------------------- |
| `note` + <kbd>tab</kbd>    | Inserts a note template (for XeLaTeX) |
| `toc` + <kbd>tab</kbd>     | Inserts a TOC block                   |

| Section and block snippets | Description                           |
| -------------------------- | ------------------------------------- |
| `beg` + <kbd>tab</kbd>     | Inserts a begin/end block             |
| `sec` + <kbd>tab</kbd>     | Inserts a section block               |
| `sub` + <kbd>tab</kbd>     | Inserts a subsection block            |
| `enum` + <kbd>tab</kbd>    | Inserts an enum list block            |
| `item` + <kbd>tab</kbd>    | Inserts an item list block            |
| `itm` + <kbd>tab</kbd>     | Inserts an item line                  |
| `fig` + <kbd>tab</kbd>     | Inserts a figure/label block          |
| `tabl` + <kbd>tab</kbd>    | Inserts a table block                 |
| `ref` + <kbd>tab</kbd>     | Inserts a reference block             |
| `apdx` + <kbd>tab</kbd>    | Inserts an appendix block             |

| Math snippets              | Description                           |
| -------------------------- | ------------------------------------- |
| `//` + <kbd>tab</kbd>      | Inserts a formatted fraction          |
| `sr` + <kbd>tab</kbd>      | Inserts a formatted square            |
| `cb` + <kbd>tab</kbd>      | Inserts a formatted cube              |
| `compl` + <kbd>tab</kbd>   | Inserts a complement                  |
| `_` + <kbd>tab</kbd>       | Formats and inserts a subscript       |

| Include snippet            | Description                           |
| -------------------------- | ------------------------------------- |
| `pdf` + <kbd>tab</kbd>     | Inserts an `includepdf` line          |

## How snippets work

Type a pre-defined keyword, say, `fig` and press <kbd>tab</kbd>, and it produces a full block of figure LaTeX code. See a demo below.

https://user-images.githubusercontent.com/177423/118755310-398e4980-b89b-11eb-9167-746a98af80d3.mov

Place `*.snippets` files under, say, `~/.vim/UltiSnips/` (and reload `~/.vimrc` with `source ~/.vimrc` if appropriate). 

## Requirements

To be able to use snippets, the following are required: 

1. Vim version that supports python3 bindings. Check `vim --version` and it should have `+python3` in the listing. For example, `vim-nox` is +python3 enabled, and it can be installed using apt (`sudo apt-get install vim-nox`).
3. [UltiSnips][us] 
4. [latex-snippets-vim][ck]

## Installation

1. Set up [vim-plug][vp] plug-in manager
2. Set the required UltiSnips plug-in for [latex-snippets-vim][ck] by adding the following to `.vimrc` file (see the author's version of [.vimrc][rc] for reference):

```vim
call plug#begin('~/.vim/plugged')

" UltiSnips for snippets
Plug 'sirver/ultisnips'

let g:UltiSnipsExpandTrigger = '<tab>'
let g:UltiSnipsJumpForwardTrigger = '<C-j>'
let g:UltiSnipsJumpBackwardTrigger = '<C-k>'

" LaTeX snippets for Vim using UltiSnips (downloads only tagged releases)
Plug 'ckunte/latex-snippets-vim', { 'tag': '*' }

call plug#end()
```

Reload `.vimrc` and `:PlugInstall` to install plug-ins.

[us]: https://github.com/SirVer/ultisnips
[vp]: https://github.com/junegunn/vim-plug
[ck]: https://github.com/ckunte/latex-snippets-vim
[rc]: https://github.com/ckunte/dotfiles/blob/master/.vimrc
