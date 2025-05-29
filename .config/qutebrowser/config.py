import json
from pathlib import Path

# ====================
# Cargar colores de Pywal
# ====================
def load_pywal_colors():
    colors_path = Path.home() / ".cache" / "wal" / "colors.json"
    if colors_path.exists():
        with open(colors_path, 'r') as f:
            return json.load(f)
    return {}

colors = load_pywal_colors()
special = colors.get("special", {})
scheme = colors.get("colors", {})

# ====================
# Configuración base
# ====================
config.load_autoconfig(True)

# Pestañas siempre visibles y arriba
c.tabs.position = "top"
c.tabs.show = "always"

# Controles de pestañas
config.bind('<Ctrl-Tab>', 'tab-next') # pestaña siguiente
config.bind('<Ctrl-Shift-Tab>', 'tab-prev') # pestaña anterior

# Modo oscuro
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.algorithm = 'lightness-cielab'
c.colors.webpage.darkmode.policy.images = 'never'
config.set('colors.webpage.darkmode.enabled', False, 'file://*')

# Navegación
config.bind('h', 'back') # historial atras
config.bind('l', 'forward') # historial adelante
config.bind('<Ctrl-t>', 'open -t')  # nueva pestaña
config.bind('<Ctrl-w>', 'tab-close') # cerrar pestaña
config.bind('<Ctrl-q>', 'close')   # cerrar navegador
config.bind('yy', 'yank')          # copiar URL

# Scroll
config.bind('<Alt-j>', 'scroll down')
config.bind('<Alt-k>', 'scroll up')

# Página de inicio
c.url.start_pages = ["https://www.google.com"]

# Página predeterminada para pestañas nuevas
c.url.default_page = "https://www.google.com"

# Motor de búsqueda predeterminado
c.url.searchengines = {'DEFAULT': 'https://www.google.com/search?q={}'}
                       
# Activar adlocker
c.content.blocking.enabled = True
c.content.blocking.method = "both"
c.content.blocking.adblock.lists = [
    "https://github.com/ewpratten/youtube_ad_blocklist/blob/master/blocklist.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/legacy.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2020.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2021.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2022.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2023.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2024.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badware.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/privacy.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badlists.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances-cookies.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances-others.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badlists.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/quick-fixes.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/resource-abuse.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/unbreak.txt"] 
]

# Desactivar reproducción automática
c.content.autoplay = False

# ====================
# Aplicar colores (solo válidos)
# ====================
if special and scheme:
    c.colors.statusbar.normal.bg = special["background"]
    c.colors.statusbar.normal.fg = special["foreground"]

    c.colors.tabs.bar.bg = special["background"]
    c.colors.tabs.even.bg = scheme["color0"]
    c.colors.tabs.odd.bg = scheme["color1"]
    c.colors.tabs.even.fg = special["foreground"]
    c.colors.tabs.odd.fg = special["foreground"]
    c.colors.tabs.selected.even.bg = scheme["color2"]
    c.colors.tabs.selected.odd.bg = scheme["color3"]
    c.colors.tabs.selected.even.fg = special["background"]
    c.colors.tabs.selected.odd.fg = special["background"]

    c.colors.statusbar.insert.bg = scheme["color4"]
    c.colors.statusbar.insert.fg = special["background"]

    c.colors.statusbar.command.bg = special["background"]
    c.colors.statusbar.command.fg = special["foreground"]

    c.colors.statusbar.url.fg = scheme["color5"]

