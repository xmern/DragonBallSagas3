from Scenes.Scene import GuiScene
from DTOs.SceneDtos import SceneUpdate, TitleSceneUpdate

class TitleScreen(GuiScene):
    def __init__(self, scale, screen, background, eventCodes, spriteGroup, screensize):
        super().__init__( screen, eventCodes)
        self.screen = screen
        self.scale = scale
        self.backGround = background
        self.backGrounds = spriteGroup()
        self.buttons = spriteGroup()
        self.effects = spriteGroup()
        self.backGrounds.add(background)
        self.screenSize = screensize
        self.init()

    def init(self):
        #self.backGround.setSize(self.screenSize[0] + 196, self.screenSize[1])
        self.backGround.rect.y += 20
        pass

    def update(self, events):
        for event in events:
            if event.type == self.eventCodes.close:
                return TitleSceneUpdate(True, True)
        self.screen.fill((0,0,0))
        self.backGrounds.draw(self.screen)
        self.backGrounds.update()
        return SceneUpdate(False, False)


        




