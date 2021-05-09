import pygame
import time

screen = pygame.display.set_mode((720, 480))

rect = pygame.Rect((10, 50), (32, 32))
image = pygame.Surface((32, 32))
image.fill((0, 100, 0))

rect2 = pygame.Rect((10, 10), (32, 32))
image2 = pygame.Surface((32, 32))
image2.fill((100, 100, 0))

i = 0
while True:
    i += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.blit(image, rect)
    screen.blit(image2, rect2)
    rect.x += 1  # we update the position every cycle
    rect2.x += 1  # we update the position every cycle

    # but update the rect on screen at different times:
    if i < 10:
        pygame.display.update()  # both
    elif i > 50 and i < 75:
        pygame.display.update(rect2)  # only rect2
    elif i >= 100:
        pygame.display.update(rect)  # only rect

    time.sleep(0.1)