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
	Plug 'windwp/nvim-autopairs'
	Plug 'nvim-tree/nvim-tree.lua'
	Plug 'nvim-tree/nvim-web-devicons' " Para íconos
	Plug 'goolord/alpha-nvim'
	Plug 'nvim-lua/plenary.nvim'            " Dependencia necesaria para Telescope
	Plug 'nvim-telescope/telescope.nvim', {'tag': '0.1.2'}
	Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
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

" =============================
" Configuración nvim-autopairs
" =============================
lua << EOF
require("nvim-autopairs").setup {}
EOF

" =============================
" Configuración Nvim-tree
" =============================
lua << EOF
require("nvim-tree").setup()
EOF
nnoremap <F2> :NvimTreeToggle<CR>

" =============================
" Configuración inicio neovim
" =============================
lua << EOF
local alpha = require("alpha")
local dashboard = require("alpha.themes.dashboard")

dashboard.section.header.val = {
  [[                                  __]],
  [[     ___     ___    ___   __  __ /\_\    ___ ___]],
  [[    / _ `\  / __`\ / __`\/\ \/\ \\/\ \  / __` __`\]],
  [[   /\ \/\ \/\  __//\ \_\ \ \ \_/ |\ \ \/\ \/\ \/\ \]],
  [[   \ \_\ \_\ \____\ \____/\ \___/  \ \_\ \_\ \_\ \_\]],
  [[    \/_/\/_/\/____/\/___/  \/__/    \/_/\/_/\/_/\/_/]],
}

dashboard.section.buttons.val = {
  dashboard.button("e", "  Nuevo archivo", ":ene <BAR> startinsert <CR>"),
  dashboard.button("f", "󰈞  Buscar archivo", ":Telescope find_files<CR>"),
  dashboard.button("r", "  Archivos recientes", ":Telescope oldfiles<CR>"),
  dashboard.button("q", "  Salir", ":qa<CR>"),
}

dashboard.section.footer.val = "Arch Linux"

alpha.setup(dashboard.opts)
EOF

" =============================
" Configuración Telescope
" =============================
lua << EOF
require('telescope').setup{
  defaults = {
    file_ignore_patterns = {"node_modules", ".git/"},
  }
}
EOF

" Atajos para abrir Telescope fácilmente
nnoremap <leader>ff :Telescope find_files<CR>
nnoremap <leader>fg :Telescope live_grep<CR>
nnoremap <leader>fb :Telescope buffers<CR>
nnoremap <leader>fh :Telescope help_tags<CR>

" =============================
" Configuración Treesitter
" =============================
lua << EOF
require'nvim-treesitter.configs'.setup {
  ensure_installed = { "c", "lua", "python", "javascript", "html", "css" }, -- lenguajes a instalar
  highlight = {
    enable = true,              -- activar resaltado
    additional_vim_regex_highlighting = false,
  },
  indent = {
    enable = true               -- activar indentación mejorada
  }
}
EOF


