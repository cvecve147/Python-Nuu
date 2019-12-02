from sklearn.preprocessing import StandardScaler
import cv2
import time
from datetime import datetime
from matplotlib import pyplot as plt
import numpy
import os
import PIL
import requests
from PIL import Image
import joblib
clf = joblib.load('captcha.pkl')

basewidth = 50


def saveKaptcha():
    img = cv2.imread('./code.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thessh = cv2.threshold(gray, 127, 255, 0)
    x = numpy.array(thessh)

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
        plt.savefig('./imagedata/'+'{}.jpg'.format(id), dpi=100)


def predictKaptcha(dest):
    data = []
    for img in range(0, 4):
        pil_image = PIL.Image.open(os.path.join(
            dest, '{}.jpg'.format(img))).convert('1')
        wpercent = (basewidth/float(pil_image.size[0]))
        hsize = int((float(pil_image.size[1])*float(wpercent)))
        img = pil_image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        data.append([pixel for pixel in iter(img.getdata())])
    scaler = StandardScaler()
    scaler.fit(data)
    data_scaled = scaler.transform(data)
    return clf.predict(data_scaled)


if __name__ == '__main__':
    saveKaptcha()
    print(predictKaptcha('./imagedata'))
