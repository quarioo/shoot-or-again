import sys

import pygame
import random
import time


def game():
    pygame.init()
    pygame.display.set_caption("shot or again")
    size = width, height = 1550, 840
    screen = pygame.display.set_mode(size)


    running = True

    fps = 60
    clock = pygame.time.Clock()
    pos_vil = random.randrange(1, 7)
    while running:
        tic = time.perf_counter()
        if time.perf_counter() - tic > 1:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    if pos_vil == 1:
                        pos_vil = random.randrange(1, 7)
                    else:
                        pos_vil = random.randrange(1, 7)
                elif event.key == pygame.K_w:
                    if pos_vil == 2:
                        pos_vil = random.randrange(1, 7)
                    else:
                        pos_vil = random.randrange(1, 7)
                elif event.key == pygame.K_e:
                    if pos_vil == 3:
                        pos_vil = random.randrange(1, 7)
                    else:
                        pos_vil = random.randrange(1, 7)
                elif event.key == pygame.K_i:
                    if pos_vil == 4:
                        pos_vil = random.randrange(1, 7)
                    else:
                        pos_vil = random.randrange(1, 7)
                elif event.key == pygame.K_o:
                    if pos_vil == 5:
                        pos_vil = random.randrange(1, 7)
                    else:
                        pos_vil = random.randrange(1, 7)
                elif event.key == pygame.K_p:
                    if pos_vil == 6:
                        pos_vil = random.randrange(1, 7)
                    else:
                        pos_vil = random.randrange(1, 7)
                else:
                    pos_vil = random.randrange(1, 7)

        screen.fill((0, 0, 0))
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 600, 200
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont('Arial', 40)

objects = []


class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def process(self):

        mousePos = pygame.mouse.get_pos()

        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)

customButton = Button(100, 50, 400, 100, 'НАЧАТЬ', game)

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for object in objects:
        object.process()

    pygame.display.flip()
    fpsClock.tick(fps)