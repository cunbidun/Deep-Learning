import os
import sys
import shutil
import random

OR_MASK = './MASK/'
OR_NOMASK = './NOMASK/'

shutil.rmtree('./data/train/') 
shutil.rmtree('./data/val/')

os.mkdir('./data/train/')
os.mkdir('./data/train/no_mask/')
os.mkdir('./data/train/mask/')

os.mkdir('./data/val/')
os.mkdir('./data/val/no_mask/')
os.mkdir('./data/val/mask/')

TRAIN_MASK ='./data/train/mask/'
TRAIN_NOMASK ='./data/train/no_mask/'
VAL_MASK ='./data/val/mask/'
VAL_NOMASK ='./data/val/no_mask/'

imgs = os.listdir(OR_MASK)
random.shuffle(imgs) 


cnt = 0
for img in imgs:
    cnt = cnt + 1
    if cnt >= 5250:
        break
    if(cnt <= 1000):
        shutil.copy(OR_MASK + img,VAL_MASK + img)
    else:
        shutil.copy(OR_MASK + img,TRAIN_MASK + img)

imgs = os.listdir(OR_NOMASK)
random.shuffle(imgs) 


cnt = 0
for img in imgs:
    cnt = cnt + 1
    if cnt >= 9001:
        break
    if(cnt <= 1000):
        shutil.copy(OR_NOMASK + img,VAL_NOMASK + img)
    else:
        shutil.copy(OR_NOMASK + img,TRAIN_NOMASK + img)

