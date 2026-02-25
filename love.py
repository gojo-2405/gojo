import platform
import socket
import psutil
import datetime

def system_report():
    print("=== SYSTEM HEALTH CHECK REPORT ===")
    print(f"Timestamp       : {datetime.datetime.now()}")
    print(f"Hostname        : {socket.gethostname()}")
    print(f"OS              : {platform.system()} {platform.release()}")
    print(f"Architecture    : {platform.machine()}")
    print(f"Python Version  : {platform.python_version()}")
    print(f"CPU Cores       : {psutil.cpu_count(logical=True)}")
    print(f"Memory Usage    : {psutil.virtual_memory().percent}%")
    print(f"Disk Usage      : {psutil.disk_usage('/').percent}%")
    print("==================================")

if __name__ == "__main__":
    system_report()
