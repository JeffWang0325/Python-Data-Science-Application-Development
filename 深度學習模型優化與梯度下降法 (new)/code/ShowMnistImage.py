
# 載入 MNIST 資料庫的訓練資料，並自動分為『訓練組』及『測試組』
import os
from keras.datasets import mnist
#data_folder = os.path.join(os.getcwd(), "datasets/mnist.npz")
(X_train, y_train), (X_test, y_test) = mnist.load_data() #path=data_folder)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(nrows=2, ncols=5, sharex=True, sharey=True,)

# Method 1
# ax = ax.flatten()
# for i in range(10):
#     # img = X_train[y_train == i][0].reshape(28, 28)
#     img = X_train[y_train == i][0]
#     # ax[i].imshow(img, cmap='Greys')
#     ax[i].imshow(img, cmap=plt.get_cmap('gray'))

# Method 2
for j in range(2):
    for i in range(5):
        img = X_train[y_train == i + 5 * j][0]
        ax[j, i].imshow(img, cmap=plt.get_cmap('gray'))

# ax[0].set_xticks([])
# ax[0].set_yticks([])
plt.tight_layout()
# plt.savefig('images/12_5.png', dpi=300)
plt.show()
