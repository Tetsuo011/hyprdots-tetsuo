" =============================
" Configuración básica de Neovim
" =============================
set number
set relativenumber
set mouse=a
set showcmd
set showmatch
set encoding=utf-8
syntax enable

" =============================
" Plugins con vim-plug
" =============================
call plug#begin()
	Plug 'RedsXDD/neopywal.nvim'
	Plug 'nvim-lualine/lualine.nvim'
	Plug 'nvim-tree/nvim-web-devicons'
call plug#end()

" =============================
" Configuración de LuaLine
" =============================
lua << END
require('lualine').setup {
	options = {
		icons_enable = true
	}
}
END

" =============================
" Configuración de pywal
" =============================
colorscheme neopywal


