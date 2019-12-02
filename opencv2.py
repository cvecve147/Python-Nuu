
from sklearn.externals import joblib
from sklearn.neural_network import MLPClassifier
import numpy
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import os
import PIL
import numpy as np
digits = []
labels = []
basewidth = 50
cnt = 0

for i in range(0, 10):
    for img in os.listdir('./{}/'.format(i)):
        pil_image = PIL.Image.open(
            './{}/{}'.format(i, img)).convert('1')

        wpercent = (basewidth/float(pil_image.size[0]))
        hsize = int((float(pil_image.size[1])*float(wpercent)))
        img = pil_image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)

        cnt = cnt + 1
        digits.append([pixel for pixel in iter(img.getdata())])
        labels.append(i)
digit_ary = numpy.array(digits)

scaler = StandardScaler()
scaler.fit(digit_ary)
X_scaled = scaler.transform(digit_ary)
mlp = MLPClassifier(hidden_layer_sizes=(30, 30, 30),
                    activation='logistic', max_iter=3000)
mlp.fit(X_scaled, labels)
joblib.dump(mlp, 'captcha.pkl')
