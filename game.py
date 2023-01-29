import os
import sys
from typing import Tuple

import pygame


class Game:
    def __init__(self, main):
        self.main = main

    def load_image(self, name, colorkey: Tuple[int, int] = None) -> pygame.image:
        """Берет изображения для спрайтов и картинок"""
        if not os.path.isfile(name):
            print(f"Файл с изображением '{name}' не найден")
            sys.exit()

        image = pygame.image.load(name)
        image = self.make_image_transparency(image, colorkey)

        return image

    def make_image_transparency(self, image, colorkey: Tuple[int, int] = None) -> pygame.image:
        """
        Функция сделает цвет colorkey прозрачным на всей картинке.
        Если colorkey не задан, то используется цвет левого верхнего угла
        """
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()

        return image

    def start(self):
        image = self.load_image('.\pictures\character_big_gun_right.gif')
        self.main.screen.blit(image, (0, 0))
