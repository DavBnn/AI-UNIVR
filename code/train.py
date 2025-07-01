import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
import numpy as np

from load_data import images, labels


from model import SimpleMLP

# Converto immagini e labels in tensori PyTorch
X = np.array(images) / 255.0  # Normalizzo tra 0 e 1
X = X.reshape(-1, 1, 28, 28)  # Aggiungo dimensione canale
X_tensor = torch.tensor(X, dtype=torch.float32)
y_tensor = torch.tensor(labels, dtype=torch.long)

# Creo il dataloader
dataset = TensorDataset(X_tensor, y_tensor)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# Inizializzo modello, loss e ottimizzatore
model = SimpleMLP()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training
n_epochs = 5
for epoch in range(n_epochs):
    running_loss = 0.0
    for inputs, targets in dataloader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    print(f"Epoch {epoch+1}/{n_epochs} - Loss: {running_loss/len(dataloader):.4f}")

print("Training completato!")
