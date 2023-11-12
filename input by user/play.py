import sys
import pygame
import basicGameLogic
from math import log2

# UI
size = width, height = 480, 500
playRegion = 480, 480
FPS = 60

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
fontColor = (82, 52, 42)
defaultTileColor = (232, 232, 232)
tileBoarderColor = fontColor

# Game
boardSize = 4

def drawBoard(screen, board):
    screen.fill(black)
    for i in range(boardSize):
        for j in range(boardSize):
            color = defaultTileColor
            numberText = ''
            if board[i][j] != 0:
                gComponent = 235 - log2(board[i][j]) * ((235 - 52) / (boardSize ** 2))
                color = (235, gComponent, 52)
                numberText = str(board[i][j])
            rect = pygame.Rect(j * playRegion[0] / boardSize,
                                i * playRegion[1] / boardSize,
                                playRegion[0] / boardSize,
                                playRegion[1] / boardSize)

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, fontColor, rect, 1)

            fontImage = tileFont.render(numberText, 0, fontColor)
            if fontImage.get_width() > playRegion[0] / boardSize:
                fontImage = pygame.transform.scale(fontImage,
                                                   (playRegion[0] / boardSize,
                                                    fontImage.get_height() / fontImage.get_width() * playRegion[
                                                        0] / boardSize))
            screen.blit(fontImage,
                        (j * playRegion[0] / boardSize + (playRegion[0] / boardSize - fontImage.get_width()) / 2,
                         i * playRegion[1] / boardSize + (playRegion[1] / boardSize - fontImage.get_height()) / 2))

    fontImage = scoreFont.render("Score: {:,}".format(sum(map(sum, board))), 1, white)  # Sum of all elements
    screen.blit(fontImage, (1, playRegion[1] + 1))


def handleInput(event, board):
    if event.type == pygame.QUIT:
        sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            basicGameLogic.board = basicGameLogic.merge_right(basicGameLogic.board)
            basicGameLogic.addNewValue()
        elif event.key == pygame.K_LEFT:
            basicGameLogic.board = basicGameLogic.merge_left(basicGameLogic.board)
            basicGameLogic.addNewValue()
        elif event.key == pygame.K_UP:
            basicGameLogic.board = basicGameLogic.merge_up(basicGameLogic.board)
            basicGameLogic.addNewValue()
        elif event.key == pygame.K_DOWN:
            basicGameLogic.board = basicGameLogic.merge_down(basicGameLogic.board)
            basicGameLogic.addNewValue()

def gameLoop():
    clock = pygame.time.Clock()
    basicGameLogic.board = basicGameLogic.initialize_board(boardSize)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                handleInput(event, basicGameLogic.board)

        drawBoard(screen, basicGameLogic.board)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("2048")
    tileFont = pygame.font.SysFont("", 72)
    scoreFont = pygame.font.SysFont("", 22)
    gameLoop()
