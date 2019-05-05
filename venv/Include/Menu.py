import pygame
import Chapter
import Plane
scoreboard_font=pygame.font.Font(None, 27)
scoreboard_msg=scoreboard_font.render("Player Score:",1,pygame.Color("Purple"))
scoreboard_msg_size=scoreboard_font.size("player score")
scoreboard_numb_font = pygame.font.Font(None, 27)

class Menu_ButtonItem():
    def __init__(self, name, width=100, height=100, centerlocation=(0, 0), mainColor=(128, 128, 128),
                 onMouseOverColor=(128, 150, 150), onMouseDownColor=(50, 100, 150), text="notext", textSize=100,
                 textColor=(0, 0, 0),):
        self.name = name
        self.colorList = [mainColor, onMouseOverColor, onMouseDownColor]
        self.centerlocation = centerlocation
        self.width = width
        self.height = height
        self.rectangle = pygame.rect.Rect(0, 0, self.width, self.height)
        self.rectangle.center = centerlocation
        self.score=0
        self.text = text
        self.textSize = textSize
        self.textColor = textColor
        self.fontedText = pygame.font.Font("fonts/ARCADE.TTF", self.textSize).render(self.text, True, self.textColor)
        self.textRectangle = pygame.rect.Rect(0, 0, self.fontedText.get_width(), self.fontedText.get_height())
        self.textRectangle.center = self.rectangle.center

        self.isMouseOver = False  # mouse is over
        self.state = 0  # mouse state for color changing

        self.mouseDownEvent = pygame.event.Event(pygame.USEREVENT, attr1=self.name, attr2="mouseDownEvent")
        self.mouseUpEvent = pygame.event.Event(pygame.USEREVENT, attr1=self.name, attr2="mouseUpEvent")


    def checkMouseOver(self, mlocation):
        if self.state == 2:
            return True
        if self.rectangle.collidepoint(mlocation):
            self.state = 1
            return True
        self.state = 0
        return False

    def onMouseDown(self, mlocation):
        if self.rectangle.collidepoint(mlocation):
            pygame.event.post(self.mouseDownEvent)
            self.state = 2

    def onMouseUp(self, mlocation):
        if self.state == 2:
            pygame.event.post(self.mouseUpEvent)
            self.state = 0
            self.checkMouseOver(mlocation)

    def draw(self, screen):
        pygame.draw.rect(screen, self.colorList[self.state], self.rectangle)
        screen.blit(self.fontedText, self.textRectangle)


class Menu_TextItem():

    def __init__(self, name, text="notext", textSize=100, mainColor=(128, 128, 128), onMouseOverColor=(128, 150, 150),
                 onMouseDownColor=(128, 150, 150), centerlocation=(0, 0)):
        self.name = name
        self.text = text
        self.textSize = textSize
        self.colorList = [mainColor, onMouseOverColor, onMouseDownColor]

        self.centerlocation = centerlocation
        self.fontedTextList = [
            pygame.font.Font("fonts/ARCADE.TTF", self.textSize).render(self.text, True, self.colorList[0]),
            pygame.font.Font("fonts/ARCADE.TTF", self.textSize).render(self.text, True, self.colorList[1]),
            pygame.font.Font("fonts/ARCADE.TTF", self.textSize).render(self.text, True, self.colorList[2])
            ]
        self.width = self.fontedTextList[0].get_width()
        self.height = self.fontedTextList[0].get_height()

        self.rectangle = pygame.rect.Rect(0, 0, self.width, self.height)
        self.rectangle.center = centerlocation
        self.isMouseOver = False  # mouse is over
        self.state = 0  # mouse state for color changing
        self.mouseDownEvent = pygame.event.Event(pygame.USEREVENT, attr1=self.name, attr2="mouseDownEvent")
        self.mouseUpEvent = pygame.event.Event(pygame.USEREVENT, attr1=self.name, attr2="mouseUpEvent")

    def checkMouseOver(self, mlocation):
        if self.state == 2:
            return True

        if self.rectangle.collidepoint(mlocation):
            self.state = 1
            return True
        self.state = 0
        return False

    def onMouseDown(self, mlocation):
        if self.rectangle.collidepoint(mlocation):
            pygame.event.post(self.mouseDownEvent)
            self.state = 2

    def onMouseUp(self, mlocation):
        if self.state == 2:
            pygame.event.post(self.mouseUpEvent)
            self.state = 0
            self.checkMouseOver(mlocation)

    def draw(self, screen):
        screen.blit(self.fontedTextList[self.state], self.rectangle)


class Menu():
    def __init__(self, screenrect=pygame.rect.Rect(0, 0, 0, 0)):
        self.isActive = False
        self.objectList = []
        self.clock = pygame.time.Clock()
        self.screenrect = screenrect
        self.initilize()

    def drawScore(self, screen, score):

        mask = pygame.Surface((800, 600), pygame.SRCALPHA)
        mask.fill
        mask.set_alpha(255)
        screen.blit(mask, (0, 0), special_flags=(pygame.BLEND_RGBA_ADD))

        self.image = 0  # to empty it
        self.image = pygame.image.load("images/png/BG.png")
        pygame.transform.scale(pygame.image.load("images/png/BG.png"),
                               (screen.get_width(), screen.get_height()))
        scoreboard_numb = scoreboard_numb_font.render(str(Chapter.score), 1, pygame.Color("Purple"))
        screen.blit(scoreboard_msg, (screen.get_width() - scoreboard_msg_size[0] - 60, 10))
        screen.blit(scoreboard_numb, (screen.get_width() - 45, 10))
    

    def initilize(self):

        self.btnRestart = Menu_ButtonItem(name="button1", text="Restart", width=200, height=50, textSize=50,
                                          mainColor=(34,139,34), onMouseOverColor=(0, 205, 205),
                                          centerlocation=(self.screenrect.center[0], self.screenrect.center[1] - 120))
        self.objectList.append(self.btnRestart)

        self.btnResume = Menu_ButtonItem(name="button2", text="Resume", width=200, height=50, textSize=50,
                                         mainColor=(128,0,128), onMouseOverColor=(0, 205, 205),
                                         centerlocation=(self.screenrect.center[0], self.screenrect.center[1] - 60))
        self.objectList.append(self.btnResume)

        self.btnScore = Menu_ButtonItem(name="button3", text="ScoreBoard", width=250, height=50, textSize=50,
                                       mainColor=(34,139,34), onMouseOverColor=(0, 205, 205),
                                       centerlocation=(self.screenrect.center[0], self.screenrect.center[1]))
        self.objectList.append(self.btnScore)

        self.btnExit = Menu_ButtonItem(name="button4", text="Exit", width=100, height=50, textSize=50,
                                       mainColor=(128,0,128), onMouseOverColor=(0, 205, 205),
                                       centerlocation=(self.screenrect.center[0], self.screenrect.center[1] + 60))

        self.objectList.append(self.btnExit)


    def reset_state(self):
        for item in self.objectList:
            item.state = 0



    def runMenu(self, screen):
        self.reset_state()
        self.isActive = True
        screenshoot = screen.copy()
        while self.isActive:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.isActive = False
                elif event.type == pygame.MOUSEMOTION:
                    self.checkMouseOver(pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.onMouseDown(pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.onMouseUp(pygame.mouse.get_pos())
                elif event == self.btnResume.mouseDownEvent:
                    self.isActive = False

                elif event == self.btnExit.mouseDownEvent:
                    return True
                elif event == self.btnRestart.mouseDownEvent:
                    return True
                elif event == self.btnScore.mouseDownEvent:
                    self.drawScore(screen,Chapter.score)

                screen.blit(screenshoot, (0, 0))
                self.draw(screen)
                pygame.display.update()
                self.clock.tick(60)
        return False

    def checkMouseOver(self, location):
        for item in self.objectList:
            item.checkMouseOver(location)

    def onMouseDown(self, location):
        for item in self.objectList:
            item.onMouseDown(location)

    def onMouseUp(self, location):
        for item in self.objectList:
            item.onMouseUp(location)

    def draw(self, screen):
        for item in self.objectList:
            item.draw(screen)