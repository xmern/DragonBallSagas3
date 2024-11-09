class SceneUpdate(object):
    def __init__(self, close, sceneDone):
        self.close = close
        self.sceneDone = sceneDone
        self.nextScene = "Play"
class TitleSceneUpdate(object):
    def __init__(self, close, sceneDone):
        self.close = close
        self.sceneDone = sceneDone
        self.nextScene = "Play"
class SceneEventCodes():
    def __init__(self):
        self.close = None
    def setClose(self, close):
        self.close = close




