import psutil, time

def monitor_network():
    while True:
        connections = psutil.net_connections()
        with open("network_log.txt", "a") as log:
            for conn in connections:
                if conn.status == 'ESTABLISHED':
                    log.write(f"{conn.laddr} -> {conn.raddr}\n")
                time.sleep(10)