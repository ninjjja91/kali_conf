#!/bin/sh

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# merge in defaults and keymaps
[ -f /etc/xprofile ] && . /etc/xprofile
[ -f ~/.xprofile ] && . ~/.xprofile
if [ -f $sysresources ]; then







    xrdb -merge $sysresources

fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then







    xrdb -merge "$userresources"

fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi
export QT_QPA_PLATFORMTHEME=qt5ct
#export QT_STYLE_OVERRIDE=gtk2
#qtile start
#xbindkeys &
#/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
#feh --bg-fill ~/.wallpapers/arcane-12.jpg ~/.wallpapers/jinx.jpg &
#/home/m4z3/Downloads/./Kraken_Z_Playground.v1.1.1.Linux_x86_64.AppImage &
#picom -b &
#pulseaudio -D &
#xbindkeys &
#nm-applet &
#pamac-tray &
#pa-applet &
#blueman-applet &
#dwmstatus 2>&1 >/dev/null &
#nvidia-xconfig &
#xfce4-power-manager &

#xrandr --output DP-2 --auto --pos 1350x0 -r 60  --primary --output DP-0 --auto --scale 1.25 --pos 0x0 --rotate right -r 165 &
#while true; do
#   dwm >/dev/null 2>&1
#done

exec i3
