from time import sleep

import pygame as pg
# klasa rysująca linie łącząca dwa obiekty
class Link():

    def __init__(self, startLinkObject, endLinkObject, screen, listaObiektow):
        self.startLinkObject = startLinkObject
        self.endLinkObject = endLinkObject
        x_start, y_start = startLinkObject.get_position()
        x_end, y_end = endLinkObject.get_position()
        self.screen = screen
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.click = False
        self.line =0
        self.listaObiektow = listaObiektow
        self.addLink2()

    def clicked(self, m_pos):
        return self.line.collidepoint(m_pos)


    # nie wiem co tu trzeba zmienić bo to z characteru
    def updateLink(self, surface, x2_start, y2_start, x2_end,y2_end ):
        self.line = pg.draw.line(self.screen, (0, 0, 0), (x2_start, y2_start), (x2_end, y2_end), 3)
        return 1
    # USUN OBIEKT Z PLANSZY
    def deleteObject(selected_option, i, delListOfObjects):

        delListOfObjects.remove(delListOfObjects[i])
        # for x in delListOfObjects:
        #     assert isinstance(x.update, object)
        #     x.update(Screen)
        # pass

    # DODAJ ŁACZE MIEDZY OBIEKTAMI
    # def addLink(self):
    #     xd = 0
    #     while xd == 0:
    #         for event in pg.event.get():
    #             for object in self.listaObiektow:
    #                 print("2")
    #                 print("1")
    #                 if event.type == pg.MOUSEBUTTONDOWN:
    #                     print("3", self.listaObiektow)
    #                     if object.rect.collidepoint(event.pos) and event.button == 1:  # przesuwanie obiektem przy pomocy lewego przycisku myszy
    #                         # object.click = True
    #                         print(pg.mouse.get_pos())
    #                         self.x_end, self.y_end = pg.mouse.get_pos()
    #                         self.line = pg.draw.line(self.screen, (0,0,0), (self.x_start, self.y_start), (self.x_end, self.y_end), 3 )
    #                         xd =1
    #                         endLinkObject = object
    #                         # sleep(10)
    #     return -1, endLinkObject

        # DODAJ ŁACZE MIEDZY OBIEKTAMI
    def addLink2(self):
        self.x_end, self.y_end = pg.mouse.get_pos()
        self.line = pg.draw.line(self.screen, (0, 0, 0), (self.x_start, self.y_start),
                                 (self.x_end, self.y_end), 3)
        xd = 1


        return -1
        #link = Link(listOfObjects[i],listOfObjects[i+1])
        #print("xDDD  ",link.x.rect.x," " ,link.y.rect.x)

