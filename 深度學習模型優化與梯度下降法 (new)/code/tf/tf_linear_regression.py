import numpy as np # conda install numpy
import tensorflow as tf

# y_pred = W*X + b
W = tf.Variable(0.0)
b = tf.Variable(0.0)

def loss(y, y_pred):
    return tf.reduce_mean(tf.square(y - y_pred))

def predict(X):
    return W * X + b
#     return W @ X + b

def train(X, y, epochs=40, lr=0.0001):
    current_loss=0
    for epoch in range(epochs):
        with tf.GradientTape() as t:
            t.watch(tf.constant(X))
            current_loss = loss(y, predict(X))

        dW, db = t.gradient(current_loss, [W, b])
        W.assign_sub(lr * dW) # W -= lr * dW
        b.assign_sub(lr * db)

        print(f'Epoch {epoch}: Loss: {current_loss.numpy()}') # <3 eager execution
        print(f'    W: {W.numpy()}, b: {b.numpy()}')

# Dataset 1
# random linear data: 100 between 0-50 i.e. [0, 50]
n = 100
X = np.linspace(0, 50, n) 
y = np.linspace(0, 50, n) 
# print(X)

# Adding noise to the random linear data
np.random.seed(1234)
X += np.random.uniform(-10, 10, n)
y += np.random.uniform(-10, 10, n) 

# reset W,b
W = tf.Variable(0.0)
b = tf.Variable(0.0)

# train(X, y)
train(X, y, epochs=100, lr=0.00005) # Dataset 1: X數值較大，因此lr不能太大!
