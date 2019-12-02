import os
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./code.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thessh = cv2.threshold(gray, 127, 255, 0)
x = np.array(thessh)

x[x < 100] = 250
x[x >= 255] = 0
x[x >= 250] = 255

contours, hierarchy = cv2.findContours(
    x, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cnts = sorted([(c, cv2.boundingRect(c)[0])
               for c in contours], key=lambda x: x[1])
ary = []
for (c, _) in cnts:
    (x, y, w, h) = cv2.boundingRect(c)
    if w > 10 and h >= 17:
        ary.append((x, y, w, h))
for id, (x, y, w, h) in enumerate(ary):
    fig = plt.figure()
    roi = img[y:y+h, x:x+w]
    thresh = roi.copy()
    a = fig.add_subplot(1, len(ary), id+1)
    plt.imshow(thresh)
    plt.savefig('{}.jpg'.format(id+82), dpi=100)
