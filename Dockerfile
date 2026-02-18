FROM daygo555/device-os-libs@sha256:9ceb205d4ce4c77c7da2b901707e6f32d5d6fffb0b56bf2e950e3d4bd136d881 AS libs

FROM python:3.9-slim

# Копируем site-packages (psutil, py-cpuinfo, os_system, device)
COPY --from=libs /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/

# Копируем ТОЛЬКО main.py (не перетираем библиотеки)
COPY main.py /app/main.py

WORKDIR /app

CMD ["python", "main.py"]