import numpy as np
import os

for filename in os.listdir(r"E:\\Files\\Code\\EPQ\\EPQ 2.0\\1code\\training_data"):
    file = np.load(f"E:\\Files\\Code\\EPQ\\EPQ 2.0\\1code\\training_data\\{filename}")

    Xs = []
    ys = []

    for datapoint in file:
        Xs.append(datapoint[0])
        ys.append(datapoint[1])

    np.save(f"E:\\Files\\Code\\EPQ\\EPQ 2.0\\1code\\Xs\\X_{filename[14:]}", Xs)
    np.save(f"E:\\Files\\Code\\EPQ\\EPQ 2.0\\1code\\ys\\y_{filename[14:]}", ys)
