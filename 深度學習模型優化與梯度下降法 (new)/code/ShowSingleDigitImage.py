
# 載入 MNIST 資料庫的訓練資料，並自動分為『訓練組』及『測試組』
import os
import sys

if len(sys.argv) <= 1:
    print("需輸入參數 0~9")
    sys.exit()
#print(sys.argv[1])
    
if len(sys.argv[1].strip()) != 1:
    print("需輸入參數 0~9")
    sys.exit()
try: 
    no = int(sys.argv[1].strip())
except:
    print("需輸入參數 0~9")
    sys.exit()
    

from keras.datasets import mnist
# data_folder = os.path.join(os.getcwd(), "../datasets/mnist.npz")
(X_train, y_train), (X_test, y_test) = mnist.load_data()

import matplotlib.pyplot as plt

fig, ax = plt.subplots(nrows=2, ncols=5, sharex=True, sharey=True,)
ax = ax.flatten()
for i in range(10):
    # img = X_train[y_train == no][i].reshape(28, 28)
    img = X_train[y_train == no][i]
    
    # show pixels' value
    for j in range(28):
        pixels = ""
        for k in range(28):
            pixels += str(img[j,k]).zfill(3) + " "
        print(pixels)
    print("")

    # ax[i].imshow(img, cmap='Greys')
    ax[i].imshow(img, cmap=plt.get_cmap('gray'))

ax[0].set_xticks([])
ax[0].set_yticks([])
plt.tight_layout()
# plt.savefig('images/12_5.png', dpi=300)
plt.show()
