import os
import subprocess
import ctypes
from typing import List

class FileFence:
    def __init__(self, file_path: str):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")

    def set_permissions(self, user: str, permissions: List[str]):
        """Set permissions for a specified user on the file."""
        valid_permissions = {"read", "write", "execute", "full"}
        for perm in permissions:
            if perm.lower() not in valid_permissions:
                raise ValueError(f"Invalid permission: {perm}. Valid permissions are: {valid_permissions}")
        
        permission_string = ",".join(permissions)
        command = f'icacls "{self.file_path}" /grant {user}:(OI)(CI)({permission_string})'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode != 0:
            raise OSError(f"Error setting permissions: {result.stderr.strip()}")

    def remove_user_permissions(self, user: str):
        """Remove all permissions for a specified user."""
        command = f'icacls "{self.file_path}" /remove {user}'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode != 0:
            raise OSError(f"Error removing permissions: {result.stderr.strip()}")

    def make_file_private(self):
        """Restrict file access to the current user only."""
        current_user = os.getlogin()
        command = f'icacls "{self.file_path}" /reset /grant {current_user}:(F)'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode != 0:
            raise OSError(f"Error making file private: {result.stderr.strip()}")

def is_admin():
    """Check if the script is running with administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == "__main__":
    if not is_admin():
        print("This script requires administrative privileges. Please run it as an administrator.")
    else:
        file_path = input("Enter the path of the file to secure: ")
        file_fence = FileFence(file_path)

        print("Choose an option:")
        print("1. Set permissions")
        print("2. Remove user permissions")
        print("3. Make file private")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            user = input("Enter the username: ")
            permissions = input("Enter permissions (comma separated: read, write, execute, full): ").split(',')
            file_fence.set_permissions(user, permissions)
            print("Permissions set successfully.")
        elif choice == '2':
            user = input("Enter the username: ")
            file_fence.remove_user_permissions(user)
            print("Permissions removed successfully.")
        elif choice == '3':
            file_fence.make_file_private()
            print("File access restricted to the current user.")
        else:
            print("Invalid choice.")