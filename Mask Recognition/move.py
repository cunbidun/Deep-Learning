import os
import sys
import shutil

FISRT_ITEM = 1
LAST_ITEM = 7141
COPY_DIR = './1/'
PASTE_DIR ='./NOMASK/'

cnt = FISRT_ITEM - 1

imgs = os.listdir(COPY_DIR)

for img in imgs:
    shutil.copy(COPY_DIR + img,PASTE_DIR + img)
    # cnt = cnt + 1
    # if(cnt == LAST_ITEM):
    #      break
