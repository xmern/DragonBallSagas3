import pygame
from Scenes.Scene import GuiScene 
from Scenes.TitleScreen import TitleScreen
from DTOs.SceneDtos import SceneEventCodes
from Widgets.ImageLoaders import TextureLoader
from MetaData.Assets import Backgrounds
from Widgets.Textures import Texture
import sys

class Game_():
    def __init__(self, screenSize):
        self.screenSize = screenSize
        self.screen = pygame.display.set_mode(self.screenSize)
        pygame.display.set_caption("Dragon Ball Sagas")
        self.clock = pygame.time.Clock()
        self.done = False
        self.sceneEventCodes = SceneEventCodes()
        self.sceneTransitions = {"Story":"",}
        self.imageContext = pygame.image
        
        #self.scene = GuiScene(self.screen, self.sceneEventCodes)

    def init(self):
        pygame.init()
        self.textureLoader = TextureLoader(self.imageContext)
        self.sceneEventCodes.setClose(pygame.QUIT)
        self.backGroundData = Backgrounds()

        selectBack = Texture(1,self.textureLoader.loadImage(self.backGroundData.get_Background("titleScreen")), 0,0)
        self.scene = TitleScreen(1,self.screen, selectBack, self.sceneEventCodes, pygame.sprite.Group, self.screenSize)
    def close(self):
        pygame.quit()
        sys.exit()
    def sceneDataManager(self, sceneData):
        if sceneData.close:
            self.close()

    def run(self):
        while not self.done:
            
            sceneData = self.scene.update(pygame.event.get())
            self.sceneDataManager(sceneData)
            self.clock.tick(60)
            pygame.display.flip()





