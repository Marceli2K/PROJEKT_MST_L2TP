# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame

import os, sys
import pygame as pg  # lazy but responsible (avoid namespace flooding)
from OptionBox import OptionBox as OB



lista_obiektow = []

class Character:
    def __init__(self, rect, option):
        characters = 0
        if option == 0:
            characters = pygame.image.load("grafiki/pc.png")
        elif option == 1:
            characters = pygame.image.load("grafiki/switch.png")
        elif option == 2:
            characters = pygame.image.load("grafiki/router.png")
        self.rect = pg.Rect(rect)
        self.click = False
        self.image = pg.Surface(self.rect.size).convert()
        self.image.fill((255,255,255))
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
            self.rect.center = pg.mouse.get_pos()
        surface.blit(self.image, self.rect)

    # USUN OBIEKT Z PLANSZY
    def deleteObject(selected_option, i, delListOfObjects):
        print(selected_option, i)
        print(delListOfObjects.__len__())
        delListOfObjects.remove(delListOfObjects[i])
        # for x in delListOfObjects:
        #     assert isinstance(x.update, object)
        #     x.update(Screen)
        # pass


    # DODAJ ŁACZE MIEDZY OBIEKTAMI
    def addLink(selected_option, i, listOfObjects):
        pass

    #ZMIEN USTAWIENIA OBIEKTU
    def changeSettings(selected_option, i, listOfObjects):
        pass


#główna funkcja odpowiadająca za obsługe obiektów, pierwszy if to gdy nie ma żadnego obiektu, natomiast drugi gdy już jakiś obiekt jest na planszy
def main(Surface, listOfObject):
    pygame.display.set_caption('L2TP Projekt')
    if len(listOfObject) ==  0:
        Player = None
        while Player == None:
            Player = game_event_loop_withoutPlayer()
        listOfObject.append(Player)
        try:
            listOfObject.pop(1)
        except:
            print("a")
        if listOfObject:
            Surface.fill((255, 255, 255))
            for x in listOfObject:
                assert isinstance(x.update, object)
                x.update(Surface)
    else:
        game_event_loop_withPlayer(listOfObject)
        Surface.fill((255, 255, 255))
        for x in listOfObject:
            assert isinstance(x.update, object)
            x.update(Surface)


# funkcja dodająca nowe obiekty po wykonaniu opcji prawy klik i wybraniu z menu rodzaju obiektu
def add_new_object(option):
    MyPlayer = Character((0, 0, 75, 75), option)
    lista_obiektow.append(MyPlayer)
    MyPlayer.rect.center = Screen.get_rect().center
    lista_obiektow[-1].update(Screen)
    return False, MyPlayer

# funkcja dodająca menu dodawania nowych obiektów
def moreOption(listOfObjects):
    mpos = pygame.mouse.get_pos()
    x = mpos[0]
    y = mpos[1]
    menu_obiektow = OB(x, y, 160, 40, (150, 150, 150), (100, 200, 255), pygame.font.SysFont("Comic Sans", 30),
                       ["Dodaj PC", "Dodaj Switch", "Dodaj Router"])
    whiles = True
    clock = pygame.time.Clock()
    MyPlayer = 0
    while whiles == True:
        mpos = pygame.mouse.get_pos()
        clock.tick(60)
        selected_option = -1
        if ((x + 170) >= mpos[0] >= x - 10 and (y + 150) >= mpos[1] >= y - 10):
            event_list = pygame.event.get()
            selected_option = menu_obiektow.update_menu(event_list)
            menu_obiektow.draw_menu_on_screen(Screen)
            pygame.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit();
                    sys.exit()
            if (selected_option > -1):
                whiles, MyPlayer = add_new_object(selected_option)
        else:
            whiles = False

    return MyPlayer



def moreOption_edit_object(listOfObjects, i):
    mpos = pygame.mouse.get_pos()
    x = mpos[0]
    y = mpos[1]
    menu_obiektow = OB(x, y, 200, 40, (150, 150, 150), (100, 200, 255), pygame.font.SysFont("Comic Sans", 30),
                       ["Usuń obiekt", "Dodaj łącze", "Edytuj ustawienia"])
    whiles = True
    clock = pygame.time.Clock()
    MyPlayer = 0
    while whiles == True:
        mpos = pygame.mouse.get_pos()
        clock.tick(60)
        selected_option = -1
        if ((x + 220) >= mpos[0] >= x - 10 and (y + 150) >= mpos[1] >= y - 10):
            event_list = pygame.event.get()
            selected_option = menu_obiektow.update_menu(event_list)
            menu_obiektow.draw_menu_on_screen(Screen)
            pygame.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit();
                    sys.exit()
            if (selected_option == 0):
                Character.deleteObject(selected_option, i, listOfObjects)
                break
            elif (selected_option == 1):
                Character.addLink(selected_option, i, listOfObjects)
            elif (selected_option == 2):
                Character.changeSettings(selected_option, i, listOfObjects)
        else:
            whiles = False

    return MyPlayer

def game_event_loop_withPlayer(listOfObjects):
    new_player = 0
    collid = []
    for event in pg.event.get():
        for i, object in enumerate(listOfObjects):
            # new_player += 1
            if event.type == pg.MOUSEBUTTONDOWN:
                if object.rect.collidepoint(event.pos) and event.button == 1: # przesuwanie obiektem przy pomocy lewego przycisku myszy
                    object.click = True
                elif object.rect.collidepoint(event.pos) and event.button == 3: # włączanie większej liczby opcji po naciśnieciu prawego przycisku
                    moreOption_edit_object(listOfObjects, i)
                    break

                elif event.button == 3 and not object.rect.collidepoint(event.pos): #dodawanie nowych obiektów na polu
                    for ii, ob in enumerate(listOfObjects): # Niestety z jakiegoś powodu powyższy elif nie zawsze działa dlatego tu należy iterować ponownie aby działały ustawienia dla pozostałych obiektów
                        if object in listOfObjects and ob.rect.collidepoint(event.pos):
                            moreOption_edit_object(listOfObjects, ii)
                    moreOption(listOfObjects) # dodaj nowy obiekt
                    break
            elif event.type == pg.MOUSEBUTTONUP:
                object.click = False
            elif event.type == pg.QUIT: # wyłączanie programu
                pg.quit();
                sys.exit()
    return new_player

def game_event_loop_withoutPlayer() -> object:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
            player = moreOption(object)
            return player
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            print("xx")
        elif event.type == pg.QUIT:
            print("X")
            pg.quit();sys.exit()


if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    Screen = pg.display.set_mode((777, 777))
    background_image = pygame.image.load("grafiki/back.jpg").convert()
    MyClock = pg.time.Clock()
    run = 1
    Screen.fill((255, 2, 255))
    obiekty =[]
    while run == 1:
        main(Screen, lista_obiektow)
        pg.display.update()
        MyClock.tick(60)


