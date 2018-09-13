from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
import keras, sys
from PIL import Image
import numpy as np 


classes = ['monkey', 'boar', 'crow']
num_classes = len(classes)
image_size = 50

def build_model(epoch=1):
    model = Sequential()
# Convolutional Neural Network

## Hidden Layers (Get Feature value)
# #1 Conv, relu, Pooling
    model.add(Conv2D(32, (3,3), padding='same', input_shape=(50, 50, 3)))
    model.add(Activation('relu'))
    model.add(Conv2D(32, (3,3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
# #2 Conv, relu, Pooling
    model.add(Conv2D(64,(3,3), padding='same'))
    model.add(Activation('relu'))
    model.add(Conv2D(64,(3,3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

## [Classifier by Feature value] Flatten, Dense, Softmax
    model.add(Flatten())
    model.add(Dense(512)) # Fully Connect
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(3))
    model.add(Activation('softmax'))

    
    opt = keras.optimizers.rmsprop(lr=0.0001, decay=1e-6)
    model.compile(
        loss='categorical_crossentropy',
        optimizer=opt, metrics=['accuracy']
    )

    model = load_model('./CNNLossAcc/animal_cnn' + str(epoch) +'.h5')

##### モデルがあまりに大きかったため、一つだけ保存する。
#    if index == 0:
#        model.save('./CNNLossAcc/animal_cnn' + str(epoch) + '.h5')

# evaluation 
    return model

def main():
    image = Image.open(sys.argv[1])
    image = image.convert('RGB')
    image = image.resize((image_size, image_size))
    data = np.asarray(image)
    X = []
    X.append(data)
    X = np.array(X)
    model = build_model()

    result = model.predict([X])[0]
    predicted = result.argmax()

    percentage = int(result[predicted] * 100)

    print("{0} ({1} % )".format(classes[predicted], percentage))

if __name__ == "__main__":
    main()

