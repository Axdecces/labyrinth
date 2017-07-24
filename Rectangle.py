import pygame

class Rectangle(pygame.Rect):

    def __init__(self, game, position, size, color):
        super(Rectangle, self).__init__(position, size)
        self.game = game
        self.color = color

    def change_color(self, color):
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self)