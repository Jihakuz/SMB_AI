import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten

Xs = np.load(r"Xs/X_0.npy")

split_Xs = int(len(Xs) * 0.8)

X_train = Xs[:split_Xs]
X_test = Xs[split_Xs:]


print(f"""
Xs length: {len(Xs)},
Xs_train length: {len(X_train)},
Xs_test: {len(X_test)}.
""")

model = Sequential()

model.Add(Conv2D(64, kernel_size=3, activation="relu", input_shape=(515, 590, 3)))
model.Add(Conv2D(32, kernel_size=3, activation="relu"))
model.Add(Flatten())
model.Add(Dense(10, activation="softmax"))

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
