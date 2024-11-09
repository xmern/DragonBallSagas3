from DTOs.SceneDtos import SceneUpdate

class GuiScene(object):
    def __init__(self, screen,eventCodes):
        self.done = False
        self.closing = False
        self.screen = screen
        self.eventCodes = eventCodes
    def update(self, events):
        for event in events:
            if event.type == self.eventCodes.close:
                return SceneUpdate(True, True)
        self.screen.fill((255,255,255))
        return SceneUpdate(False, False)





