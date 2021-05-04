# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
import pygame_gui
import os, sys
import pygame as pg  # lazy but responsible (avoid namespace flooding)
from OptionBox import OptionBox as OB


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
        print()

    def update(self, surface):
        if self.click:
            self.rect.center = pg.mouse.get_pos()
        surface.blit(self.image, self.rect)


def main(Surface, Player):
    pygame.display.set_caption('L2TP Projekt')
    if Player == 0:
        game_event_loop_withoutPlayer()
        # Surface.blit(background_image, [0, 0])
        Surface.fill((255, 255, 255))
    else:
        game_event_loop_withPlayer(Player)
        # Surface.blit(background_image, [0, 0])
        Player.update(Surface)


# funkcja dodająca nowe obiekty po wykonaniu opcji prawy klik i wybraniu z menu rodzaju obiektu
def add_new_object(option):
    MyPlayer = Character((0, 0, 75, 75), option)
    MyPlayer.rect.center = Screen.get_rect().center
    MyPlayer.update(Screen)
    return False, MyPlayer


def moreOption():
    mpos = pygame.mouse.get_pos()
    x = mpos[0]
    y = mpos[1]
    menu_obiektow = OB(x, y, 160, 40, (150, 150, 150), (100, 200, 255), pygame.font.SysFont(None, 30),
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
                print("xxx")
                whiles, MyPlayer = add_new_object(selected_option)
        else:
            whiles = False

    return MyPlayer
    # pg.display.update()
    print("out of while")


def game_event_loop_withPlayer(Player):
    new_player = 0
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if Player.rect.collidepoint(event.pos) and event.button == 1:
                Player.click = True
            elif Player.rect.collidepoint(event.pos) and event.button == 3:
                print(event.button)
                new_player = moreOption()
            elif event.button == 3:
                print(event.button, "XXX")
                new_player = moreOption()
        elif event.type == pg.MOUSEBUTTONUP:
            Player.click = False
        elif event.type == pg.QUIT:
            pg.quit();
            sys.exit()
    return new_player

def game_event_loop_withoutPlayer():
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
            print(event.button)
            moreOption()
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            print("xd")
        elif event.type == pg.QUIT:
            pg.quit();
            sys.exit()


if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    Screen = pg.display.set_mode((777, 777))

    background_image = pygame.image.load("grafiki/back.jpg").convert()
    MyPlayer = 0
    MyClock = pg.time.Clock()
    MyPlayer = Character((0, 0, 75, 75), 2)
    MyPlayer.rect.center = Screen.get_rect().center
    run = 1
    Screen.fill((255, 2, 255))
    obiekty =[]
    while run == 1:
        obiekty.append(game_event_loop_withPlayer(MyPlayer))
        main(Screen, MyPlayer)
        pg.display.update()
        MyClock.tick(60)
        print(obiekty)

