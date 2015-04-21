#!/usr/bin/env python

import numpy as np
import os, sys
from scipy.ndimage import imread
from scipy import misc
import matplotlib.pyplot as plt
import random


IMG_DIM = 143


def resize_img(im):
	im = im[((im.shape[0]-IMG_DIM)/2):(IMG_DIM+(im.shape[0]-IMG_DIM)/2), \
			((im.shape[1]-IMG_DIM)/2):(IMG_DIM+(im.shape[1]-IMG_DIM)/2)]
	return im


def split_data(dat_size):
	train = []
	val = []
	test = []
	for i in range(dat_size):
		r = random.random()
		if r < 0.6:
			train.append(i)
		elif r < 0.8:
			val.append(i)
		else:
			test.append(i)
	return train, val, test


def main ():
	X_data = []
	Y_data = []
	imfile = open("../images/top4_image_list","r")
	lengths = []

	for line in imfile:
		[imname, label, diagnosis] = line.strip().split("\t")
		im = resize_img(imread("../images/%s" % (imname)))
		print im.shape, imname, label
		X_data.append(im)
		Y_data.append(label)
		lengths.append(im.shape[1])

	train, val, test = split_data(len(Y_data))
	mean_img = np.mean([X_data[i] for i in train],axis=0)
	misc.imsave("tmp.png", mean_img)

	X_train = [X_data[i] for i in train] - mean_img
	X_val = [X_data[i] for i in val] - mean_img
	X_test = [X_data[i] for i in test] - mean_img
	y_train = [Y_data[i] for i in train]
	y_val = [Y_data[i] for i in val]
	y_test = [Y_data[i] for i in test]
	

	with open("y_train_full.txt", "w") as f:
	  for i in xrange(X_train.shape[0]):
	    file_name = "train_%i.jpeg" % (i)
	    misc.imsave("/afs/ir/users/l/i/linzwill/Documents/cs194/scripts/train/" + file_name, X_train[i])#,:,:,:])
	    f.write("%s %s\n" % (file_name, y_train[i]))
	    
	with open("y_val_full.txt", "w") as f:
	  for i in xrange(X_val.shape[0]):
	    file_name = "val_%i.jpeg" % (i)
	    misc.imsave("/afs/ir/users/l/i/linzwill/Documents/cs194/scripts/val/" + file_name, X_val[i])#:,:,:])
	    f.write("%s %s\n" % (file_name, y_val[i]))

	with open("_____y_test_full.txt", "w") as f:
		for i in xrange(X_test.shape[0]):
		  file_name = "test_%i.jpeg" % (i)
		  misc.imsave("/afs/ir/users/l/i/linzwill/Documents/cs194/scripts/test/" + file_name, X_test[i])#,:,:,:])
	

if __name__ == '__main__':
	main()
