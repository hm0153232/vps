import os
import subprocess
import shutil

username = "user"  # @param {type:"string"}
password = "root"  # @param {type:"string"}

os.system(f"useradd -m {username}")
os.system(f"adduser {username} sudo")
os.system(f"echo '{username}:{password}' | sudo chpasswd")
os.system("sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd")

Pin = 123456  # @param {type: "integer"}
Autostart = True  # @param {type: "boolean"}

class RemoteSetup:
    def __init__(self, user):
        os.system("apt update")
        self.installDesktopEnvironment()
        self.installRemmina()
        self.changewall()
        self.installGoogleChrome()
        self.installTelegram()
        self.installQbit()
        self.finish(user)

    @staticmethod
    def installDesktopEnvironment():
        os.environ["DEBIAN_FRONTEND"] = "noninteractive"

        # Preconfigure keyboard settings to avoid prompts
        os.system("echo 'keyboard-configuration keyboard-configuration/xkb-keymap select us' | sudo debconf-set-selections")
        os.system("echo 'keyboard-configuration keyboard-configuration/layoutcode string us' | sudo debconf-set-selections")
        os.system("echo 'keyboard-configuration keyboard-configuration/modelcode string pc105' | sudo debconf-set-selections")
        
        # Install XFCE4 and related packages
        os.system("apt install --assume-yes xfce4 desktop-base xfce4-terminal")
        os.system("bash -c 'echo \"exec /etc/X11/Xsession /usr/bin/xfce4-session\" > /etc/chrome-remote-desktop-session'")
        os.system("apt remove --assume-yes gnome-terminal")
        os.system("apt install --assume-yes xscreensaver")
        os.system("sudo apt purge --assume-yes light-locker")
        os.system("sudo apt install --reinstall xfce4-screensaver")
        os.system("systemctl disable lightdm.service")
    
        # Bypass keyboard configuration
        os.system("echo 'XKBLAYOUT=\"us\"' | sudo tee /etc/default/keyboard")
        os.system("sudo dpkg-reconfigure --frontend=noninteractive keyboard-configuration")

        print("Installed XFCE4 Desktop Environment and set default keyboard layout!")

    @staticmethod
    def installRemmina():
        subprocess.run(["apt", "install", "--assume-yes", "remmina"])
        print("Remmina Installed!")

    @staticmethod
    def installGoogleChrome():
        subprocess.run(["wget", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"])
        subprocess.run(["dpkg", "--install", "google-chrome-stable_current_amd64.deb"])
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'])
        print("Google Chrome Installed!")

    @staticmethod
    def installTelegram():
        subprocess.run(["apt", "install", "--assume-yes", "telegram-desktop"])
        print("Telegram Installed!")

    @staticmethod
    def changewall():
        os.system(f"curl -s -L -k -o xfce-verticals.png https://gitlab.com/chamod12/changewallpaper-win10/-/raw/main/CachedImage_1024_768_POS4.jpg")
        current_directory = os.getcwd()
        custom_wallpaper_path = os.path.join(current_directory, "xfce-verticals.png")
        destination_path = '/usr/share/backgrounds/xfce/'
        shutil.copy(custom_wallpaper_path, destination_path)
        print("Wallpaper Changed!")

    @staticmethod
    def installQbit():
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "install", "-y", "qbittorrent"])
        print("Qbittorrent Installed!")

    @staticmethod
    def finish(user):
        if Autostart:
            os.makedirs(f"/home/{user}/.config/autostart", exist_ok=True)
            link = "https://www.metatrader5.com/en/terminal/help/start_advanced/install_linux"
            colab_autostart = """[Desktop Entry]
Type=Application
Name=Colab
Exec=sh -c "sensible-browser {}"
Icon=
Comment=Open a predefined notebook at session signin.
X-GNOME-Autostart-enabled=true""".format(link)
            with open(f"/home/{user}/.config/autostart/colab.desktop", "w") as f:
                f.write(colab_autostart)
            os.system(f"chmod +x /home/{user}/.config/autostart/colab.desktop")
            os.system(f"chown {user}:{user} /home/{user}/.config")
        
        print("..........................................................") 
        print(".....Brought By The Disala................................") 
        print("..........................................................") 
        print("......#####...######...####....####...##.......####.......") 
        print("......##..##....##....##......##..##..##......##..##......")  
        print("......##..##....##.....####...######..##......######......") 
        print("......##..##....##........##..##..##..##......##..##......") 
        print("......#####...######...####...##..##..######..##..##......") 
        print("..........................................................") 
        print("..Youtube Video Tutorial - https://youtu.be/xqpCQCJXKxU ..") 
        print("..........................................................") 
        print(f"Log in PIN : {Pin}") 
        print(f"User Name : {username}") 
        print(f"User Pass : {password}") 
        while True:
            pass

try:
    if len(str(Pin)) < 6:
        print("Enter a pin more or equal to 6 digits")
    else:
        RemoteSetup(username)
except NameError as e:
    print("'username' variable not found, Create a user first")
