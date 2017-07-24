import sys, pygame
from SceneManager import SceneManager

class Game():
    def __init__(self):
        self.scene_manager = SceneManager(self)
        pygame.init()
        self.size = self.width, self.height = 640, 640
        self.background_color = 200, 200, 200
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.scene_manager.set_scene('Menu')
        while True:
            delta_time = 1 / float(self.clock.tick(60))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
            self.update(delta_time, events)
            self.screen.fill(self.background_color)
            self.draw(self.screen)
            pygame.display.flip()

    def update(self, delta_time, events):
        self.scene_manager.update(delta_time, events)

    def draw(self, screen):
        self.scene_manager.draw(screen)