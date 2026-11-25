# PROGRAM
import numpy as np

np.random.seed(1)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

W1 = np.random.uniform(size=(2, 4))
b1 = np.zeros((1, 4))
W2 = np.random.uniform(size=(4, 1))
b2 = np.zeros((1, 1))
lr = 0.5

for epoch in range(10000):
    hidden = sigmoid(np.dot(X, W1) + b1)
    output = sigmoid(np.dot(hidden, W2) + b2)
    error = y - output
    d_output = error * sigmoid_derivative(output)
    d_hidden = d_output.dot(W2.T) * sigmoid_derivative(hidden)
    W2 += hidden.T.dot(d_output) * lr
    b2 += np.sum(d_output, axis=0, keepdims=True) * lr
    W1 += X.T.dot(d_hidden) * lr
    b1 += np.sum(d_hidden, axis=0, keepdims=True) * lr
    if epoch % 2000 == 0:
        print(f"Epoch {epoch}, Loss: {np.mean(np.square(error)):.6f}")

print("\nFinal predictions:")
for inp, out in zip(X, output):
    print(inp, "->", round(float(out[0]), 4), "=>", int(out[0] > 0.5))

# OUTPUT
# Epoch 0, Loss: 0.318067
# Epoch 2000, Loss: 0.005901
# Epoch 4000, Loss: 0.001162
# Epoch 6000, Loss: 0.000615
# Epoch 8000, Loss: 0.000412
#
# Final predictions:
# [0 0] -> 0.0196 => 0
# [0 1] -> 0.983 => 1
# [1 0] -> 0.9835 => 1
# [1 1] -> 0.017 => 0
