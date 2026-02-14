from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from os_system.main import get_os_name
from device.main import get_device_info

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        os_info = get_os_name()
        all_info = get_device_info()
        
        cpu_info = all_info["cpu"]
        gpu_info = all_info["gpu"]
        ram_info = all_info["ram"]
        
        response = {
            "os": os_info,
            "cpu": cpu_info,
            "gpu": gpu_info,
            "ram": ram_info
        }
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response, indent=2).encode())

if __name__ == "__main__":
    port = 10000  # Render использует порт из переменной окружения PORT
    server = HTTPServer(('0.0.0.0', port), Handler)
    print(f"Server running on port {port}")
    server.serve_forever()