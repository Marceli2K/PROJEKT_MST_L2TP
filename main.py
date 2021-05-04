# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame

import os,sys
import pygame as pg #lazy but responsible (avoid namespace flooding)

class Character:
    def __init__(self,rect):
        pc = pygame.image.load("grafiki/pc.png")
        self.rect = pg.Rect(rect)
        self.click = False
        self.image = pg.Surface(self.rect.size).convert()
        #self.image.fill((255,0,0))

        #var = pc.size.convert()
        self.image.blit(pc, (0,0))

    def update(self,surface):
        if self.click:
            self.rect.center = pg.mouse.get_pos()
        surface.blit(self.image,self.rect)

def main(Surface,Player):
    pygame.display.set_caption('L2TP Projekt')
    game_event_loop(Player)
    Surface.blit(background_image, [0, 0])
    Player.update(Surface)


def game_event_loop(Player):
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN :
            if Player.rect.collidepoint(event.pos) and event.button ==1:
                Player.click = True
            elif Player.rect.collidepoint(event.pos) and event.button == 3:
                print(event.button)
        elif event.type == pg.MOUSEBUTTONUP:
            Player.click = False
        elif event.type == pg.QUIT:
            pg.quit(); sys.exit()

if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    Screen = pg.display.set_mode((777,777))
    background_image = pygame.image.load("grafiki/back.jpg").convert()

    MyClock = pg.time.Clock()
    MyPlayer = Character((0,0,75,75))
    MyPlayer.rect.center = Screen.get_rect().center
    run = 1
    while run == 1:

        main(Screen,MyPlayer)
        pg.display.update()
        MyClock.tick(666)