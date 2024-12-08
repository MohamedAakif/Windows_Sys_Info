# Windows_Sys_Info

This Python script gathers essential system information for audit and asset management purposes. It provides details such as operating system, manufacturer, model, IP address, MAC address, and more. The script also includes a user-friendly GUI for viewing the information and options to either send it via email or save it to a text file.

# Features

- Retrieves operating system, manufacturer, model, serial number, network details, and user information.
- Displays the gathered information in a graphical interface.
- Buttons for sending the data via email or saving it to a file.
- Sends the system information as an email using Outlook.
- Saves the information to a text file for record-keeping.

# Requirements

- Supported OS: Windows
- Python Version: Python 3.x

Libraries:

- tkinter
- wmi
- pywin32
- getmac

# Installation

Install Python 3.x if not already installed.
Install the required Python libraries:

    pip install wmi pywin32 getmac

# Usage

- Clone or download the script.
- Run the script in a Python environment.

      python3 system_audit_gui.py

# Running the Script

- Method 1: 
  * Open a terminal and navigate to the script’s directory.
  * Make the script executable (if needed):

        chmod +x system_audit_gui.py

  * Run the script:

        python3 system_audit_gui.py
- Method 2:
  * Navigate to the script’s directory.
  * Right Click > Open with Python

# Using the GUI

- The system information is displayed in a read-only text box.
- Click the Send Email button to email the information.
- Click the Save to File button to save the information as information.txt in the current directory.

# Notes

- The email functionality requires Microsoft Outlook to be installed and configured on your system.
- The script is tailored for Windows due to its reliance on pywin32 and wmi libraries.

# Troubleshooting

- Missing Libraries: If you encounter errors about missing libraries, ensure all dependencies are installed using pip install.
- Email Errors:
  * Ensure Outlook is installed and configured.
  * Verify the recipient’s email address in the script.
