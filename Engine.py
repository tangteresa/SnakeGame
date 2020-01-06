import numpy as np
import pygame
import Player
import Board
import Tail
import Snack
import StateChanges
import time
import numpy as np
from pygame.locals import *

squareSize = 50
screenWidth = 600
screenHeight = screenWidth
stepsUntilAction = 40

"""NOTE: Snake starts in top left corner"""
def blitTailSegments(tailSegmentsList, screen):
    for segment in tailSegmentsList:
        screen.blit(segment.surf, (segment.rect))

def updateTailSegments(tailSegmentsList, statesList):
    for segment in tailSegmentsList:
        segment.update(statesList)

def snackCollision(tailSegmentsList, gamer, snack, step):
    if gamer.snackCollision(snack):
        end = len(tailSegmentsList) - 1
        (tailSegmentsList[end]).notIsLast()
        newTail = Tail.Tail(tailSegmentsList[end], screenWidth, screenHeight, squareSize, stepsUntilAction, step)
        tailSegmentsList.append(newTail)
        snack.moveSnack()

"""If snake collides with itself, game is over"""
def selfCollision(gamer, tailSegmentsList):
    if gamer.selfCollision(tailSegmentsList):
        pygame.display.quit()
        pygame.quit()


def main():
    pygame.init()
    step = 0

    screen = pygame.display.set_mode((screenWidth, screenHeight))

    # create key game elements
    tiles = Board.Board(screenWidth, screenHeight, squareSize)
    gamer = Player.Player(screenWidth, screenHeight, squareSize, stepsUntilAction, step)
    tail = Tail.Tail(gamer, screenWidth, screenHeight, squareSize, stepsUntilAction, step)
    snack = Snack.Snack(screenWidth, screenHeight, squareSize)

    # list of key presses and location they occurred
    statesList = StateChanges.StateChanges()

    # list of segments in the tail
    tailSegmentsList = [tail]

    # add the text "Press space to begin"
    pygame.font.init()
    gameFont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = gameFont.render('Press space to begin', False, (0, 0, 0))

    # wait for player to press any key to start game
    waiting = True

    # game is automatically set to run
    running = True

    #//////////////////////////////////////////////////////////////////////////////////
    # waiting screen

    while waiting:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    waiting = False
                    running = False
            elif event.type == QUIT:
                waiting = False
                running = False

        screen.fill((0, 0, 255))
        screen.blit(textsurface, ((screenWidth - 425), (screenHeight - 425)))
        pygame.display.flip()

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_SPACE]:
            waiting = False


    # ///////////////////////////////////////////////////////////////////////////////////////
    # begin game

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

        pressed_keys = pygame.key.get_pressed()

        # determine if player has eaten snack
        snackCollision(tailSegmentsList, gamer, snack, step)

        # determine if player has collided with self
        selfCollision(gamer, tailSegmentsList)

        # update positions
        gamer.update(pressed_keys, statesList)
        updateTailSegments(tailSegmentsList, statesList)

        # determine score
        score = gameFont.render((" " + str(snack.numMoves)), False, (0, 0, 0))

        # begin drawing
        #screen.fill((0, 0, 0))
        screen.blit(tiles.surf, (0, 0))
        screen.blit(snack.surf, (snack.rect))
        screen.blit(gamer.surf, (gamer.rect))
        blitTailSegments(tailSegmentsList, screen)
        screen.blit(score, (gamer.rect))

        pygame.display.flip()

        # increase game counter
        step = step + 1

        # change this delay to speed up game
        # note that an overly high delay may cause lag in the game
        pygame.time.delay(3)

if __name__ == '__main__':
    main()