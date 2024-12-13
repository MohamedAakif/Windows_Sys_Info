import tkinter as tk
from tkinter import messagebox
from os import environ, getlogin, getcwd
from wmi import WMI
from socket import gethostbyname, gaierror
from platform import system, uname, release
from getmac import get_mac_address
import win32com.client as win32
import traceback

class Information:
    try:
        operating_system = f"{system().lower()} {release()}"
        computer_name = uname().node
        computer_version = uname().version
        domain = environ.get('userdomain', 'Unknown Domain')
        username = getlogin()
        wmi_obj = WMI()
        manufacturer = wmi_obj.Win32_ComputerSystem()[0].manufacturer
        serialnumber = wmi_obj.Win32_Bios()[0].SerialNumber
        model = wmi_obj.Win32_ComputerSystem()[0].model

        try:
            ip_address = gethostbyname(computer_name)
        except gaierror:
            ip_address = "Unknown IP Address"

        mac_address = get_mac_address() or "Unknown MAC Address"

        display_information = f"""
        Basic Information
        Username            : {username.capitalize()}
        Computer Name       : {computer_name}
        Manufacturer        : {manufacturer.upper()}
        Model               : {model}
        Operating System    : {operating_system.capitalize()}
        Version             : {computer_version}
        Serial Number       : {serialnumber.upper()}

        Network Information
        IP Address          : {ip_address}
        MAC Address         : {mac_address.upper()}
        Domain Name         : {domain.upper()}
        """
    except Exception as e:
        display_information = "Error gathering information."
        traceback.print_exc()

def send_email():
    try:
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = 'test@mail.com'  # Update with the recipient's email
        mail.Subject = f"{Information.computer_name} {Information.username} - System Information"
        mail.Body = Information.display_information
        mail.Send()
        messagebox.showinfo("Success", "Email sent successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {e}")

def save_to_file():
    try:
        desktop_location = getcwd()
        information_file_path = f"{desktop_location}\information.txt"
        with open(information_file_path, "w") as information_file:
            information_file.write(Information.display_information)
        messagebox.showinfo("Success", f"Information saved to {information_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file: {e}")

def main():
    root = tk.Tk()
    root.title("System Information")

    # Display information in a text widget
    text_widget = tk.Text(root, wrap=tk.WORD, width=80, height=25)
    text_widget.insert(tk.END, Information.display_information)
    text_widget.configure(state=tk.DISABLED)
    text_widget.pack(padx=10, pady=10)

    # Buttons for sending email and saving to file
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    send_email_button = tk.Button(button_frame, text="Send Email", command=send_email, width=20)
    send_email_button.grid(row=0, column=0, padx=10)

    save_file_button = tk.Button(button_frame, text="Save to File", command=save_to_file, width=20)
    save_file_button.grid(row=0, column=1, padx=10)

    root.mainloop()

if __name__ == "__main__":
    main()
