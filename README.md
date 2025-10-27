# Python App Launcher

A simple **Python-based App Launcher** for Windows with console interface and keyboard navigation.  
Easily manage, launch, and organize your frequently used applications.

---

## Features

- Display all saved applications in a **list**.
- **Add new apps** by selecting executable files (`.exe`).
- **Delete apps** from the list.
- **Launch apps** directly from the console.
- Automatically saves app list in JSON format at:
```%LOCALAPPDATA%\PythonAppLauncher\apps.json```
- Additional Windows controls:
- **Clear temp folders** (`C:\Windows\Temp`, `%LOCALAPPDATA%\Temp`)
- **Shutdown Windows**
- **Delete Windows system files** (⚠️ Dangerous — requires double confirmation)

---

## Installation

1. Ensure **Python 3.x** is installed on your system.
2. Clone the repository:
 ```bash
 git clone https://github.com/yourusername/python-app-launcher.git
```
3.Navigate to the folder:

```bash
cd python-app-launcher
```
4.Run the app:

```bash
python app.py
```
### Recommend Python Version: Python 3.11.9
## Usage

### Navigate and operate the app using the keyboard:

### Menu Option	Action Key(s)
- Move Up / Down	Navigate the menu	W / S or ↑ / ↓
- Launch App	Open the selected application	Enter / →
- Add new app	Add a new executable to the list	Select from menu
- Delete an app	Remove an app from the list	Select from menu
- Clear temp folders	Delete temp files from Windows folders	Select from menu
- Shutdown Windows	Shutdown the computer	Select from menu
- Delete Windows files ⚠️	Attempt to delete Windows system files	Requires typing DELETE
- Exit	Quit the launcher	Select from menu

## 🚨 Important Notes
- Irreversible Actions: Be extremely cautious when using the Shutdown and Delete Windows Files features, as these actions are irreversible.

- First Run: The launcher will automatically create a default set of applications if the apps.json configuration file is not found upon launch

## File Structure
```bash
PythonAppLauncher/
├── app.py           # Main application
├── README.md        # Project README
└── apps.json        # Stored app list (created automatically)
```
## Screenshots
![คำอธิบายภาพหน้าจอ](ลิงก์ URL ของรูปภาพ)

License
- Opensource

Author
## Tayakorn000
