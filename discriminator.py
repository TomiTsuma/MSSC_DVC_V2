from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, LeakyReLU, ZeroPadding2D, Input,ReLU
from tensorflow.keras.optimizers import Adam
import numpy as np
from sklearn.metrics import classification_report

def patchGANDsc(image_shape):
    model = Sequential()
    model.add(Input(shape=image_shape))
    model.add(Conv2D(64,kernel_size=(4,4), strides=(2,2), padding='same', activation='relu'))
    model.add(Conv2D(64,kernel_size=(4,4), strides=(2,2), padding='same', activation='relu'))
    model.add(Conv2D(64,kernel_size=(4,4), strides=(2,2), padding='same', activation='relu'))
    model.add(ZeroPadding2D())
    model.add(Conv2D(512, kernel_size=(4,4), strides=(1,1), padding='valid'))
    model.add(ZeroPadding2D())
    model.add(Conv2D(1, kernel_size=(4,4), strides=(1,1), padding='valid', activation='sigmoid'))
    model.compile(loss='mse', optimizer=Adam(lr=0.0002, beta_1=0.5), loss_weights=[0.5])
    return model

def load_real_samples(filename, file):
    # load the dataset
    data = np.load(filename)
    print(filename)
    data = data[file]
    print("Done")
    return data
try:
    anime_dataset = load_real_samples('anime_arr.npz', 'arr_0')
    human_dataset = load_real_samples('human_arr.npz', 'arr_0')
except Exception as e:
    print(e)
    f= open("report.txt","w+")
    f.write(f"{e}")
    f.close()

print(np.shape(human_dataset))

X = np.append(human_dataset, anime_dataset)
human_target = np.zeros(len(human_dataset))
anime_target = np.ones(len(anime_dataset))
y = np.append(human_target,anime_target)

model = patchGANDsc(image_shape=np.shape(human_dataset[0]))

model.summary()


model.fit(X,y, epochs=30, batch_size=2, shuffle=True)

y_preds = model.predict(X)
report = (classification_report(y_preds,y))
f= open("report.txt","w+")
f.write(f"{report}")
f.close()