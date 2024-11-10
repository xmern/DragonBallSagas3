
from pygame.font import SysFont, init
init()
class my_class(object):
    pass
TEXTFONT = SysFont("Arial", 30)
def draw_text(text, surface, font, text_col, x, y):
    img = font.render(text, True, text_col)
    surface.blit(img, (x, y))




