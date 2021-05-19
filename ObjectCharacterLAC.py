import pygame as pg
import pygame
from InputDataBox import InputDataBox, inputForPC

class ObjectCharacterPC():

    def __init__(self, rect, option, screen):
        self.screen = screen
        print(type(self.screen))
        characters = pygame.image.load("grafiki/lac.png")
        self.rect = pg.Rect(rect)
        self.click = False
        self.image = pg.Surface(self.rect.size).convert()
        # self.image.fill((255,255,255))
        self.image.blit(characters, (0, 0))

    def clicked(self, m_pos):
        return self.rect.collidepoint(m_pos)

    def set_offset(self, m_pos):
        self.dragging = True
        m_x, m_y = m_pos
        self.offset_x = self.rect.x - m_x
        self.offset_y = self.rect.y - m_y

    def update(self, surface):
        if self.click:
            drawGrid(self.screen)
            self.rect.center = pg.mouse.get_pos()
        # pg.draw.line(surface, (0,0,0), (0,0), (100,100))
        surface.blit(self.image, self.rect)

    # USUN OBIEKT Z PLANSZY
    def deleteObject(selected_option, i, delListOfObjects):

        delListOfObjects.remove(delListOfObjects[i])
        # for x in delListOfObjects:
        #     assert isinstance(x.update, object)
        #     x.update(Screen)
        # pass

    # DODAJ ŁACZE MIEDZY OBIEKTAMI
    def addLink(selected_option, i, listOfObjects):
        # print("xDDD", listOfObjects[i].rect.x)
        pass
        # link = Link(listOfObjects[i],listOfObjects[i+1])
        # print("xDDD  ",link.x.rect.x," " ,link.y.rect.x)

    # ZMIEN USTAWIENIA OBIEKTU
    def changeSettings(selected_option, i, listOfObjects, Screen):
        # changeSet = InputDataBox()
        inputForPC(Screen) # tu trzeba jakoś pozmieniać
        pass

def drawGrid(Screen):

    BLACK = (0, 0, 0)
    WHITE = (200, 200, 200)
    WINDOW_HEIGHT = 1600
    WINDOW_WIDTH = Screen.get_width() // (10) * 8
    blockSize = 20  # Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(Screen, WHITE, rect, 1)

