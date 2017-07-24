from Scene import Scene
import pygame

class Scene_Menu(Scene):
    def __init__(self, game):
        Scene.__init__(self, game)

    def init(self):
        pygame.font.init()
        self.font = pygame.font.Font('assets/fonts/Munro.ttf', 30)

    def update(self, delta_time, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game.scene_manager.set_scene('Level')

    def draw(self, screen):
        text_surface_1 = self.font.render('LABYRINTH', False, (100, 100, 100))
        text_surface_2 = self.font.render('press ENTER to start', False, (100, 100, 100))
        screen.blit(text_surface_1,(64,64))
        screen.blit(text_surface_2,(64,480))