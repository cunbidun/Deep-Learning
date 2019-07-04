import os
import cv2
import sys

def show_path(path):
    imgs = open(path, 'r').readlines()

    for img in imgs:
        img_path = img.strip().split(' ')[0]
        img = cv2.imread(img_path)

        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    show_dir(sys.argv[1])
