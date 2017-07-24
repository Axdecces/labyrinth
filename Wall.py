from Rectangle import Rectangle
import pygame

class Wall():
    def __init__(self, game, position):
        self.game = game
        self.init(position)

    def init(self, position):
        self.position = [position[0]*16,position[1]*16]
        self.rect = Rectangle(self.game, self.position, [16, 16],  [150, 150, 150])

    def draw(self, screen):
        self.rect.draw(screen)