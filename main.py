from monitoring.resource_monitor import monitor_resources
from monitoring.network_monitor import monitor_network
from monitoring.process_monitor import monitor_processes
from hooking.api_hooker import start_hooking
from analysis.anomaly_detector import detect_anomalies
import threading

if __name__ == '__main__':
    threading.Thread(target=monitor_resources, daemon=True).start()
    threading.Thread(target=monitor_network, daemon=True).start()
    threading.Thread(target=monitor_processes, daemon=True).start()
    threading.Thread(target=start_hooking, daemon=True).start()
    threading.Thread(target=detect_anomalies, daemon=True).start()

    while True:
        pass  # 메인 스레드 유지
