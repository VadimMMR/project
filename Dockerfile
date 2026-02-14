
FROM daygo555/device-os-libs:v1.1 AS libs

FROM python:3.9-slim

# Копируем библиотеки из первого образа
COPY --from=libs /usr/local/lib/python3.9/site-packages/device /usr/local/lib/python3.9/site-packages/device
COPY --from=libs /usr/local/lib/python3.9/site-packages/os_system /usr/local/lib/python3.9/site-packages/os_system

WORKDIR /app
COPY main.py .

CMD ["python", "main.py"]