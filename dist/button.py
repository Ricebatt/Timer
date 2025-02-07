import pygame
class JustText:
    def __init__(self, text="", x=0, y=0, width=200, height=180, textFont="calibri", textSize=40):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.textFont = textFont
        self.textSize = textSize

    def setX(self, newX):
        self.x = newX

    def setY(self, newY):
        self.y = newY

    def setText(self, newText):
        self.text = newText

    def draw(self, win):
        font = pygame.font.SysFont(self.textFont, self.textSize)
        text = font.render(self.text, True, (0, 0, 0))
        win.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2),
                        self.y + round(self.height / 2) - round(text.get_height() / 2)))

class Button:
    def __init__(self, text="", x=0, y=0, color=0, width=200, height=180, borderColor=pygame.Color(150, 150, 150)):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.selected = False
        self.borderColor = borderColor

    def setX(self, newX):
        self.x = newX

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False

    def setY(self, newY):
        self.y = newY

    def setColor(self, newColor):
        self.color = newColor

    def setText(self, newText):
        self.text = newText

    def draw(self, win):
        pygame.draw.rect(win, pygame.Color(0, 0, 0), (self.x, self.y, self.width, self.height))
        if self.selected:
            pygame.draw.rect(win, pygame.Color(150, 150, 150), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, self.color, (self.x + 5, self.y + 5, self.width - 10, self.height - 10))
        font = pygame.font.SysFont("Ink Free", 50)
        text = font.render(self.text, True, (0, 0, 0))
        win.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2),
                        self.y + round(self.height / 2) - round(text.get_height() / 2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False