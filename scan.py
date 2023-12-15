import psutil

def check_unauthorized_processes():
    authorized_processes = ["explorer.exe", "chrome.exe", "python.exe"]  # Add authorized processes

    for process in psutil.process_iter(['pid', 'name']):
        process_name = process.info['name'].lower()
        if process_name not in authorized_processes:
            print(f"Unauthorized process found: {process_name}, PID: {process.info['pid']}")

if __name__ == "__main__":
    check_unauthorized_processes()
