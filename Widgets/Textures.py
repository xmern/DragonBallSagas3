from pygame.sprite import Sprite
from pygame.transform import scale as Scale
class Texture(Sprite):
    def __init__(self,scale, image, x, y):
        super().__init__()
        self.scale = scale
        self.image = image
        self.rect = self.image.get_rect()
        self.opacity = 0
        self.rect.x = x
        self.rect.y = y
        self.transparency = 255
        #self.image = self.scaleImage()
    def scaleImage(self):
        return Scale(self.image, (self.rect.w*self.scale, self.rect.h *self.scale))
    def setSize(self, w, h):
        self.image =  Scale(self.image, (w, h))
    def update(self):
        self.image.set_alpha(self.transparency)



