import numpy as np
from scipy.misc import imsave
from data_utils import load_tiny_imagenet

class_names, X_train, y_train, X_val, y_val, X_test, y_test = load_tiny_imagenet("tiny-imagenet-200")

from tsne import bh_sne
X = np.asarray(np.vstack((X_train, X_val, X_test)), dtype=np.float64).reshape(120000, 3*64*64)
X_2d = bh_sne(X)

# Zero-mean the data
mean_img = np.mean(X_train, axis=0)
X_train -= mean_img
X_val -= mean_img
X_test -= mean_img

with open("y_train.txt", "w") as f:
  for i in xrange(X_train.shape[0]):
    file_name = "train_%i.jpeg" % (i)
    imsave("train_flat/" + file_name, X_train[i,:,:,:])
    f.write("%s %s\n" % (file_name, y_train[i]))
    
with open("y_val.txt", "w") as f:
  for i in xrange(X_val.shape[0]):
    file_name = "val_%i.jpeg" % (i)
    imsave("val_flat/" + file_name, X_val[i,:,:,:])
    f.write("%s %s\n" % (file_name, y_val[i]))
    
for i in xrange(X_test.shape[0]):
  file_name = "test_%i.jpeg" % (i)
  imsave("test_flat/" + file_name, X_test[i,:,:,:])





