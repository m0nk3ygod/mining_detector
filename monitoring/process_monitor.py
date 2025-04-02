import psutil, time

def monitor_processes():
    suspicious_names = ["miner", "xmrig", "minerd"]
    while True:
        for proc in psutil.process_iter(['pid', 'name']):
            if any(sus in proc.info['name'].lower() for sus in suspicious_names):
                with open("process_log.txt", "a") as log:
                    log.write(f"Suspicious process: {proc.info}\n")
        time.sleep(5)