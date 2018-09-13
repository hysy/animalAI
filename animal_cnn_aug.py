
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
import keras
import numpy as np


classes = ['monkey', 'boar', 'crow']
num_classes = len(classes)
image_size = 50


# define main function 

def main():
    X_train, X_test, Y_train, Y_test = np.load('./animal_aug.npy')
    X_train = X_train.astype('float') / 256
    X_test = X_test.astype('float') / 256
    Y_train = np_utils.to_categorical(Y_train, num_classes) # one-hot-vector 
    Y_test = np_utils.to_categorical(Y_test, num_classes) # one-hot-vector 

    for epoch in [1, 20, 50, 100]:
        Loss = Acc = 0.0 
        num = 5 # Num of Executions
        for index in range(num):
            model = model_train(X_train, Y_train, epoch, index)
            loss, acc = model_eval(model, X_test, Y_test)
            Loss += loss
            Acc  += acc
        Loss /= float(num)
        Acc /= float(num)

        o_fname = "./CNNLossAcc_aug/CNNLossAcc_aug_" + str(epoch) + ".txt"

        with open(o_fname, "w") as f:
            print("Loss: " + str(Loss), file=f)
            print("Acc: "  + str(Acc) , file=f)





def model_train(X, Y, epoch=30, index=0):
    model = Sequential()
# Convolutional Neural Network

## Hidden Layers (Get Feature value)
# #1 Conv, relu, Pooling
    model.add(Conv2D(32, (3,3), padding='same', input_shape=X.shape[1:]))
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

# 25 epoch -> 75%
# 50 epoch -> 79% ... 
    model.fit(X, Y, batch_size=32, epochs=epoch) 
# save model
# モデルがあまりに大きかったため、一つだけ保存する。
    if index == 0:
        model.save('./CNNLossAcc/animal_cnn_aug' + str(epoch) + '.h5')

# evaluation 
    return model

def model_eval(model, X, Y):
    scores = model.evaluate(X, Y, verbose=1) # vervose途中結果表示
    print('Test Loss: ', scores[0])
    print('Test Accuracy: ', scores[1])
    return scores

if __name__ == "__main__":
    main()
