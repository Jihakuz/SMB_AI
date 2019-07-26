"""Main function that bring together keylog.py and screen_grab.py
time: how long program has been running and time to save
os: finds if latest training data file
numpy: holds and saves training_data

data_points_counter: exact number of data points or a rough guess
keylog: gets currently pressed keys
screen_grab: gets proccessed screenshot of game
"""
import time
import numpy as np

from data_points_counter import datacount, roughdatapoints
from keylog import key_check
from screen_grab import screen_record
from one_hot import keys_to_one_hot


def main(show_preview=False, acc_tdp=False):
    """Main method that controls collecting and saving of data

    Args:
        name: name of the file that needs to saved next,
        number: file number of the file being saved,
        tdp: total data points (at the moment this is extremly rough guess),
        show_preview: if a window should be shown with the image being captured.
    """

    if acc_tdp is True:
        file_name, file_number, total_data_points = datacount()
    else:
        file_name, file_number, total_data_points = roughdatapoints()

    training_data = []

    for i in range(4, 0, -1):
        print(i + 1)
        time.sleep(1)

    print("Starting...")

    while True:
        screen = screen_record(show_preview)
        keys = key_check()

        output = keys_to_one_hot(keys)

        # print (f"Keys: {keys}\nOutput: {output}")

        training_data.append([screen, output])

        if len(training_data) % 500 == 0:
            try:
                print(f"""
It took {round((time.time() - TIMESTART), 0)} to collect {len(training_data)} bits of data for this file.
""")
                total_data_points += 500
                print(f"""
You roughly have {total_data_points} total data points.\nSaving in file: {file_name}.
""")
                save_start = time.time()
                print("\nDO NOT EXIT YET!\n")
                np.save(file_name, training_data)
                print(f"Saved in {round((time.time() - save_start), 0)} seconds!\n\n")
            except MemoryError:
                print("""
Failed to save file due to a memory error. Creating new file.\nRetrying save...
""")

                # creating temp storage for extra values
                to_save = training_data[(len(training_data) - 500):]
                training_data = training_data[:(len(training_data) - 500)]

                # resaving "safe" amount of data
                np.save(file_name, training_data)

                # increasing file name number by one
                file_number += 1
                file_name = f"training_data_{file_number}.npy"
                # making training_data now store the temp values
                training_data = to_save
                # deleting to_save to save space
                del to_save
                # saving to a new file
                np.save(file_name, training_data)

                print("Finished creating new training data file.\n\n")

if __name__ == "__main__":
    TIMESTART = time.time()
    main()

# ~5000 points per file
