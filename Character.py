from Rectangle import Rectangle
from Map import Map
import pygame

class Character():
    def __init__(self, game, position):
        self.game = game
        self.init(position)
        self.map = Map(game)

    def init(self, position):
        self.position = position
        self.rect = Rectangle(self.game, position, [16, 16],  [200, 0, 0])
        self.velocity_x = 16
        self.velocity_y = 16

    def keep_in_bounds(self):
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.x > self.game.width:
            self.rect.x = self.game.width
        if self.rect.y > self.game.height:
            self.rect.y = self.game.height

    def move_up(self):
        if self.map.tile_map[int(self.rect.y / 16 - 1)][int(self.rect.x / 16)] == 128:
            self.game.scene_manager.set_scene('Win')
        if self.map.tile_map[int(self.rect.y / 16 - 1)][int(self.rect.x / 16)] != 0:
            self.rect.move_ip(0, -self.velocity_y)

    def move_down(self):
        if self.map.tile_map[int(self.rect.y / 16 + 1)][int(self.rect.x / 16)] == 128:
            self.game.scene_manager.set_scene('Win')
        if self.map.tile_map[int(self.rect.y / 16 + 1)][int(self.rect.x / 16)] != 0:
            self.rect.move_ip(0, self.velocity_y)

    def move_left(self):
        if self.map.tile_map[int(self.rect.y / 16)][int(self.rect.x / 16) - 1] == 128:
            self.game.scene_manager.set_scene('Win')
        if self.map.tile_map[int(self.rect.y / 16)][int(self.rect.x / 16) - 1] != 0:
            self.rect.move_ip(-self.velocity_x, 0)

    def move_right(self):
        if self.map.tile_map[int(self.rect.y / 16)][int(self.rect.x / 16) + 1] == 128:
            self.game.scene_manager.set_scene('Win')
        if self.map.tile_map[int(self.rect.y / 16)][int(self.rect.x / 16) + 1] != 0:
            self.rect.move_ip(self.velocity_x, 0)

    def move_direction(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.move_up()
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.move_down()
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.move_left()
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.move_right()

    def update_position(self, events):
        self.keep_in_bounds()
        self.move_direction(events)

    def update(self, delta_time, events):
        self.update_position(events)

    def draw(self, screen):
        self.rect.draw(screen)
