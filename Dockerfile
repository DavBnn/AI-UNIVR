FROM python:3.9-slim

WORKDIR /app

COPY . .

# Dipendenze
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest torch torchvision matplotlib pillow numpy

CMD ["pytest"]
