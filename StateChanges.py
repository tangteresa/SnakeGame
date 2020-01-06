import pygame
import numpy as np

class StateChanges():

    # constructor
    def __init__(self):
        self.stateChangesList = np.empty((1,3))

    """Adds a state to the list of state changes when keys pressed"""
    def addState(self, firstKeyPress, x, y, state):
        if firstKeyPress:
            self.stateChangesList[0] = [x, y, state]
            print("FIRST KEY PRESS!")
            print(self.stateChangesList)
        else:
            self.stateChangesList = np.append(self.stateChangesList, [[x, y, state]], axis=0)
            print("NUP NUP NUP")
            print(self.stateChangesList)
            print(self.stateChangesList.shape[0])

    """Deletes the state of interest when the tail end of the snake has left location"""
    def deleteState(self, row):
        self.stateChangesList = np.delete(self.stateChangesList, row, 0)