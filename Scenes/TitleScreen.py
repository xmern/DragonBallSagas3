from Scenes.Scene import GuiScene
from DTOs.SceneDtos import SceneUpdate, TitleSceneUpdate
from Widgets.TextWidgets import TEXTFONT
from Widgets.Buttons import RaisedButton

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
        self.timer = 0
        
        self.init()

    def init(self):
        #self.backGround.setSize(self.screenSize[0] + 196, self.screenSize[1])
        self.backGround.rect.y += 20
        self.arcadeButton = RaisedButton(self.screen,TEXTFONT,"Arcade", 500, 500, 200, 50, (0,0,0), (255,144,31), (240, 40, 15),(255,248,112), (255,141,31),6)
        self.storyButton = RaisedButton(self.screen,TEXTFONT,"Story", 500, 580, 200, 50, (0,0,0), (255,144,31), (240, 40, 15),(255,192,0), (240, 40, 15), 6)
        self.fadeIn = 20

    def update(self, events):
        
        for event in events:
            if event.type == self.eventCodes.close:
                return TitleSceneUpdate(True, True)
        self.screen.fill((0,0,0))
        
        self.backGrounds.draw(self.screen)
        self.backGrounds.update()
        if self.timer >= self.fadeIn + 1:
            if self.backGround.transparency > 250:
                self.backGround.transparency -= 5
        if self.timer > self.fadeIn and self.backGround.transparency <= 250:
            self.arcadeButton.update()
            self.storyButton.update()
        self.timer += 1
        return SceneUpdate(False, False)


        




