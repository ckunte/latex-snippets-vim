# LaTeX snippets for Vim

This repository provides LaTeX [UltiSnips][us] snippets for Vim. Sorry that was a mouthful. It simply means these snippets require UltiSnips plug-in pre-installed to work as intended.

## What are snippets and how do they work?

See a demo of snippets in action.

https://user-images.githubusercontent.com/177423/121562114-b7cdae00-ca4b-11eb-9865-875ecb1b190b.mp4

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

This repository contains the following snippets:

| Snippets                   | Description                           |
| -------------------------- | ------------------------------------- |
| `note` + <kbd>tab</kbd>    | Inserts a note template (for XeLaTeX) |
| `toc` + <kbd>tab</kbd>     | Inserts a TOC block                   |
| `beg` + <kbd>tab</kbd>     | Inserts a begin/end block             |
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

1. Vim version that supports python3 bindings. Check `vim --version | grep '+python3'` and it should have `+python3` or `+python3/dyn` in the listing. If you do not have `+python3` enabled, then see how to enable this below.

    1. On __Debian Linux__, `vim-nox` for example is `+python3` enabled, and it can be installed using apt like so: `sudo apt-get install vim-nox`. But before you do, it may be necessary to uninstall `vim-tiny` beforehand (that some systems are bundled-with) with the following: `sudo apt-get remove vim-tiny`.

    2. On __MacOS__, the best way to get vim with `+python3` bindings is to compile from source. Before this, it is best to download the latest [python](https://www.python.org) and install it on the Mac (v3.9.5 as of this writing). Here is how in five steps (be sure to read comments below for instructions):

    ```bash
    git clone --depth=1 https://github.com/vim/vim.git
    cd vim/src
    # Uncomment the following line in the Makefile and save it
    # CONF_OPT_PYTHON3 = --enable-python3interp=dynamic
    make
    make install
    # vim will be installed to /usr/local/bin
    ```

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
let g:UltiSnipsJumpForwardTrigger = '<C-j>'
let g:UltiSnipsJumpBackwardTrigger = '<C-k>'

```

Reload `.vimrc` and `:PlugInstall` to install plug-ins.

## Manual installation (not recommended)

Place `*.snippets` files under, say, `~/.vim/UltiSnips/` (and reload `~/.vimrc` with `source ~/.vimrc` if appropriate). This method is not recommended because then one needs to keep track of updates and will have to manually download and place these whenever snippets are updated. This method still requires that UltiSnips plug-in is installed.

[us]: https://github.com/SirVer/ultisnips
[vp]: https://github.com/junegunn/vim-plug
[ck]: https://github.com/ckunte/latex-snippets-vim
[rc]: https://github.com/ckunte/dotfiles/blob/master/.vimrc
