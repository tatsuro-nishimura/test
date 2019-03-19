from sklearn import datasets
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers import Dropout
from keras.utils import np_utils
from sklearn import preprocessing
import numpy as np

def get_mlp():
    model = Sequential()
    model.add(Dense(10, input_shape=(4, )))
    model.add(Activation('relu'))
    model.add(Dropout(0.25))
    model.add(Dense(6))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(3))
    model.add(Activation('softmax'))
    return model

def main():
    iris = datasets.load_iris()

    X = preprocessing.scale(iris.data)
    Y = np_utils.to_categorical(iris.target)
    train_X, test_X, train_Y, test_Y = train_test_split(X, Y, train_size=.7)

    model = get_mlp()
    model.compile(optimizer='SGD', loss='categorical_crossentropy',
        metrics=['accuracy'])
    model.fit(train_X, train_Y, nb_epoch=100, batch_size=1, verbose=1)

    result = 1*(np.argmax(Y, axis=1) == np.argmax(model.predict(X), axis=1))
    print('result')
    print(result)
    print(len(result))
    print(np.sum(result))
    print(np.mean(result))

if __name__ == "__main__":
    main()
