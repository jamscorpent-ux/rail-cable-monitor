# Guna Python 3.10 sebagai asas
FROM python:3.10-slim

# Tetapkan folder kerja di dalam kotak
WORKDIR /app

# Salin fail kod ke dalam kotak
COPY rail_cable_monitor.py .

# Jalankan skrip anda
CMD ["python", "rail_cable_monitor.py"]
