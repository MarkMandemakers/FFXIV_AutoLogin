# Final Fantasy XIV AutoLogin
Automatically start the Final Fantasy XIV Launcher, login and start the game.
I wrote this script since it was becoming quite a hassle (read: am lazy) to login to my password manager, find my FFXIV account, copy its password and paste it into the FFXIV Launcher.

## Usage
- Make sure you have installed [Python](https://www.python.org/) and the required modules, see below
- Change settings in [FFXIV_Login_Settings.py](https://github.com/MarkMandemakers/FFXIV_AutoLogin/blob/main/FFXIV_Login_Settings.py) to reflect launcher location and password
- If your account has an authenticator with one-time passwords, please see below for additional instructions. Otherwise leave *token_2fa* empty!
- It is recommended to create a shortcut to the main script; use this as your FFXIV shortcut from now on
- Launch the script and let it do its magic :)

**Note** - Your password (and optionally 2FA token) will be stored as plaintext in the file, store this file and script in a safe location on your PC!

### Using one-time passwords
In order to use Square Enix' one-time passwords (2FA), it is easiest to remove and re-install the authenticator as follows:
- Remove your existing authenticator from your Square Enix account
- Start the process to setup a new **software** authenticator
- Click on "unable to Scan QR Code" when the QR code is given
- Copy the code, without spaces into **both** your 2FA app of choice, e.g. Google Authenticator, and the settings file for this script under *token_2fa*
- Setup the authenticator as usual and it should now be synced with script

## Requirements
Written for Python 3.8.x.
Requires the following modules (see [requirements.txt](https://github.com/MarkMandemakers/FFXIV_AutoLogin/blob/main/requirements.txt)):
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- [psutil](https://pypi.org/project/psutil/)
- (optional) [PyOTP](https://github.com/pyauth/pyotp) - only required if you use one-time passwords

## Author & License
FFXIV AutoLogin is created by [Mark Mandemakers](https://github.com/MarkMandemakers) and is licensed under the MIT License - see the [LICENSE](https://github.com/MarkMandemakers/FFXIV_AutoLogin/blob/main/LICENSE) file for details.
