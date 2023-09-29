import pygame as pg
import random
import time

pg.init()

SIZE_SCREEN = (600,300)
result = 0
SPEED = -5

background = pg.image.load('./background.jpg')
clock = pg.time.Clock()

def font():
    font = pg.font.SysFont(None,32)
    text = font.render(f'SCORE: {result}',True,(0,0,0))
    text_rect = text.get_rect(center = (100,50))
    screen.blit(text,text_rect)

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

    def jump(self):
        self.speed[1]-=15

class Dino(Sprite):
    def __init__(self,x,y,size,filename1,filename2,filename3, filename_down):
        Sprite.__init__(self, x, y, size, filename1)

        self.image1 = pg.transform.scale(pg.image.load(filename1), (size, size))
        self.image1.set_colorkey(self.image1.get_at((0,0)))

        self.image2 = pg.transform.scale(pg.image.load(filename2), (size, size))
        self.image2.set_colorkey(self.image1.get_at((0,0)))

        self.image3 = pg.transform.scale(pg.image.load(filename3), (size, size))
        self.image3.set_colorkey(self.image3.get_at((0,0)))

        self.image_down = pg.transform.scale(pg.image.load(filename_down), (size, size))
        self.image_down.set_colorkey(self.image_down.get_at((0,0)))
        self.images = [self.image1,self.image2]

        self.rect = self.image1.get_rect(center=(x, y))
        self.speed = [0, 0]



dino = Dino(55,220,50,'dino1.png', 'dino3.png','dino2.png','image_down.png')
screen = pg.display.set_mode(SIZE_SCREEN)
cactus = Sprite(550,220,50,'cactus.jpg')
pg.display.set_caption('Dino')
ptero = Sprite(550,180,30,'Ptero.png')

cactus.speed[0]=SPEED
ptero.speed[0]=SPEED


running = True
f = 0
flag = False
while running:
    
    if dino.rect.bottom>240:
        dino.speed = [0,0]
    else:
        dino.speed[1]+=1


    if cactus.rect.right<0:
        result+=1
        cactus.rect.left = SIZE_SCREEN[0]
        if result%5==0:
            cactus.speed[0]-= 1

    if ptero.rect.right<0:
        result+=1
        ptero.rect.left = SIZE_SCREEN[0]
        if result%5==0:
            ptero.speed[0]-= 1
    
    if pg.sprite.collide_rect(dino,cactus):
        running = False

    if pg.sprite.collide_rect(dino,ptero):
        running = False

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type==pg.KEYDOWN and dino.rect.bottom==245:
            if event.key == pg.K_SPACE or event.key == pg.K_UP:
                dino.speed[1]-=16
            if event.key == pg.K_DOWN:
                flag = True
            else:
                flag = False

    screen.blit(background,(0,0))
    
 
    if dino.rect.bottom!=245:
        screen.blit(dino.image3,dino.rect)
    elif flag == True:
        screen.blit(dino.image_down,dino.rect)
    else:

        if f<5:
            screen.blit(dino.image1, dino.rect)
            f +=1
        else:
            
            
            screen.blit(dino.image2,dino.rect)
            f+=1
            if f==10:
                f = 0
            
        
    screen.blit(cactus.image,cactus.rect)
    # screen.blit(ptero.image,ptero.rect)
    font()

    cactus.update()
    ptero.update()
    dino.update()
    # print(dino.rect.top,dino.rect.bottom)
    # print(dino.rect.bottom)
    pg.display.update()
    clock.tick(60)
