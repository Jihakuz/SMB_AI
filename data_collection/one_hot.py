"""Turns data from keylog.py into a one hot array for training data
"""

W = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
A = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
S = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
D = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
WJ = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
WK = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
AJ = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
AK = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
SJ = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
SK = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
DJ = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
DK = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
J = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
K = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]


def keys_to_one_hot(keys):
    """Turns key data into one hot data (defined above)

    Args:
        keys: unproccessed key data from keylog.py

    Return:
        output: one hot version of keys being pressed
    """
    # [W,A,S,D,J,K]

    output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    if "W" in keys and "J" in keys:
        output = WJ

    elif "W" in keys and "K" in keys:
        output = WK

    elif "S" in keys and "J" in keys:
        output = SJ

    elif "S" in keys and "K" in keys:
        output = SK

    elif "A" in keys and "J" in keys:
        output = AJ

    elif "A" in keys and "K" in keys:
        output = AK

    elif "D" in keys and "J" in keys:
        output = DJ

    elif "D" in keys and "K" in keys:
        output = DK

    elif "W" in keys:
        output = W

    elif "A" in keys:
        output = A

    elif "S" in keys:
        output = S

    elif "J" in keys:
        output = J

    elif "K" in keys:
        output = K

    else:
        output = D

    return output
