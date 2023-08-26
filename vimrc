set nocompatible
filetype on

set rtp+=/home/burnout/.vim/Vundle.vim/
call vundle#begin()

Plugin 'itchyny/lightline.vim'
Plugin 'vimwiki/vimwiki'
Plugin 'preservim/nerdtree'
Plugin 'vifm/vifm'

call vundle#end()
filetype plugin indent on 

autocmd VimEnter * call lightline#update()
set laststatus=2

let g:lightline = {
    \ 'colorscheme': 'selenized_black',
    \  }



let mapleader=","



set hlsearch
set incsearch
set clipboard=unnamedplus

set tabstop=4
set softtabstop=4
set shiftwidth=4


set expandtab
set autoindent
set fileformat=unix

syntax on 

set encoding=utf-8

set number relativenumber

set splitbelow splitright

