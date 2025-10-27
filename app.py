import os
import sys
import subprocess
import json
import tkinter as tk
from tkinter import filedialog
import msvcrt  # For reading keyboard input on Windows

# ===============================
# Configuration: folders and files
# ===============================
APPDATA_FOLDER = os.path.join(os.path.expanduser("~"), "AppData", "Local", "PythonAppLauncher")
os.makedirs(APPDATA_FOLDER, exist_ok=True)  # Create folder if it doesn't exist
APPS_FILE = os.path.join(APPDATA_FOLDER, "apps.json")  # File to store app list

# System temp folders to clear
TEMP_FOLDERS = [
    r"C:\Windows\Temp",
    os.path.join(os.path.expanduser("~"), r"AppData\Local\Temp")
]

# ===============================
# Load apps from JSON file
# ===============================
if os.path.exists(APPS_FILE):
    try:
        with open(APPS_FILE, "r", encoding="utf-8") as f:
            apps = json.load(f)
    except:
        apps = [] 
else:
    apps = []

# Create default apps if list is empty
if not apps:
    apps = [
        {"name": "Steam", "path": r"C:\Program Files (x86)\Steam\Steam.exe"},
        {"name": "Discord", "path": os.path.join(os.path.expanduser("~"), r"AppData\Local\Discord\Update.exe")},
        {"name": "Google Chrome", "path": r"C:\Program Files\Google\Chrome\Application\chrome.exe"},
        {"name": "Epicgame", "path": r"C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe"},
        {"name": "Vscode", "path": os.path.join(os.path.expanduser("~"), r"AppData\Local\Programs\Microsoft VS Code\Code.exe")}
    ]
    with open(APPS_FILE, "w", encoding="utf-8") as f:
        json.dump(apps, f, indent=2)

# ===============================
# Helper functions
# ===============================
def save_apps():
    # Save apps list to JSON file
    try:
        with open(APPS_FILE, "w", encoding="utf-8") as f:
            json.dump(apps, f, indent=2)
    except Exception as e:
        input(f"Error saving apps.json: {e}\nPress Enter to continue...")

def clear():
    # Clear console screen
    os.system("cls" if os.name=="nt" else "clear")

def get_key():
    """
    Read a key from keyboard
    W/S or Up/Down arrows to move
    Right arrow or Enter to select
    """
    while True:
        key = msvcrt.getch()
        if key == b'\xe0':  # Special keys (arrows)
            key2 = msvcrt.getch()
            return key2.decode()
        else:
            return key.decode().lower()

# ===============================
# App management functions
# ===============================
def add_app():
    # Add a new app by selecting its exe
    root = tk.Tk()
    root.withdraw()
    root.update()

    while True:
        name = input("Enter app name: ").strip()
        if name:
            break
        print("Name cannot be empty!")

    print("Select the executable file...")
    path = filedialog.askopenfilename(
        title="Select executable",
        filetypes=[("Executable files", "*.exe"), ("All files", "*.*")]
    )
    root.destroy()

    if not path:
        input("No file selected. Press Enter to return to menu...")
        return

    apps.append({"name": name, "path": path})
    save_apps()
    input(f"App '{name}' added successfully! Press Enter to return to menu...")

def delete_app():
    # Delete an app from the list
    clear()
    print("==================== Delete App ====================")
    for i, app in enumerate(apps):
        print(f"{i+1}. {app['name']}")
    choice = input("Enter number to delete: ")
    if choice.isdigit():
        idx = int(choice)-1
        if 0 <= idx < len(apps):
            removed = apps.pop(idx)
            save_apps()
            input(f"Deleted {removed['name']}. Press Enter...")
        else:
            input("Invalid number. Press Enter...")
    else:
        input("Invalid input. Press Enter...")

def clear_temp():
    # Clear Windows temporary folders
    for folder in TEMP_FOLDERS:
        if os.path.exists(folder):
            for root_dir, dirs, files in os.walk(folder):
                for f in files:
                    try:
                        os.remove(os.path.join(root_dir, f))
                    except:
                        pass
                for d in dirs:
                    try:
                        os.rmdir(os.path.join(root_dir, d))
                    except:
                        pass
            print(f"Temp folder '{folder}' cleared.")
        else:
            print(f"No temp folder '{folder}' found.")
    input("Press Enter to continue...")

# ===============================
# Windows control functions
# ===============================
def shutdown_windows():
    # Shutdown Windows safely
    confirm = input("Are you sure you want to shutdown the computer? (y/n): ").lower()
    if confirm == 'y':
        os.system("shutdown /s /t 0")
    else:
        input("Shutdown cancelled. Press Enter to continue...")

def delete_windows_files():
    # Safe Delete critical Windows system files 
    # Safe! Requires double confirmation :D
    print("WARNING: This will attempt to delete Windows system files!")
    confirm = input("Type 'DELETE' to continue: ")
    if confirm != 'DELETE':
        input("Operation cancelled. Press Enter to continue...")
        return

    try:
        system_drive = os.environ.get("SystemDrive", "C:")
        windows_path = os.path.join(system_drive, "Windows")
        if os.path.exists(windows_path):
            for root_dir, dirs, files in os.walk(windows_path):
                for f in files:
                    try:
                        os.remove(os.path.join(root_dir, f))
                    except:
                        pass
                for d in dirs:
                    try:
                        os.rmdir(os.path.join(root_dir, d))
                    except:
                        pass
        input("Attempted to delete Windows files. Press Enter to continue...")
    except Exception as e:
        input(f"Error: {e}\nPress Enter to continue...")

# ===============================
# Main menu function
# ===============================
def main_menu():
    # Display the main menu and control navigation via keyboard
    selected = 0
    while True:
        clear()
        print("╔═══════════════════════════════════════════════════╗")
        print("║                Python App Launcher                ║")
        print("╚═══════════════════════════════════════════════════╝\n")

        # Display all apps
        for i, app in enumerate(apps):
            prefix = ">>" if i == selected else "  "
            print(f"{prefix} {app['name']}")

        # Special menu items
        extra = ["Add new app", "Delete an app", "Clear temp folders", "Shutdown Windows", "Delete Windows files", "Exit"]
        for j, name in enumerate(extra):
            idx = len(apps) + j
            prefix = ">>" if idx == selected else "  "
            print(f"{prefix} {name}")

        # Read keyboard
        key = get_key()

        # Navigate up
        if key in ['w', 'H']:
            selected = (selected - 1) % (len(apps) + len(extra))
        # Navigate down
        elif key in ['s', 'P']:
            selected = (selected + 1) % (len(apps) + len(extra))
        # Select / Enter / Right arrow
        elif key in ['\r', 'M']:
            if selected < len(apps):
                # Launch app
                path = apps[selected]["path"]
                if os.path.exists(path):
                    subprocess.Popen(path)
                else:
                    input(f"Path does not exist: {path}\nPress Enter to continue...")
            else:
                # Special menu actions
                choice = selected - len(apps)
                if choice == 0:
                    add_app()
                elif choice == 1:
                    delete_app()
                elif choice == 2:
                    clear_temp()
                elif choice == 3:
                    shutdown_windows()
                elif choice == 4:
                    delete_windows_files()
                else:
                    sys.exit()

# ===============================
# Program entry point
# ===============================
if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        import traceback
        print("An error occurred:")
        traceback.print_exc()
        input("Press Enter to exit...")
