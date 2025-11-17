import os 
import psutil 
import time

def printInfo():
    cpu_usage = psutil.cpu_percent()
    ram = psutil.virtual_memory()
    usage = psutil.disk_usage('/')

    print(f"CPU STATS: CPU USAGE: {cpu_usage} - RAM USAGE : {ram.percent} - DISK USAGE : {usage.percent}")
    if(cpu_usage > 80):
        print("CPU USAGE OVER 80%")
    if(usage.percent > 80):
        print("DISK USAGE OVER 80%")


if __name__ == "__main__":
    try:
        while True:
            printInfo()
            time.sleep(10)
    except KeyboardInterrupt:
        print("Stopped")