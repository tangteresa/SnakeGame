import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):

    # constructor
    def __init__(self, screenWidth, screenHeight, squareSize, stepsUntilAction, currentStep):
        super(Player, self).__init__()

        # set player size
        self.squareSize = squareSize
        self.surf = pygame.Surface((self.squareSize, self.squareSize))

        # color player
        self.surf.fill((252, 63, 63))
        self.rect = self.surf.get_rect()

        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.step = currentStep
        self.stepsUntilMove = stepsUntilAction

        # states are 0 for right, 90 for up, 180 for left, and 270 for down
        self.state = 270

        self.firstKeyPress = True

    def checkState(self):
        if self.state == 270:
            if self.step % self.stepsUntilMove == 0:
                self.rect.move_ip(0, self.squareSize)

        elif self.state == 0:
            if self.step % self.stepsUntilMove == 0:
                self.rect.move_ip(self.squareSize, 0)

        elif self.state == 90:
            if self.step % self.stepsUntilMove == 0:
                self.rect.move_ip(0, -self.squareSize)

        elif self.state == 180:
            if self.step % self.stepsUntilMove == 0:
                self.rect.move_ip(-self.squareSize, 0)
        """if self.state == 270:
            if self.step % self.stepsUntilMove == 0:
                self.rect.move_ip(0, self.squareSize)

        elif self.state == 0:
            if self.step % self.stepsUntilMove == 0:
                self.rect.move_ip(self.squareSize, 0)

        elif self.state == 90:
            if self.step % self.stepsUntilMove == 0:
                self.rect.move_ip(0, -self.squareSize)

        elif self.state == 180:
            if self.step % self.stepsUntilMove == 0:
                self.rect.move_ip(-self.squareSize, 0)"""

    def changeState(self, pressed_keys, statesList):
        if pressed_keys[K_UP]:
            newState = 90

            if self.state != newState:
                self.saveNewState(newState, statesList)

        elif pressed_keys[K_DOWN]:
            newState = 270

            if self.state != newState:
                self.saveNewState(newState, statesList)

        elif pressed_keys[K_LEFT]:
            newState = 180

            if self.state != newState:
                self.saveNewState(newState, statesList)

        elif pressed_keys[K_RIGHT]:
            newState = 0

            if self.state != newState:
                self.saveNewState(newState, statesList)


    def saveNewState(self, newState, statesList):
        if self.step % self.stepsUntilMove == 0 and abs(self.state - newState) != 180:
            statesList.addState(self.firstKeyPress, self.rect.left, self.rect.top, newState)
            self.state = newState
            self.firstKeyPress = False

    def update(self, pressed_keys, statesList):
        # player dies when offscreen
        self.offScreen()

        # determine if key has been pressed and change state accordingly
        self.changeState(pressed_keys, statesList)

        # check what direction player should be moving
        self.checkState()

        # determine if key has been pressed and change state accordingly
        self.changeState(pressed_keys, statesList)

        self.step = self.step + 1

    def snackCollision(self, snack):
        return self.rect.colliderect(snack.rect)

    def selfCollision(self, tailSegmentsList):
        for segment in tailSegmentsList:
            if self.rect.colliderect(segment.rect):
                return True
        return False

    """Player dies if the edge of the screen is hit"""
    def offScreen(self):
        if self.rect.left < 0 and self.state == 180:
            pygame.display.quit()
            pygame.quit()
        elif self.rect.right > self.screenWidth and self.state == 0:
            pygame.display.quit()
            pygame.quit()
        if self.rect.top < 0 and self.state == 90:
            pygame.display.quit()
            pygame.quit()
        elif self.rect.bottom > self.screenHeight and self.state == 270:
            pygame.display.quit()
            pygame.quit()

