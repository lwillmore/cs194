import numpy as np
import os
from scipy.ndimage import imread
import matplotlib.pyplot as plt


X_data = []
Y_data = []
imfile = open("../images/top4_image_list","r")

for line in imfile:
	[imname, label, diagnosis] = line.strip().split("\t")
	im = imread("../images/%s" % (imname))
	print im.shape
	X_data.append(im)
	Y_data.append(label)

mean_image = mean(X_data)
plt.imshow(mean_iamge)
plt.show()