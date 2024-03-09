sudo apt update
sudo grub-install --target=x86_64-efi --efi-directory=/boot/efi --removable --recheck
sudo apt install kali-desktop-i3 terminator i3blocks feh grub-customizer ranger awesome-extra dunst 
sudo apt purge xdg-desktop-portal 
sudo apt purge plymouth
cp -r .config/* ~/.config/
cp -r .fehbg ~/.fehbg
cp -r .fonts ~/.fonts
cp -r .wallpapers ~/.wallpapers
cp -r .xinitrc ~/.xinitrc
cp -r .zshrc ~/.zshrc 
sudo systemctl disable lightdm.service
sudo cp etc/40-libinput.conf /etc/X11/xorg.conf.d/0-libinput.conf
