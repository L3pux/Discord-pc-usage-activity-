from pypresence import Presence
import time
import platform
import distro
import subprocess

distro_name = distro.name() if platform.system() == "Linux" else "Unknown"

start = int(time.time())
client_id = "EnterYourID" 
RPC = Presence(client_id)
RPC.connect()

def format_uptime(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return f"{int(hours)} hours, {int(minutes)} mins"

def ram():
    try:
        command = "free -h"
        result = subprocess.run(command, stdout=subprocess.PIPE, text=True, shell=True)
        lines = result.stdout.split('\n')
        for line in lines:
            if line.startswith("Mem:"):
                total, used, free = line.split()[1], line.split()[2], line.split()[3]
                return f"{used}/{total}"
    except Exception as e:
        print(f"huh? {e}")
    return None

uptime_seconds = time.monotonic()
formatted_uptime = format_uptime(uptime_seconds)

while True:
    current_ram = ram()
    additional_info = "Some additional information"  # Add more information here
    formatted_uptime = format_uptime(uptime_seconds)

    RPC.update(
        large_image="status",
        large_text="aa",
        details=f"{distro_name} - {current_ram}",
        state=f"Uptime: {formatted_uptime}",
        start=start,
    )
    time.sleep(15)




 
