
import numpy as np
import pandas as pd
from PIL import Image
import pickle


df = pd.read_csv('key_log2.csv', header=None)
df.columns = ['path', 'steer', 'throttle', 'brake']
df.dropna(inplace=True)

X, y = [], []
for _, row in df.iterrows():
    img = Image.open(row['path']).convert('L').resize((64, 48))
    X.append(np.array(img).flatten() / 255.0)
    y.append([row['steer'], row['throttle'], row['brake']])

x = np.array(X)
y = np.array(y)


np.random.seed(42)
w = np.random.randn(x.shape[1], 3) * 0.01
b = np.zeros((1, 3))


def predict(x, w, b):
    return np.dot(x, w) + b

def compute_loss(y_pred, y_true):
    return np.mean((y_pred - y_true) ** 2)

def train(x, y, w, b, lr=0.001, epochs=1500):
    for epoch in range(epochs):
        y_pred = predict(x, w, b)
        loss = compute_loss(y_pred, y)

        dw = np.dot(x.T, (y_pred - y)) * (2 / len(x))
        db = np.mean(2 * (y_pred - y), axis=0, keepdims=True)

        w -= lr * dw
        b -= lr * db

        if epoch % 10 == 0:
            print(f"Epoch {epoch}: Loss = {loss:.4f}")

    return w, b


w_final, b_final = train(x, y, w, b)

with open("weights.pkl", "wb") as f:
    pickle.dump((w_final, b_final), f)
