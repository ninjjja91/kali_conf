sudo apt update

sudo apt install kali-desktop-i3 terminator i3blocks feh grub-customizer ranger awesome-extra dunst 
sudo apt purge xdg-desktop-portal
cp -r .config/* ~/.config/
cp -r .fehbg ~/.fehbg
cp -r .fonts ~/.fonts
cp -r .wallpapers ~/.wallpapers
cp -r .xinitrc ~/.xinitrc
sudo systemctl disable lightdm.service
