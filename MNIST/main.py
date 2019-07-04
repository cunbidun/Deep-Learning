import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import caffe
import cv2
import lmdb
caffe.set_device(0)
caffe.set_mode_gpu()

def train(solver_prototxt_filename):
    solver = caffe.get_solver(solver_prototxt_filename)
    solver.solve()


net = caffe.Net("layer.prototxt",caffe.TEST)
train("solver.prototxt")
net.save("test.caffemodel")