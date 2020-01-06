import pygame
import Player
import numpy as np
from pygame.locals import *

class Tail(Player.Player):

    # constructor
    def __init__(self, head, screenWidth, screenHeight, squareSize, stepsUntilAction, currentStep):
        Player.Player.__init__(self, screenWidth, screenHeight, squareSize, stepsUntilAction, currentStep)
        self.head = head

        # set size
        self.squareSize = head.squareSize
        self.surf = pygame.Surface((self.squareSize, self.squareSize))

        # color fill
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

        self.findStart(head.state)

        # begins moving in same direction as gamer
        self.state = head.state

        self.step = currentStep
        self.stepsUntilMove = stepsUntilAction

        self.isLast = True

    def findStart(self, direction):
        if direction == 0:
            self.rect.left = self.head.rect.left - self.squareSize
            self.rect.top = self.head.rect.top

        elif direction == 90:
            self.rect.left = self.head.rect.left
            self.rect.top = self.head.rect.top + self.squareSize

        elif direction == 180:
            self.rect.left = self.head.rect.left + self.squareSize
            self.rect.top = self.head.rect.top

        elif direction == 270:
            self.rect.left = self.head.rect.left
            self.rect.top = self.head.rect.top - self.squareSize

    """Parse through statesList to determine if current location matches a location at which snake head's state was changed"""
    def changeState(self, statesList):
        row = 0
        while row < statesList.stateChangesList.shape[0]:
            if statesList.stateChangesList[row, 0] == self.rect.left and statesList.stateChangesList[row, 1] == self.rect.top:
                self.state = statesList.stateChangesList[row, 2]

                # if this is the last part of the snake, the location of change is deleted
                if self.isLast:
                    statesList.deleteState(row)

            row = row + 1

    def update(self, statesList):
        self.changeState(statesList)
        self.checkState()
        self.changeState(statesList)
        self.offScreen()
        self.step = self.step + 1

    def notIsLast(self):
        self.isLast = False