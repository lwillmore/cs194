import caffe
import numpy as np
import json

cs231n = "/home/ubuntu/cs231n"
with open(cs231n + '/tiny-imagenet-200/wnids.txt', 'r') as f:
  wnids = [x.strip() for x in f]
wnid_to_label = {wnid: i for i, wnid in enumerate(wnids)}

caffe.set_mode_gpu()
net = caffe.Classifier("/home/ubuntu/prelu/caffe/models/bvlc_reference_caffenet/deploy.prototxt", "/home/ubuntu/cs231n/nest_another_layer_iter_45000.caffemodel", channel_swap=(2,1,0),raw_scale=255, image_dims=(64,64))

images = []
for i in xrange(10000):
    images += [caffe.io.load_image(cs231n + "/test_flat/test_%s.jpeg" % (i))]

f = open("lucash.txt", "w")
probs = open("probs.txt", "w")
for i in xrange(4,5):
    prediction = net.predict([images[i]])
    cls = np.argmax(prediction[0])
    print("Image #%s is %s" % (i, wnids[cls]))
    f.write("test_%s.JPEG %s\n" % (i, wnids[cls]))
    probs.write("test_%s.JPEG %s\n" % (i, json.dumps(prediction[0].tolist())))
f.close()
probs.close()
