import os
from PIL import Image
import numpy as np

# Percorso della cartella dataset
dataset_path = "./data/notMNIST_small/"

classes = sorted(os.listdir(dataset_path))
print(f"Classi trovate: {classes}")

images = []
labels = []

# Carico le immagini
for label_idx, class_name in enumerate(classes):
    class_dir = os.path.join(dataset_path, class_name)
    if os.path.isdir(class_dir):
        for img_name in os.listdir(class_dir)[:200]:  # Prendo max 200 immagini per classe
            img_path = os.path.join(class_dir, img_name)
            try:
                img = Image.open(img_path).convert('L')
                img_resized = img.resize((28, 28))
                images.append(np.array(img_resized))
                labels.append(label_idx)
            except Exception as e:
                print(
    f"Errore con immagine {img_path}: {e}"
)
                
