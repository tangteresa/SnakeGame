import pygame

class Board(pygame.sprite.Sprite):
    def __init__(self, screenWidth, screenHeight, squareSize):
        super(Board, self).__init__()

        self.surf = pygame.Surface((screenWidth, screenHeight))

        # size[number of rows, number of columns]
        size = [screenWidth//squareSize, screenHeight//squareSize]

        self.color(size, squareSize)

    """Colors the tiles of the board in checkerboard style"""
    def color(self, size, squareSize):
        for row in range(size[0]):
            for col in range(size[1]):
                # green fill
                if (row + col) % 2 == 0:
                    pygame.draw.rect(self.surf, (63, 252, 113), (row*squareSize, col*squareSize, squareSize, squareSize))

                # blue fill
                else:
                    pygame.draw.rect(self.surf, (63, 135, 252), (row * squareSize, col * squareSize, squareSize, squareSize))



