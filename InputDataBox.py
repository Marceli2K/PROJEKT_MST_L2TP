import pygame as pg

import sys
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
pc_ipAddress =''
pc_ipMask =''
class InputDataBox:

    def __init__(self, x, y, w, h, text=''):
        self.x =  x
        self.rect = pg.Rect(x, y, w, h)
        self.button = pg.Rect(self.rect.x + 10, 220, 140, 32)
        self.color = pg.Color('lightskyblue3')
        self.text = text
        self.txt_surface = pg.font.Font(None, 32).render(text, True, self.color)
        self.font = pg.font.Font(None, 32)
        self.active = False


    def handle_event(self, event):

        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                FONT = pg.font.SysFont(None, 30)
                self.txt_surface = FONT.render(self.text, True, self.color)
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # gets mouse position
            if self.button.collidepoint(mouse_pos):
                # prints current location of mouse
                done = True
                print('button was pressed at {0}'.format(mouse_pos))
                return done


    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)

        pg.draw.rect(screen, (255, 0, 0), self.button)  # draw button
        screen.blit(self.font.render('Prześlij dane', True, (0, 0, 0)), self.button)

# funkcja definiująca dane wejściowe dla PC
def inputForPC(screen):
    width = screen.get_width() // (10) * 8
    width2 = screen.get_width() // (10) * 2
    height2 = screen.get_height()
    myfont = pg.font.SysFont("Comic Sans MS", 17)

    label1 = myfont.render("Adres IP", 1, (255,233,155))
    input_box1 = InputDataBox(width +10, 90, 140, 32)

    label2 = myfont.render("Maska podsieci", 1, (255,233,155))
    input_box2 = InputDataBox(width +10, 170, 140, 32)

    input_boxes = [input_box1, input_box2]
    done = False
    while not done:


        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                done = box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen.fill((150, 230, 215), (width, 0, width2, height2))

        for box in input_boxes:

            screen.blit(label1, (width + 10, 50, 140, 32))
            screen.blit(label2, (width + 10, 130, 140, 32))
            box.draw(screen)
        # done = drawButton(screen, width)
        pg.display.flip()
        pc_ipAddress= input_box1.text
        pc_ipMask = input_box2.text
    print(pc_ipAddress," :", pc_ipMask )
    return pc_ipAddress,  pc_ipMask;

