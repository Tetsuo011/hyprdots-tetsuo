
██╗  ██╗██╗   ██╗██████╗ ██████╗ ██████╗  ██████╗ ████████╗███████╗
██║  ██║╚██╗ ██╔╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝
███████║ ╚████╔╝ ██████╔╝██████╔╝██║  ██║██║   ██║   ██║   ███████╗
██╔══██║  ╚██╔╝  ██╔═══╝ ██╔══██╗██║  ██║██║   ██║   ██║   ╚════██║
██║  ██║   ██║   ██║     ██║  ██║██████╔╝╚██████╔╝   ██║   ███████║
╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝   ╚══════╝
                 T E T S U O   -   D O T F I L E S                                        
                                                                                                        
                                                                                                        
 # hyprdots-tetsuo

**⚠️ Requiere instalar previamente la configuración base de [JaKooLit](https:https://github.com/JaKooLit/Arch-Hyprland)**

Configuración personalizada de **Hyprland** basada en los dotfiles de JaKooLit, adaptada por **Tetsuo** para **Arch Linux**.

🔧 **Enfocada en una experiencia productiva, minimalista y ligeramente retro**, con un diseño limpio, funcional y adaptable al flujo de trabajo diario.

> ⚠️ Este proyecto es altamente personal. No está pensado para ser una configuración genérica ni para otros usuarios, sino como un entorno de trabajo ajustado a mis gustos y necesidades.

---

## 📁 Estructura del repositorio

- `hypr/`  
  Configuración principal de Hyprland.

- `UserConfigs/`  
  Configuración modular separada por categorías: temas, reglas de ventana, animaciones, atajos de teclado, etc.

- `initial-boot.sh`  
  Script de arranque inicial para aplicar el fondo de pantalla y los colores del sistema.

- `.config/`  
  Archivos de configuración para las siguientes aplicaciones:
  - `cava`
  - `fastfetch`
  - `kitty`
  - `mpd`
  - `neofetch` *(opcional)*
  - `nvim`
  - `qutebrowser` *(opcional)*
  - `rmpc`
  - `rofi`
  - `swaync`
  - `wallust`
  - `waybar`
  - `wlogout`

- `.themes/`  
  Temas GTK utilizados: **Gruvbox**, **Catppuccin**, **Tokyonight**.

- `.icons/`  
  Paquetes de iconos utilizados.

---

## 📸 Screenshots

| Escritorio Principal | Escritorio Secundario |
|----------------------|------------------------|
| ![desktop](screenshots/desktop.png) | ![desktop2](screenshots/desktop2.png) |

| Rofi Launcher | Rofi Powermenu |
|---------------|----------------|
| ![rofi1](screenshots/rofi1.png) | ![rofi2](screenshots/rofi2.png) |

| Wlogout | Código (Neovim) |
|---------|-----------------------------|
| ![wlogout](screenshots/wlogout.png) | ![codess](screenshots/codess.png) |

---

## 🌈 Colores Automáticos Basados en el Wallpaper

Esta configuración está pensada para adaptar automáticamente los colores del sistema al fondo de pantalla actual usando `pywal` y `wallust`.

Los colores se aplican a:

- `waybar` (barra de estado)
- `rofi` (launcher)
- `kitty` (terminal)
- `neovim` (tema dinámico)
- `rmpc` (cliente de MPD)
- `swaync`, `wlogout`, entre otros

Todo esto ocurre al iniciar sesión o ejecutar el script `initial-boot.sh`, el cual detecta el wallpaper y actualiza los colores globalmente.

---

## ⚙️ Requisitos

Este setup depende de varias herramientas. Algunas vienen incluidas en la configuración base de JaKooLit, otras debes instalarlas manualmente:

### Incluidas con JaKooLit:
- `rofi`
- `swaync`
- `waybar`
- `wlogout`
- `kitty`
- `mpd`
- `wallust`

### Adicionales (debes instalarlas tú):
```bash
- `pywal`
- `mpc`
- `rmpc`
- `neovim`
- `qutebrowser`
- `neofetch`i

## 🙏 Créditos

- [JaKooLit/hyprdots](https://github.com/JaKooLit/hyprdots) – Configuración base de donde partí para crear mi entorno.
- [rxyhn](https://github.com/rxyhn) – Inspiración en estética minimalista y retro.
- [eylles/wallust](https://github.com/eylles/wallust) – Herramienta clave para gestionar esquemas de colores basados en wallpapers.
- [dylanaraps/pywal](https://github.com/dylanaraps/pywal) – Utilidad para generar colores automáticos desde imágenes.


sudo pacman -S pywal rmpc mpc neovim qutebrowser 
yay -S neofetch

