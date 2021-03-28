import pygame as pg
from Const import figure


pg.init()
figure.screen.fill((255, 255, 255))


figure.drowing_field()
pg.display.update()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()


        elif event.type == pg.MOUSEBUTTONDOWN and figure.flag:
            figure.game_process()
            pg.display.update()