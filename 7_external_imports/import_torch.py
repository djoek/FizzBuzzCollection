import logging

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

logger = logging.getLogger(__name__)

# Parameters for easy experimentation
NUM_BITS = 12
HIDDEN_SIZE1 = 256
HIDDEN_SIZE2 = 128
OUTPUT_SIZE = 4
NUM_EPOCHS = 5000
LEARNING_RATE = 0.005

TRAIN_START = 101
TRAIN_END = 2 ** NUM_BITS - 1


# Define useful functions and classes
def binary_encode(i):
    return np.array([i >> d & 1 for d in range(NUM_BITS)])


def fizz_buzz_encode(i):
    return (i % 5 == 0)*2 + (i % 3 == 0)


def fizz_buzz_decode(i, prediction):
    return [str(i), "Fizz", "Buzz", "FizzBuzz"][prediction]


class FizzBuzzModel(nn.Module):

    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(NUM_BITS, HIDDEN_SIZE1),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(HIDDEN_SIZE1, HIDDEN_SIZE2),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(HIDDEN_SIZE2, OUTPUT_SIZE),
        )

    def forward(self, x):
        return self.model(x)


# Configure torch backend
cuda = "cuda" if torch.cuda.is_available() else None
mps = "mps" if torch.backends.mps.is_available() else None
device = torch.device(cuda or mps or "cpu")
logger.debug(f"Using device: {device}")

# Create model and stuff
model = FizzBuzzModel().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

# Training Data & Labels
training_range = range(TRAIN_START, TRAIN_END + 1)
train_inputs = torch.from_numpy(np.array([binary_encode(i) for i in training_range], dtype=np.float32)).to(device)
train_labels = torch.from_numpy(np.array([fizz_buzz_encode(i) for i in training_range], dtype=np.long)).to(device)

# Train the model in epochs
for epoch in range(1, NUM_EPOCHS+1):
    model.train()
    outputs = model(train_inputs)
    loss = criterion(outputs, train_labels)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 500 == 0:
        logger.debug(f"Epoch [{epoch}/{NUM_EPOCHS}], Loss: {loss.item():.4f}")


def fizzbuzz(i: int) -> str:
    model.eval()
    with torch.no_grad():
        prediction = model(torch.from_numpy(np.array([binary_encode(i)], dtype=np.float32)).to(device))
        label = torch.argmax(prediction, dim=1)

        return fizz_buzz_decode(i, label)


print(*(fizzbuzz(x) for x in range(1, 101)), sep='\n')
