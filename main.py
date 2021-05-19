import os, sys
from time import sleep

import pygame as pg  # lazy but responsible (avoid namespace flooding)
from OptionBox import OptionBox as OB
import pygame_menu
import pygame

from OutputMessage import OutputMessage
from InputDataBox import InputDataBox, inputForPC
from ObjectCharacterPC import *
from Link import Link

# TO DO LIST
# 1 PRZECZYTAJ O MASCE BITOWEJ DLA NIEWIDZIALNEJ LINI
# 2 ZAIMPLEMENTUJ RYSOWANIE LINI ŁĄCZĄCEJ DWA OBIEKTY

lista_obiektow = []
lista_wiadomosci = []
lista_laczy = []
tupleLink = ()
link = 0
selected_option = -1


class connectObjectLine():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.click = False


# główna funkcja odpowiadająca za obsługe obiektów, pierwszy if to gdy nie ma żadnego obiektu, natomiast drugi gdy już jakiś obiekt jest na planszy
def main(Surface, listOfObject, ):
    pygame.display.set_caption('L2TP Projekt')
    if len(listOfObject) == 0:
        Player = None
        while Player == None:
            Player = game_event_loop_withoutPlayer()
        listOfObject.append(Player)
        try:
            # print(listOfObject)
            listOfObject.pop(1)
        except:
            print("a")
        if listOfObject:
            screenDivide()
            drawGrid(Screen)
            for x in listOfObject:
                print(x)
                # assert isinstance(x.update, object)
                x.update(Surface)
    else:
        game_event_loop_withPlayer(listOfObject)
        screenDivide()
        drawGrid(Screen)
        x_start =None
        y_start = None
        x_end =None
        y_end = None
        objectYY=0
        for xx in listOfObject:
            for yy in lista_laczy:
                print(lista_laczy)
                if x_start == None or y_start == None or x_end == None or y_end == None:
                    if xx == yy.startLinkObject:
                        x_start, y_start = xx.get_position()
                        # print("1 :", x, " " , y, " ", yy.x_end, " ", yy.y_end)
                        # yy.updateLink(Screen, x, y, yy.x_end, yy.y_end )
                        pass
                    elif (xx == yy.endLinkObject):
                        x_end, y_end = xx.get_position()
                        # print("2 :",yy.x_start, " " , yy.y_start, " ", x, " ", y)
                        # yy.updateLink(Screen, yy.x_start, yy.y_start, x, y)
                        pass
                else:
                    yy.updateLink(Screen, x_start, y_start, x_end, y_end)
            assert isinstance(xx.update, object)
            xx.update(Surface)


# funkcja dodająca nowe obiekty po wykonaniu opcji prawy klik i wybraniu z menu rodzaju obiektu
def add_new_object(option):
    MyPlayer = ObjectCharacterPC((0, 0, 75, 75), option, Screen)
    lista_obiektow.append(MyPlayer)
    MyPlayer.rect.center = Screen.get_rect().center
    lista_obiektow[-1].update(Screen)
    lista_wiadomosci.append("Dodano nowy oibiekt")

    return False, MyPlayer


# funkcja dodająca menu dodawania nowych obiektów
def moreOption(listOfObjects):
    mpos = pygame.mouse.get_pos()
    x = mpos[0]
    y = mpos[1]
    menu_obiektow = OB(x, y, 240, 40, (150, 150, 150), (100, 200, 255), pygame.font.SysFont("Comic Sans", 30),
                       ["Dodaj PC", "Dodaj Switch", "Dodaj Router", "Client(LAC)", "Server(LNS)"])
    whiles = True
    clock = pygame.time.Clock()
    MyPlayer = None
    while whiles == True:
        mpos = pygame.mouse.get_pos()
        clock.tick(60)
        selected_option = -1
        if ((x + 170) >= mpos[0] >= x - 10 and (y + 255) >= mpos[1] >= y - 10 and mpos[0] < (
                Screen.get_width() // (10) * 8)):
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
    screenDivide()
    return MyPlayer


def moreOption_edit_object(listOfObjects, i, event):
    mpos = pygame.mouse.get_pos()
    x = mpos[0]
    y = mpos[1]
    menu_obiektow = OB(x, y, 200, 40, (150, 150, 150), (100, 200, 255), pygame.font.SysFont("Comic Sans", 30),
                       ["Usuń obiekt", "Dodaj łącze", "Edytuj ustawienia"])
    whiles = True
    clock = pygame.time.Clock()
    MyPlayer = 0
    selected_option = -1
    while whiles == True:
        mpos = pygame.mouse.get_pos()
        clock.tick(60)
        # selected_option = -1
        if ((x + 220) >= mpos[0] >= x - 10 and (y + 150) >= mpos[1] >= y - 10):
            # if selected_option == -1 or selected_option == 1:
            event_list = pygame.event.get()
            selected_option = menu_obiektow.update_menu(event_list)
            menu_obiektow.draw_menu_on_screen(Screen)
            pygame.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit();
                    sys.exit()
            if (selected_option == 0):
                ObjectCharacterPC.deleteObject(selected_option, i, listOfObjects)
                break
            elif (selected_option == 1):
                print("")


            elif (selected_option == 2):
                ObjectCharacterPC.changeSettings(selected_option, i, listOfObjects, Screen)

        elif selected_option == 1:  # obługa dodawania łączy pomiędzy obiektami
            startLinkObject = listOfObjects[i]
            xd = 0
            while xd == 0:
                for event in pg.event.get():
                    for object in listOfObjects:
                        if event.type == pg.MOUSEBUTTONDOWN:
                            if object.rect.collidepoint(
                                    event.pos) and event.button == 1:  # przesuwanie obiektem przy pomocy lewego przycisku myszy
                                endLinkObject = object
                                linkObject = Link(startLinkObject, endLinkObject, Screen, listOfObjects)
                                lista_laczy.append(linkObject)
                                whiles = False
                                xd = 1
        else:
            whiles = False

    return MyPlayer


# def moreOption_link_object(listOfObjects):
#     new_player = 0
#     collid = []
#     for event in pg.event.get():
#         for i, object in enumerate(listOfObjects):
#             # new_player += 1
#
#             if event.type == pg.MOUSEBUTTONDOWN and p==0:
#                 if object.rect.collidepoint(
#                         event.pos) and event.button == 2:  # przesuwanie obiektem przy pomocy lewego przycisku myszy
#                     print("xDD",i)
#                     return i
#
#
#             elif event.type == pg.QUIT:  # wyłączanie programu
#                 pg.quit();
#                 sys.exit()
#     return 0


def collsionWithBorder(object, event, ):
    if object.rect.collidepoint(event.pos) and event.pos[0] > (Screen.get_width() // (10) * 8):
        object.rect.move_ip(0, 0)
        object.rect.move_ip(-310, 0)


def game_event_loop_withPlayer(listOfObjects):
    new_player = 0
    collid = []
    for event in pg.event.get():
        for i, object in enumerate(listOfObjects):
            # Obługa nachodzących na siebie obiektów
            for object2 in listOfObjects:
                if object2.get_position() == object.get_position() and object2 != object:
                    object2.rect.move_ip(0, -10)
                    object.rect.move_ip(100, 10)  # Automatyczne przesunięcie obiektu o sto pikseli w prawo
            if event.type == pg.MOUSEBUTTONDOWN:
                collsionWithBorder(object, event)
                if object.rect.collidepoint(
                        event.pos) and event.button == 1:  # przesuwanie obiektem przy pomocy lewego przycisku myszy
                    object.click = True
                elif object.rect.collidepoint(
                        event.pos) and event.button == 3 and link == 0:  # włączanie większej liczby opcji po naciśnieciu prawego przycisku
                    moreOption_edit_object(listOfObjects, i, event)

                    break
                elif event.button == 3 and not object.rect.collidepoint(
                        event.pos) and link == 0:  # dodawanie nowych obiektów na polu
                    for ii, ob in enumerate(
                            listOfObjects):  # Niestety z jakiegoś powodu powyższy elif nie zawsze działa dlatego tu należy iterować ponownie aby działały ustawienia dla pozostałych obiektów
                        if object in listOfObjects and ob.rect.collidepoint(event.pos):
                            moreOption_edit_object(listOfObjects, ii, event)
                            break
                    moreOption(listOfObjects)  # dodaj nowy obiekt
                    break
            elif event.type == pg.MOUSEBUTTONUP:
                collsionWithBorder(object, event)
                object.click = False
            elif event.type == pg.QUIT:  # wyłączanie programu
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
            pg.quit();
            sys.exit()


def screenDivide():
    width = Screen.get_width() // (10) * 8
    height = Screen.get_height()
    Screen.fill((255, 255, 215), (0, 0, width, height))

    width2 = Screen.get_width() // (10) * 2
    height2 = Screen.get_height()
    Screen.fill((250, 230, 215), (width, 0, width2, height2))
    drawGrid(Screen)


def start():
    MyClock = pg.time.Clock()
    run = 1
    screenDivide()
    drawGrid(Screen)
    pg.display.update()
    obiekty = []

    while run == 1:
        MyClock.tick(66)
        drawGrid(Screen)
        main(Screen, lista_obiektow)
        pygame.time.delay(10)
        pg.display.update()

        output = OutputMessage(Screen)
        xx = output.displayTextAnimation(lista_wiadomosci)
        sleep(0.1)


def instruction():
    HELP = "Aby zbudować nowy obiekt należy użyć prawego przycisku myszy a następnie wybrać typ obiektu. Prawym przyciskiem myszy,\n " \
           "klikniętym na obiekcie można edytować parametru obiektu. Lewy przycisk myszy służy do przemieszczania obiektów"

    menu.add.label(HELP, max_char=-1, font_size=20)


if __name__ == "__main__":
    # os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    Screen = pg.display.set_mode((1600, 1000),pygame.RESIZABLE)
    width = Screen.get_width() // (10) * 8
    height = Screen.get_height()
    Screen2 = pygame.Rect((0, 0), (width, height))
    menu = pygame_menu.Menu('L2TP SYMULATOR', 1598, 998,
                            theme=pygame_menu.themes.THEME_BLUE)

    menu.add.button('Rozpocznij symulacje', start)
    menu.add.button('Instrukcja obsługi', instruction)
    menu.add.button('Wyjśćie', pygame_menu.events.EXIT)
    menu.mainloop(Screen)
