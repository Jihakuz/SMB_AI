"""Gets an accurate value for the number of data points, however is very slow
os: sees if files exist in this path
numpy: load training data files
"""
import os
import numpy as np


def datacount():
    """Returns exact number of data points saved.
    """
    file_number = 0
    tdp = 0

    while True:
        file_name = f"training_data_{file_number}.npy"

        if os.path.isfile(file_name):
            file = np.load(file_name)

            tdp += len(file)

            print(f"""
There are {len(file)} data points in {file_name}.\nCurrently there are {tdp} total data points. That is {tdp/1000}%!\n
    """)

            del file

        else:
            print("Finished file counting.")
            break

        file_number += 1

    return (file_name, file_number, tdp)

# ===================================================================================================
# ===================================================================================================
# ===================================================================================================


def roughdatapoints():
    """Finds latest training_data file

    Returns:
        file_name: where the training_data should next be saved,
        file_name: the number of file that is going to be saved next,
        tdp: a rough guess of total data points,
             use data_points_counter.py for an accurate answer (slow).
    """
    # starting at file 0
    file_number = 0

    while True:
        # set a file_name to be searched for
        file_name = f"training_data_{file_number}.npy"

        if os.path.isfile(file_name):
            # if the file exists, then a new file_name is created.
            print(f'File {file_number} exists, moving to next file.')
            file_number += 1
        else:
            # if it can't find the file, then it starts there.
            # could impliment a way to check how big it is then using that file,
            # but this is okay for the moment.
            print(f"Found last file, making new file at {file_number}.")
            total_data_points = 4000 * file_number
            print(f"You have roughly {total_data_points} data points so far.")
            return (file_name, file_number, total_data_points)

        if file_number == 1000:
            # doubt I will ever make more than 1000 files.
            print("Assuming there is no new file, starting fresh!")
            file_number = 0
            file_name = f"training_data_{file_number}.npy"
            return (file_name, file_number, total_data_points)

if __name__ == "__main__":
    if int(input("Type 1 for accurate.\nType 2 for rough.\n")) == 1:
        print(datacount())
    else:
        print(roughdatapoints())
