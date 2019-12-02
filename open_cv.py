import os
import PIL
import numpy
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

digits = []
labels = []
basewidth = 50
fig = plt.figure(figsize=(20, 20))
cnt = 0
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
for i in range(2, 10):
    for img in os.listdir('./{}/'.format(i)):
        pil_image = PIL.Image.open(
            './{}/{}'.format(i, img)).convert('1')

        wpercent = (basewidth/float(pil_image.size[0]))
        hsize = int((float(pil_image.size[1])*float(wpercent)))
        img = pil_image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)

        ax = fig.add_subplot(10, 16, cnt+1, xticks=[], yticks=[])
        ax.imshow(img, cmap=plt.cm.binary, interpolation='nearest')

        ax.text(2, 9, str(i), color="red", fontsize=20)

        cnt = cnt + 1
        digits.append([pixel for pixel in iter(img.getdata())])
        labels.append(i)

digit_ary = numpy.array(digits)
print(digit_ary.shape)
scaler = StandardScaler()
scaler.fit(digit_ary)
x_scaled = scaler.transform(digit_ary)


mlp = MLPClassifier(hidden_layer_sizes=(30, 30, 30),
                    activation='logistic', max_iter=3000)
print(mlp.fit(x_scaled, labels))

predicted = mlp.predict(x_scaled)
print(predicted)
target = numpy.array(labels)
print(predicted == target)

# 預測

data = []
basewidth = 50
fig = plt.figure(figsize=(20, 20))
cnt = 0
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
for idx, img in enumerate(os.listdir('./prediction/')):
    pil_image = PIL.Image.open(
        './prediction/{}'.format(img)).convert('1')

    wpercent = (basewidth/float(pil_image.size[0]))
    hsize = int((float(pil_image.size[1])*float(wpercent)))
    img = pil_image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    data.append([pixel for pixel in iter(img.getdata())])


scaler = StandardScaler()
scaler.fit(data)
data_scaled = scaler.transform(data)
print(mlp.predict(data_scaled))
