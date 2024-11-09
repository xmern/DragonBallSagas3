#BackGrounds = {'titleScreen':"assets\backgrounds\DBSZ_banner_mobile.jpg"}
class Backgrounds(object):
    def __init__(self):
        self.backGrounds = {'titleScreen':"assets/backgrounds/DBSZ_banner_mobile.jpg"}
    def get_Background(self, name):
        if name in self.backGrounds:
            return self.backGrounds[name]
        else:
            return False




