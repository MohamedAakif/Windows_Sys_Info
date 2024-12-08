import os
import subprocess
from pathlib import Path

def log(message):
    log_file = Path("/var/log/linux_maintenance.log")
    with log_file.open("a") as file:
        file.write(message + "\n")

def execute_command(command, ignore_error=False):
    try:
        log(f"Executing: {command}")
        subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        log(f"Error executing '{command}': {e.stderr.decode().strip()}")
        if not ignore_error:
            print(f"Error executing: {command}. Check logs for details.")

def update_system():
    print("Updating system...")
    execute_command("sudo apt update && sudo apt upgrade -y")
    execute_command("sudo apt autoremove -y")
    execute_command("sudo apt autoclean")

def clean_temp_files():
    print("Cleaning temporary files...")
    execute_command("sudo rm -rf /tmp/*")
    execute_command("sudo rm -rf /var/tmp/*")

def clean_logs():
    print("Cleaning old logs...")
    execute_command("sudo find /var/log -type f -name '*.log' -exec truncate -s 0 {} \;")

def clean_user_cache():
    print("Cleaning user cache...")
    cache_dirs = ["~/.cache", "~/.mozilla/firefox", "~/.config/google-chrome", "~/.config/chromium"]
    for directory in cache_dirs:
        expanded_dir = os.path.expanduser(directory)
        execute_command(f"rm -rf {expanded_dir}/*", ignore_error=True)

def flush_dns():
    print("Flushing DNS cache...")
    execute_command("sudo systemd-resolve --flush-caches")

def boost_performance():
    print("Boosting system performance...")
    execute_command("echo 'vm.swappiness=10' | sudo tee -a /etc/sysctl.conf")
    execute_command("sudo sysctl -p")

def monitor_disk_usage():
    print("Monitoring disk usage...")
    execute_command("df -h > ~/disk_usage_report.txt")
    log("Disk usage report saved to ~/disk_usage_report.txt")

def clear_recycle_bin():
    print("Emptying recycle bin...")
    execute_command("rm -rf ~/.local/share/Trash/*")

def main():
    if os.geteuid() != 0:
        print("Please run this script as an administrator (sudo).")
        log("Script not running as administrator.")
        return

    log("Starting maintenance script...")

    update_system()
    clean_temp_files()
    clean_logs()
    clean_user_cache()
    flush_dns()
    clear_recycle_bin()
    monitor_disk_usage()
    boost_performance()

    log("Maintenance script completed successfully.")
    print("Maintenance completed. Check /var/log/linux_maintenance.log for details.")

if __name__ == "__main__":
    main()
