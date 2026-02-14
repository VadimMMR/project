FROM daygo555/device-os-libs@sha256:b72394a3867321660a0a79c9fa056d9d2ba526c8c92110ee2d3c2e9903322b15 AS libs

FROM python:3.9-slim

# Копируем ВСЮ папку site-packages (включая psutil и py-cpuinfo)
COPY --from=libs /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/

WORKDIR /app
COPY main.py .

CMD ["python", "main.py"]