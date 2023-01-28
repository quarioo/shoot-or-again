import sys

import pygame
from pygame.locals import *

from start_menu import Button
from game import Game

FPS = 60
RUNNING = True

pygame.init()


class Main:
    def __init__(self):
        pygame.display.set_caption('Shoot or again?')

        self.clock = pygame.time.Clock()

        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.screen = pygame.display.set_mode((1920, 1080))
        self.width, self.height = self.screen.get_width(), self.screen.get_height()
        print(self.width, self.height)

        self.font = pygame.font.Font('./fonts/ZenDots-Regular.ttf', 40)
        start_text = self.font.render('REGISTRATION', True, 'Blue')

        self.objects = []

        start_button = Button(
            self, 'Start', 200, 40, (self.width / 2 - 200 / 2, self.height / 2 - 40 / 2), 5
        )
        self.objects.append(start_button)

        self.is_game_starting = False
        self.game = Game(self)

        while RUNNING:
            self.loop()
            self.clock.tick(FPS)

    def loop(self):
        """Main game loop"""
        self.eventLoop()

        self.tick()
        self.draw()
        pygame.display.update()

    def eventLoop(self):
        """The main event loop, detects keypresses"""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if self.is_game_starting and event.type == KEYDOWN:
                self.game.start()


    def tick(self):
        self.time = self.clock.tick()
        self.keys_pressed = pygame.key.get_pressed()

    def draw(self):
        for game_object in self.objects:
            game_object.draw()


if __name__ == '__main__':
    Main()
