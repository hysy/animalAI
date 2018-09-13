from PIL import Image
import os, glob
import numpy as np 
# from sklearn import cross_validation
from sklearn import model_selection

classes = ['monkey', 'boar', 'crow']
num_classes = len(classes)
image_size = 50

X = []  # image matrix
Y = []  # index

for index, class_name in enumerate(classes):
    photos_dir = './' + class_name
    files = glob.glob(photos_dir + '/*.jpg')
    for i, file in enumerate(files):
        if i >= 200: break
        image = Image.open(file)
        image = image.convert('RGB') ## convert to RGB
        image = image.resize((image_size, image_size))
        data = np.asarray(image)

        X.append(data)
        Y.append(index)
                
X = np.array(X)
Y = np.array(Y)
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, Y_train, Y_test) 
np.save('./animal.npy', xy)
