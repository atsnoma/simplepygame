import sys
import pygame as pg

pg.init()

width, height = 480, 320
xbox, ybox = 20, 20
startx, starty = width/2, height/2
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
main_ship = pg.Rect(startx, starty, xbox, ybox)
running = True
while running:
 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        main_ship.x -= 3
        if main_ship.x < 0 : main_ship.x = 0

    if keys[pg.K_RIGHT]:
        main_ship.x += 3
        if main_ship.x > width-xbox : main_ship.x = width-xbox

    screen.fill((20, 20, 30))
    pg.draw.rect(screen, (80, 80, 80), main_ship)

    pg.display.flip()

    clock.tick(60)

# End of Game
pg.quit() 
sys.exit()