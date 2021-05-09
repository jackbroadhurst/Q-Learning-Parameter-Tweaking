import pandas
from mazes import *
from time import time,sleep
from numpy import savetxt
from random import randint as r
import random

terms = getMaze1Terminals()
rews = getMaze1Rewards()
AList = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
GList = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]


def select_action(current_state):
    global current_position, epsilon
    possible_actions = []
    if np.random.uniform(0, 1) <= epsilon:  # exploration
        global ModeFlag
        if current_position[0] != 0:
            possible_actions.append("up")
        if current_position[0] != n - 1:
            possible_actions.append("down")
        if current_position[1] != 0:
            possible_actions.append("left")
        if current_position[1] != n - 1:
            possible_actions.append("right")
        action = actions[possible_actions[r(0, len(possible_actions) - 1)]]
        ModeFlag = True
    else:  # Use Q table
        minQ = np.min(Q[current_state])
        if current_position[0] != 0:  # up
            possible_actions.append(Q[current_state, 0])
        else:
            possible_actions.append(minQ - 100)
        if current_position[0] != n - 1:  # down
            possible_actions.append(Q[current_state, 1])
        else:
            possible_actions.append(minQ - 100)
        if current_position[1] != 0:  # left
            possible_actions.append(Q[current_state, 2])
        else:
            possible_actions.append(minQ - 100)
        if current_position[1] != n - 1:  # right
            possible_actions.append(Q[current_state, 3])
        else:
            possible_actions.append(minQ - 100)
        action = random.choice([i for i, a in enumerate(possible_actions) if a == max(
            possible_actions)])
        ModeFlag = False
    return action

def epoch(terminals, reward):
    global current_position, epsilon, its, wins, steps, step, last_position, ouches
    current_state = states[(current_position[0], current_position[1])]
    action = select_action(current_state)
    if action == 0:  # move up
        current_position[0] -= 1
    elif action == 1:  # move down
        current_position[0] += 1
    elif action == 2:  # move left
        current_position[1] -= 1
    elif action == 3:  # move right
        current_position[1] += 1
    new_state = states[(current_position[0], current_position[1])]
    if new_state not in terminals:
        Q[current_state, action] += alpha * (
                    reward[current_position[0], current_position[1]] + gamma * (np.max(Q[new_state])) - Q[
                current_state, action])
        step += 1
        if current_position == [7, 7]:
            wins += 1
            updateStacks()
            its += 1
            step = 0
            ouches = 0
            current_position = [0, 0]
    else:
        Q[current_state, action] += alpha * (
                    reward[current_position[0], current_position[1]] + gamma * (np.max(Q[new_state])) - Q[
                current_state, action])
        step += 1
        ouches += 1

def updateStacks():
    outMoves.append(place)
    outSteps.append(step)
    outIts.append(its)
    outWins.append(wins)
    outOuches.append(ouches)
    outTest.append(test)

for A in range(0, 10, 1):
    alpha = AList[A]
    Apath = str(A+1)
    for G in range(0, 10, 1):
        gamma = GList[G]
        Gpath = str(G+1)
        for test in range (0,10,1):
            strtest = str(test)
            epochs = 0
            step = 0
            its = 0
            wins = 0
            ouches = 0
            state = 0
            steps = np.zeros((2,1))
            outTest = []
            outSteps = []
            outIts = []
            outMoves = []
            outWins = []
            outOuches = []
            outState = []

            Q = np.zeros((n ** 2, 4))
            actions = {"up": 0, "down": 1, "left": 2, "right": 3}
            states = {}

            k = 0
            for i in range(n):
                for j in range(n):
                    states[(i, j)] = k
                    k += 1

            epsilon = 0
            current_position = [0, 0]

            run = True
            while run:
                epoch(terms, rews)
                place = states[(current_position[0], current_position[1])]
                epochs += 1
                print(test, "  ",epochs, "  ", wins)
                if wins == 40:
                    run = False
            print(Q)
            # Qpath = 'C:/Users/Jack/PycharmProjects/QGame/PROPERPARAMETERTWEAKDATA/Q/' + "A" + Apath + "G" + Gpath + "_" + strtest + ".csv"
            # np.savetxt(Qpath, Q, delimiter=',')
            path = 'C:/Users/Jack/PycharmProjects/QGame/PROPERPARAMETERTWEAKDATA/FullFile.csv'
            data = pandas.DataFrame({"Alpha": alpha, "Gamma": gamma, "Test": outTest, "Ouches": outOuches, "Wins": outWins, "Steps": outSteps, "Move": outMoves})
            data.to_csv(path, mode='a')