import frida

def on_message(message, data):
    print("[프리다 메시지 수신]", message)
    with open("hook_log.txt", "a") as log:
        log.write(str(message) + "\n")

def start_hooking():
    pid = frida.spawn(r"C:\Program Files\Naver\Naver Whale\Application\whale.exe")
    session = frida.attach(pid)
    print(pid)
    script = session.create_script(open("hooking/hook_scripts/hook.js").read())
    script.on("message", on_message)
    script.load()
    frida.resume(pid)
    input("Press Enter to stop hooking...")