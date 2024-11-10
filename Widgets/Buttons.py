from pygame import Rect , mouse
from pygame.draw import rect as drawRect
class RaisedButton(object):
    def __init__(self,screenobject, fontobject, text, x, y, width, height, textcolor, topcolor, bottomcolor, tophover, bottomhover, elevation):
        self.top_rect = Rect((x,y), (width, height))
        self.top_color = topcolor  
        self.top_colorOrignl = topcolor
        self.font_object = fontobject
        self.screen = screenobject
        self.text_color = textcolor
        self.top_hovercolor = tophover
        
        self.text = text
        self.elevation =elevation
        self.dynamic_elevation = elevation
        self.orig_pos = [x,y]
        
        self.text_surf = fontobject.render(text, True, self.text_color)
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        #bottom rectangle
        self.bottom_rect = Rect((x,y), (width, elevation))
        self.bottom_color = bottomcolor
        self.bottom_colorOrgnl = bottomcolor
        self.bottom_hovercolor = bottomhover

        self.pressed = False
        self.clicked = False
    def draw(self):
        self.top_rect.y = self.orig_pos[1] - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.text_rect.midtop
        self.bottom_rect.height = self.top_rect.height - 10 + self.dynamic_elevation


        drawRect(self.screen, self.bottom_color, self.bottom_rect, border_radius=12)
        #self.screen.blit(self.text_surf, self.text_rect)
        drawRect(self.screen, self.top_color, self.top_rect, border_radius=12)
        self.screen.blit(self.text_surf, self.text_rect)
        #self.check_click()
    def check_click(self):
        mouse_pos = mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            mouseClicks = mouse.get_pressed()
            self.top_color = self.top_hovercolor
            self.bottom_color = self.bottom_hovercolor
            if mouseClicks[0]:
                self.dynamic_elevation = 0
                self.pressed = True
                #print(self.top_rect.height," ",self.bottom_rect.height)
            elif self.pressed:
                self.pressed = False
                self.clicked = True
                self.dynamic_elevation = self.elevation
                #print(self.top_rect.height," ",self.bottom_rect.height)
                
        else:
            self.top_color = self.top_colorOrignl
            self.bottom_color = self.bottom_colorOrgnl
            self.dynamic_elevation = self.elevation
    def update(self):
        if self.clicked and not self.pressed:
            self.clicked = False
        self.draw()
        self.check_click()









