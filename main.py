from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import threading
from os_system.main import get_complete_os_info
from device.main import get_device_info

# Глобальные переменные для хранения данных
_os_info = None
_cpu_info = None
_gpu_info = None
_ram_info = None

def get_info_divice():
    global _os_info, _cpu_info, _gpu_info, _ram_info
    
    os_info = get_complete_os_info()
    all_info = get_device_info()

    cpu_info = all_info["cpu"]
    gpu_info = all_info["gpu"]
    ram_info = all_info["ram"]
    
    # Сохраняем в глобальные переменные
    _os_info = os_info
    _cpu_info = cpu_info
    _gpu_info = gpu_info
    _ram_info = ram_info
    
    globals().update(os_info)      # type: ignore
    globals().update(cpu_info)     # type: ignore
    globals().update(gpu_info)     # type: ignore
    globals().update(ram_info)     # type: ignore

    print_info()
    
    return {
        "os": os_info,
        "cpu": cpu_info,
        "gpu": gpu_info,
        "ram": ram_info
    }

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

class DeviceInfoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Получаем свежие данные
            result = get_info_divice()
            
            # Отправляем ответ
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = json.dumps(result, indent=2, default=str)
            self.wfile.write(response.encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_response = json.dumps({"error": str(e)}, indent=2)
            self.wfile.write(error_response.encode())
    
    def log_message(self, format, *args):
        # Подавляем логи запросов для чистоты вывода
        pass

def run_web_server():
    """Запускает веб-сервер в отдельном потоке"""
    server = HTTPServer(('0.0.0.0', 10000), DeviceInfoHandler)
    print(f"\n🌐 Веб-сервер запущен на порту 10000")
    print(f"📝 Открой в браузере: http://localhost:10000")
    print(f"🔍 Или на Render: https://твой-сервис.render.com\n")
    server.serve_forever()

if __name__ == "__main__":
    # Запускаем веб-сервер в отдельном потоке
    web_thread = threading.Thread(target=run_web_server, daemon=True)
    web_thread.start()
    
    # Твоя оригинальная логика
    get_info_divice()
    
    # Держим главный поток активным
    try:
        while True:
            import time
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Программа завершена")