from os_system.main import get_os_name
from device.main import get_device_info

def get_info_divice():
    os_info = get_os_name()
    all_info = get_device_info()

    cpu_info = all_info["cpu"]
    gpu_info = all_info["gpu"]
    ram_info = all_info["ram"]
    
    print("OS:", os_info)
    print("CPU:", cpu_info)
    print("GPU:", gpu_info)
    print("RAM:", ram_info)

if __name__ == "__main__":
    get_info_divice()