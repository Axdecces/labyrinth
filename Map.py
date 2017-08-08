import pygame
from PIL import Image


class Map():
    def __init__(self, game):
        self.game = game
        self.wall = 0
        self.floor = 255
        self.grey = 128
        self.colors = {
            0: (150, 150, 150),
            255: (200, 200, 200),
            128: (100, 100, 100)
        }
        self.im = Image.open('assets/maps/map_1.png')
        self.pix = self.im.load()

        self.raw_data = list(self.im.getdata())

        self.tile_map = []

        for pixel in range(self.im.width):
            self.tile_map.append(self.raw_data[pixel * self.im.width:(pixel + 1) * self.im.width])

        self.tile_size = 16
        self.map_width = 40
        self.map_height = 40

    def draw(self, screen):
        for row in range(self.map_height):
            for column in range(self.map_width):
                color = self.colors[self.tile_map[row][column]]
                draw_rect = (
                    column * self.tile_size,
                    row * self.tile_size,
                    self.tile_size,
                    self.tile_size
                )
                pygame.draw.rect(
                    screen,
                    color,
                    draw_rect
                )
