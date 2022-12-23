# LaTeX snippets for Vim and Neovim

This repository provides LaTeX [UltiSnips][us] snippets for Vim. Sorry that was a mouthful. It simply means these snippets require UltiSnips plug-in pre-installed to work as intended.

## What are snippets and how do they work?

See a demo of snippets in action.

https://user-images.githubusercontent.com/177423/121562114-b7cdae00-ca4b-11eb-9865-875ecb1b190b.mp4

The concept of a snippet is simple. Think of a block of pre-formatted text (i.e., a template) that one needs to use often. One can of-course type or copy-paste such blocks of text repeatedly the hard way, or one could instead assign such common blocks of text with an abbreviated keyword, which in turn calls the entire block of text. To ensure such blocks do not accidentally appear while typing the actual content of the note, paper, or report, a trigger is required. To illustrate this, see below:

In Vim' insert mode, typing `note` and hitting <kbd>tab</kbd> key on the keyboard inserts the following block, and focuses on the first user input _Title_ in the template. Type the title, and hold <kbd>ctrl</kbd> and press <kbd>j</kbd> (`c-j` in Vim parlance) to jump to the next placeholder _Author_ to enter. The shortcut to jumping between placeholders can be set in `~/.vimrc` file. 

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

This repository contains the following snippets:

| Snippets                   | Description                           |
| -------------------------- | ------------------------------------- |
| `letter` + <kbd>tab</tab>  | Inserts a letter template             |
| `note` + <kbd>tab</kbd>    | Inserts a note template (for XeLaTeX) |
| `toc` + <kbd>tab</kbd>     | Inserts a TOC block                   |
| `beg` + <kbd>tab</kbd>     | Inserts a begin/end block             |
| `sum` + <kbd>tab</kbd>     | Inserts a summary section block       |
| `sec` + <kbd>tab</kbd>     | Inserts a section block               |
| `sub` + <kbd>tab</kbd>     | Inserts a subsection block            |
| `subs` + <kbd>tab</kbd>    | Inserts a subsubsection block         |
| `enum` + <kbd>tab</kbd>    | Inserts an enumerate list block       |
| `item` + <kbd>tab</kbd>    | Inserts an itemize list block         |
| `itm` + <kbd>tab</kbd>     | Inserts an item line                  |
| `desc` + <kbd>tab</kbd>    | Inserts a description list block      |
| `par` + <kbd>tab</kbd>     | Inserts a paragraph block             |
| `fig` + <kbd>tab</kbd>     | Inserts a figure/label block          |
| `tabl` + <kbd>tab</kbd>    | Inserts a table block                 |
| `ref` + <kbd>tab</kbd>     | Inserts a reference block             |
| `bit` + <kbd>tab</kbd>     | Inserts a bibitem block               |
| `apdx` + <kbd>tab</kbd>    | Inserts an appendix block             |
| `pdf` + <kbd>tab</kbd>     | Inserts an `includepdf` line          |
| `//` + <kbd>tab</kbd>      | Inserts a formatted fraction          |
| `sr` + <kbd>tab</kbd>      | Inserts a formatted square            |
| `cb` + <kbd>tab</kbd>      | Inserts a formatted cube              |
| `compl` + <kbd>tab</kbd>   | Inserts a complement                  |
| `_` + <kbd>tab</kbd>       | Formats and inserts a subscript       |

## Requirements

To be able to use snippets, the following are required:

1. Vim or Neovim with python3 support.
2. [UltiSnips][us] 
3. [latex-snippets-vim][ck]

## Installation

1. Set up [vim-plug][vp] plug-in manager
2. Set the required UltiSnips plug-in for [latex-snippets-vim][ck] by adding the following to `.vimrc` file (see the author's version of [.vimrc][rc] for reference):

```vim
call plug#begin('~/.vim/plugged')

" UltiSnips for snippets
Plug 'sirver/ultisnips'

" LaTeX snippets for Vim using UltiSnips (downloads only tagged releases)
Plug 'ckunte/latex-snippets-vim', { 'tag': '*' }

call plug#end()

let g:UltiSnipsExpandTrigger = '<tab>'
let g:UltiSnipsJumpForwardTrigger = '<c-j>'
let g:UltiSnipsJumpBackwardTrigger = '<c-k>'
```

Reload `.vimrc` and `:PlugInstall` to install plug-ins.

## Manual installation (not recommended)

Place `*.snippets` files under, say, `~/.vim/UltiSnips/` (and reload `~/.vimrc` with `source ~/.vimrc` if appropriate). This method is not recommended because then one needs to keep track of updates and will have to manually download and place these whenever snippets are updated. This method still requires that UltiSnips plug-in is installed.

[us]: https://github.com/SirVer/ultisnips
[vp]: https://github.com/junegunn/vim-plug
[ck]: https://github.com/ckunte/latex-snippets-vim
[rc]: https://github.com/ckunte/dotfiles/blob/master/.vimrc
