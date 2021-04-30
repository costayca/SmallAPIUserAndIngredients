from tensorflow.keras.preprocessing import image
from tensorflow.keras import layers

from tensorflow.keras.applications.nasnet import NASNetMobile

from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D

def init_model():
    base_model = NASNetMobile(include_top=False, input_shape=(224,224,3))

    model = Sequential()

    model.add(base_model)
    model.add(Flatten())
    model.add(Dense(37, activation="softmax"))

    model.layers[0].trainable = False

    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    model.load_weights('D:\\OneDrive\\Licenta\\SmallAPIUserAndIngredients\\resources\\save_model.hdf5')

    return model

model = init_model()