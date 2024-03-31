import os

writeline = ""
text = ""


def fullcode():
    filepath = "/etc/NetworkManager/conf.d/default-wifi-powersave-on.conf"
    if os.path.exists(filepath) and os.access(filepath, os.W_OK):
        file = open(filepath, "w")
        file.write(writeline)
        print(text)

    else:
        print("/etc/NetworkManager/conf.d/default-wifi-powersave-on.conf not found, Please start the program as "
              "administrator: sudo python3 WifiPenguin.py. Also make sure your operating system is one of these: Debian"
              " or Debian-based distribution (Linux Mint, Ubuntu, KDE-neon, Pop!_OS, Zorin OS etc), Fedora, CentOS, "
              "AlmaLinux")


def maincode():
    global writeline
    global text
    text = "Wi-Fi Power Saving Disabled"
    writeline = """ [connection]
    wifi.powersave = 2"""
    fullcode()


def defaultcode():
    global writeline
    global text
    text = "Wi-Fi Power Saving Enabled"
    writeline = """ [connection]
    wifi.powersave = 3"""
    fullcode()


os.system('clear')

maintext = """
 __    __  ____  _____  ____      ____    ___  ____    ____  __ __  ____  ____  
|  T__T  Tl    j|     |l    j    |    \  /  _]|    \  /    T|  T  Tl    j|    \ 
|  |  |  | |  T |   __j |  T     |  o  )/  [_ |  _  YY   __j|  |  | |  T |  _  Y
|  |  |  | |  | |  l_   |  |     |   _/Y    _]|  |  ||  T  ||  |  | |  | |  |  |
l  `  '  ! |  | |   _]  |  |     |  |  |   [_ |  |  ||  l_ ||  :  | |  | |  |  |
 \      /  j  l |  T    j  l     |  |  |     T|  |  ||     |l     | j  l |  |  |
  \_/\_/  |____jl__j   |____j    l__j  l_____jl__j__jl___,_j \__,_j|____jl__j__j                                                                         
"""

print(maintext)
print("\n")
print("[1] Start Wifi Penguin" + "\n")

print("[2] Return to Default" + "\n")

print("[3] Exit" + "\n")

while True:
    try:
        print(" ")
        secim = int(input(">"))

        if secim == 1:
            print("")
            maincode()

        elif secim == 2:
            print("")
            defaultcode()

        elif secim == 3:
            break

    except ValueError:
        print("")
