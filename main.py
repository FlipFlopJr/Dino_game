import pygame as pg
import random

pg.init()

SIZE_SCREEN = (600,300)

background = pg.image.load('./background.jpg')

class Sprite(pg.sprite.Sprite):
    def __init__(self, x, y, size, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load(filename), (size, size))
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = [0, 0]

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]


dino = Sprite(50,220,50,'dino2.png')
screen = pg.display.set_mode(SIZE_SCREEN)
pg.display.set_caption('Dino')
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.blit(background,(0,0))
    screen.blit(dino.image,dino.rect)

    pg.display.update()
