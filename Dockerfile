# Använd en officiell Python-bild som basbild
FROM python:3.11-slim

# Sätt arbetskatalogen i containern
WORKDIR /app

# Kopiera requirements.txt till arbetskatalogen
COPY requirements.txt .

# Installera nödvändiga paket inklusive ca-certificates
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Installera Python-paket som anges i requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera hela applikationskoden till arbetskatalogen
COPY . .

# Ställ in miljövariabler
ENV FLASK_APP=app.py

# Exponera port 5000 för Flask-applikationen
EXPOSE 5000

# Starta Flask-applikationen
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]