import numpy as np
from random import randint as r
import random
n = 8
reward = np.zeros((n, n))
terminals = []
scrx = n * 100


def getMaze1Rewards():
    reward[0, 1] = -1
    reward[0, 2] = -10
    reward[0, 3] = -10
    reward[0, 4] = -10
    reward[0, 5] = -10
    reward[0, 7] = -10
    reward[1, 1] = -10
    reward[1, 5] = -10
    reward[1, 7] = -10
    reward[2, 3] = -10
    reward[3, 0] = -10
    reward[3, 1] = -10
    reward[3, 2] = -10
    reward[3, 3] = -10
    reward[3, 4] = -10
    reward[3, 6] = -10
    reward[3, 7] = -10
    reward[4, 3] = -10
    reward[5, 1] = -10
    reward[5, 3] = -10
    reward[5, 5] = -10
    reward[5, 6] = -10
    reward[5, 7] = -10
    reward[7, 0] = -10
    reward[7, 1] = -10
    reward[7, 3] = -10
    reward[7, 4] = -10
    reward[7, 6] = -10
    reward[7, 7] = 10
    return reward

def getMaze1Terminals():
    terminals.append(n * 0 + 1)
    terminals.append(n * 0 + 2)
    terminals.append(n * 0 + 3)
    terminals.append(n * 0 + 4)
    terminals.append(n * 0 + 5)
    terminals.append(n * 0 + 7)
    terminals.append(n * 1 + 1)
    terminals.append(n * 1 + 5)
    terminals.append(n * 1 + 7)
    terminals.append(n * 2 + 3)
    terminals.append(n * 3 + 0)
    terminals.append(n * 3 + 1)
    terminals.append(n * 3 + 2)
    terminals.append(n * 3 + 3)
    terminals.append(n * 3 + 4)
    terminals.append(n * 3 + 6)
    terminals.append(n * 3 + 7)
    terminals.append(n * 4 + 3)
    terminals.append(n * 5 + 1)
    terminals.append(n * 5 + 3)
    terminals.append(n * 5 + 5)
    terminals.append(n * 5 + 6)
    terminals.append(n * 5 + 7)
    terminals.append(n * 7 + 0)
    terminals.append(n * 7 + 1)
    terminals.append(n * 7 + 3)
    terminals.append(n * 7 + 4)
    terminals.append(n * 7 + 6)
    return terminals
