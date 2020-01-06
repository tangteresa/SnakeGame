import pygame
import random

class Snack(pygame.sprite.Sprite):
    def __init__(self, screenWidth, screenHeight, squareSize):
        super(Snack, self).__init__()
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.squareSize = squareSize

        #self.surf.fill(0, 0, 0)
        self.surf = pygame.Surface((self.squareSize, self.squareSize))
        self.rect = self.surf.get_rect()

        self.radius = self.squareSize//2
        x = random.randint(0, (int(self.screenWidth / self.squareSize) - 1))
        y = random.randint(0, (int(self.screenHeight / self.squareSize) - 1))

        self.rect.left = x*(self.squareSize)
        self.rect.top = y*(self.squareSize)

        self.numMoves = 1

    def moveSnack(self):
        self.rect.left = (self.squareSize) * (random.randint(0, (int(self.screenWidth/self.squareSize)) - 1))
        print("X IS:" + str(self.rect.left))
        self.rect.top = (self.squareSize) * (random.randint(0, (int(self.screenWidth/self.squareSize)) - 1))
        print("Y IS:" + str(self.rect.top))

        self.numMoves = self.numMoves + 1





