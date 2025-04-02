import psutil, GPUtil, time

def monitor_resources():
    with open("resource_log.txt", "w") as log:  # 파일 덮어쓰기(w) 모드로 실행!
        log.write("CPU,GPU\n")  # 헤더
    while True:
        cpu_usage = psutil.cpu_percent()
        gpu_usage = GPUtil.getGPUs()[0].load * 100 if GPUtil.getGPUs() else 0
        with open("resource_log.txt", "a") as log:
            log.write(f"{cpu_usage},{gpu_usage}\n")
        time.sleep(5)
