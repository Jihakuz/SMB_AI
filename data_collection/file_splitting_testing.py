import numpy as np
import os

file_number = 0
training_data = []

while True:
    file_name = f"training_data_testing_{file_number}.npy"

    if os.path.isfile(file_name):
        print(f'File {file_number} exists, moving to next file.')
        file_number += 1
    else:
        print(f"Found last file, making new file at {file_number}.")
        break

    if file_number == 1000:
        print("Assuming there is no new file, starting fresh!")
        break

np.save(file_name, training_data)
