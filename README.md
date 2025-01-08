# FileFence

## Overview
FileFence is a Python script designed to enhance file security on Windows systems by managing advanced file permissions and access controls. It allows you to set, modify, or remove permissions for specific users and can also make files private to the current user.

## Features
- Set custom permissions for specific users (read, write, execute, full access).
- Remove all permissions for a specified user.
- Restrict file access to the current user only.

## Prerequisites
- Windows operating system.
- Administrative privileges to run the script.
- Python 3.x installed on your system.

## Installation
1. Clone the repository or download the `filefence.py` file.
2. Ensure Python is installed on your system.

## Usage
1. Open Command Prompt as an Administrator.
2. Navigate to the directory containing `filefence.py`.
3. Run the script using: `python filefence.py`.
4. Follow the on-screen prompts to set or modify file permissions.

## Examples
- **Set Permissions:** Assigns read and write permissions to a user.
  ```
  Enter the path of the file to secure: C:\path\to\file.txt
  Choose an option:
  1. Set permissions
  2. Remove user permissions
  3. Make file private
  Enter the number of your choice: 1
  Enter the username: User1
  Enter permissions (comma separated: read, write, execute, full): read,write
  ```

- **Remove User Permissions:** Removes all permissions for a user.
  ```
  Enter the path of the file to secure: C:\path\to\file.txt
  Choose an option:
  1. Set permissions
  2. Remove user permissions
  3. Make file private
  Enter the number of your choice: 2
  Enter the username: User1
  ```

- **Make File Private:** Restricts access to the current user.
  ```
  Enter the path of the file to secure: C:\path\to\file.txt
  Choose an option:
  1. Set permissions
  2. Remove user permissions
  3. Make file private
  Enter the number of your choice: 3
  ```

## Notes
- Ensure you have backup copies of important files before modifying permissions.
- This script requires administrative privileges to modify file permissions.

## License
This project is licensed under the MIT License - see the LICENSE file for details.