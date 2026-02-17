from os_system.main import get_complete_os_info
from device.main import get_device_info

def get_info_divice():
    os_info = get_complete_os_info()
    all_info = get_device_info()

    cpu_info = all_info["cpu"]
    gpu_info = all_info["gpu"]
    ram_info = all_info["ram"]
    
    globals().update(os_info)      # type: ignore
    globals().update(cpu_info)     # type: ignore
    globals().update(gpu_info)     # type: ignore
    globals().update(ram_info)     # type: ignore

    print_info()

def print_info():
    # Словарь со всеми переменными
    variables = {
        # ОС
        "os_name": os_name,
        "os_version": os_version,
        "os_build": os_build,
        "os_architecture_bits": os_architecture_bits,
        "os_architecture_type": os_architecture_type,
        "os_edition": os_edition,
        "os_kernel": os_kernel,
        "os_hostname": os_hostname,
        "os_username": os_username,
        "os_install_date": os_install_date,
        "os_last_boot": os_last_boot,
        "os_uptime_seconds": os_uptime_seconds,
        "os_uptime_formatted": os_uptime_formatted,
        "os_temp_path": os_temp_path,
        "os_timezone": os_timezone,
        "os_encoding": os_encoding,
        "os_is_64bit": os_is_64bit,
        
        # CPU
        "cpu_cores": cpu_cores,
        "cpu_threads": cpu_threads,
        "cpu_freq_GHz": cpu_freq_GHz,
        "cpu_model": cpu_model,
        "cpu_L3_MB": cpu_L3_MB,
        "cpu_avx2": cpu_avx2,
        "cpu_avx512": cpu_avx512,
        
        # GPU
        "gpu_model": gpu_model,
        "gpu_vram_GB": gpu_vram_GB,
        "gpu_core_freq_GHz": gpu_core_freq_GHz,
        "gpu_mem_freq_GHz": gpu_mem_freq_GHz,
        "gpu_architecture": gpu_architecture,
        "bus_width": bus_width,
        "gpu_cores": gpu_cores,
        "gpu_TDP": gpu_TDP,
        
        # RAM
        "ram_total_GB": ram_total_GB,
        "ram_freq_MHz": ram_freq_MHz,
        "ram_channels": ram_channels
    }
    
    # Выводим все переменные
    for name, value in variables.items():
        if value is None:
            print(f"{name}: None")
        else:
            print(f"{name}: {value}")

if __name__ == "__main__":
    get_info_divice()