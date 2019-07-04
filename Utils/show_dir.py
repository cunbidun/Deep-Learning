import os
import cv2
import sys

def show_dir(dir):
    imgs = os.listdir(dir)

    for img in imgs:
        img = cv2.imread(dir + img)
        
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    show_dir(sys.argv[1])
