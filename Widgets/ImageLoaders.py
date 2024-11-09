class TextureLoader(object):
    def __init__(self, imageContext):
        self.imageContext = imageContext
    def loadImage(self, imagePath):
        image = self.imageContext.load(imagePath)
        return image




