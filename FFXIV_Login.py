# Import modules
from os import startfile, getcwd
import pyautogui
from time import sleep
from psutil import process_iter
from sys import exit
import FFXIV_Login_Settings

# Only try to import PyOTP if a 2FA token was filled in settings
handle_2fa = False
if FFXIV_Login_Settings != "":
    try:
        import pyotp
        handle_2fa = True
    except ModuleNotFoundError:
        print("PyOTP is not installed, will not handle 2FA")
    # end try
else:
    print("No 2FA token found in settings, will not handle 2FA")
# end if

# Check if FFXIV Launcher or Client are already running
launcher = "ffxivlauncher.exe" in (p.name() for p in process_iter())
client = "ffxiv_dx11.exe" in (p.name() for p in process_iter())

# Get resolution of monitor to select correct image
y_res = pyautogui.size()[1]
if y_res == 1080:
    img_login = "FFXIV_Loginbutton_1080.png"
    img_play = "FFXIV_Playbutton_1080.png"
if y_res == 1440:
    img_login = "FFXIV_Loginbutton_1440.png"
    img_play = "FFXIV_Playbutton_1440.png"
else:
    # Use 1080p image as fallback
    img_login = "FFXIV_Loginbutton_1080.png"
    img_play = "FFXIV_Playbutton_1080.png"
# end if


# Start FFXIV Launcher if the game is not active yet
cwd = getcwd()
if not launcher and not client:
    # Start launcher
    print("Launching FFXIV... ", end="", flush=True)
    startfile(FFXIV_Login_Settings.launcher_loc)
    
    # Wait for it to start, looking for the "login" button specifically
    while pyautogui.locateOnScreen(f"{cwd}/img/{img_login}", grayscale=True) == None:
        sleep(1)
    # end while
    print("DONE")
elif launcher:
    print("FFXIV Launcher is already running")
else:
    print("FFXIV Client is already running, nothing to do...")
    exit()
# end if

# Verify if the game is actually ready to login by looking for the "login" button
if pyautogui.locateOnScreen(f"{cwd}/img/{img_login}", grayscale=True) == None:
    print("Cannot login, likely an update or window not in view?")
    exit()
# end if

# Enter login information and press login
print("Logging in... ", end="", flush=True)
pyautogui.write(FFXIV_Login_Settings.password)
pyautogui.press("tab")
if handle_2fa:
    totp = pyotp.TOTP(FFXIV_Login_Settings.token_2fa)
    pyautogui.write(totp.now())
# end if
pyautogui.press(["tab"]*2)
pyautogui.press("enter")

# Wait for successful login, looking for the "play" button specifically, then launch game
while pyautogui.locateOnScreen(f"{cwd}/img/{img_play}", grayscale=True) == None:
    sleep(1)
# end while
print("DONE")
print("Have fun!")
pyautogui.press("enter")
