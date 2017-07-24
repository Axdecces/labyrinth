from Scene import Scene
from Character import Character
from Map import Map
import pygame

class Scene_Level(Scene):
    def __init__(self, game):
        Scene.__init__(self, game)

    def init(self):
        self.character = Character(self.game, [16,16])
        self.map = Map(self.game)

    def update(self, delta_time, events):
        self.character.update(delta_time, events)

    def draw(self, screen):
        self.map.draw(screen)
        self.character.draw(screen)