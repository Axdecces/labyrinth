import importlib

class SceneManager():
    def __init__(self, game):
        self.game = game
        self.current_scene_id = ''
        self.current_scene = None

    def get_scene_class_by_name(self, name):
        try:
            name = 'Scene_' + name
            scene_class = getattr(getattr(importlib.import_module('Scenes'), name), name)
        except AttributeError:
            return None
        else:
            return scene_class

    def set_scene(self, sceneId):
        if self.current_scene != None:
            self.current_scene.destroy()
        scene_class = self.get_scene_class_by_name(sceneId)
        if scene_class != None:
            self.current_scene = scene_class(self.game)
            self.current_scene_id = sceneId

    def update(self, delta_time, events):
        if self.current_scene != None:
            self.current_scene.update(delta_time, events)

    def draw(self, screen):
        if self.current_scene != None:
            self.current_scene.draw(screen)