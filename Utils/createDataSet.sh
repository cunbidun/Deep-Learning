#!/bin/bash 
DATA_PATH = 
SIZE = 
~$ GLOG_logtostderr=1 
/home/cunbidun/caffe/build/tools/convert_imageset \
    --resize_height=$SIZE --resize_width=$SIZE --shuffle --backend lmdb  \
    $DATA_PATH + "/trainImg/" \
    $DATA_PATH + "/train.txt" \
    $DATA_PATH + "/train_lmdb/"


~$ GLOG_logtostderr=1 
/home/cunbidun/caffe/build/tools/convert_imageset \
    --resize_height=$SIZE --resize_width=$SIZE --shuffle --backend lmdb  \
    $DATA_PATH + "/testImg/" \
    $DATA_PATH + "/test.txt" \
    $DATA_PATH + "/test_lmdb/"