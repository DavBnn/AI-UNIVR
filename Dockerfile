# Usa una immagine base di Python
FROM python:3.9-slim

# Imposta la directory di lavoro dentro il container
WORKDIR /app

# Copia tutto il contenuto del progetto dentro il container
COPY . .

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest torch torchvision matplotlib pillow numpy

# Comando di default: esegue i test quando parte il container
CMD ["pytest"]
