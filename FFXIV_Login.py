# Import modules
from os import startfile, getcwd
import pyautogui
from time import sleep
from psutil import process_iter
from sys import exit
import FFXIV_Login_Settings

# Settings

# Check if FFXIV Client is already running
launcher = "ffxivlauncher.exe" in (p.name() for p in process_iter())
client = "ffxiv_dx11.exe" in (p.name() for p in process_iter())

# Start FFXIV Launcher if the game is not active yet
cwd = getcwd()
if not launcher and not client:
    # Start launcher
    print("Launching FFXIV... ", end="", flush=True)
    startfile(FFXIV_Login_Settings.launcher_loc)
    
    # Wait for it to start, looking for the "login" button specifically
    while pyautogui.locateOnScreen(f"{cwd}/img/FFXIV_Loginbutton.png", grayscale=True) == None:
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
if pyautogui.locateOnScreen(f"{cwd}/img/FFXIV_Loginbutton.png", grayscale=True) == None:
    print("Cannot login, likely an update or window not in view?")
    exit()
# end if

# Enter login information
print("Logging in... ", end="", flush=True)
pyautogui.write(FFXIV_Login_Settings.password)
pyautogui.press(["tab"]*3)
pyautogui.press("enter")

# Wait then play game, looking for the "play" button specifically
while pyautogui.locateOnScreen(f"{cwd}/FFXIV_Playbutton.png", grayscale=True) == None:
    sleep(1)
# end while
print("DONE")
print("Have fun!")
pyautogui.press("enter")
