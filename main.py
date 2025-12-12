import sys
import pygame as pg
import random

pg.init()

width, height = 480, 320
xbox, ybox = 20, 20
startx, starty = width/2, height-ybox
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
main_ship = pg.Rect(startx, starty, xbox, ybox)

## Enemy Box Generation
enemy_fatness = 64
blockX_position = random.randint(0, width - enemy_fatness)
blockY_position = 0 - enemy_fatness
enemy_block = pg.Rect(blockX_position, blockY_position, enemy_fatness, enemy_fatness)

running = True
while running:
 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    ## Inputs
    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        main_ship.x -= 3
        if main_ship.x < 0 : main_ship.x = 0

    if keys[pg.K_RIGHT]:
        main_ship.x += 3
        if main_ship.x > width-xbox : main_ship.x = width-xbox

    ## Enemy Block Movement
    if (enemy_block.y >= height - 0 and 
    enemy_block.y <= (height + enemy_fatness)):
        enemy_block.y = 0 - enemy_fatness
        # randomly assign value in range
        enemy_block.x = random.randint(0, (width - enemy_fatness))
    if True:
        enemy_block.y += 2
    
    ## Collision
    if main_ship.y < (enemy_block.y + enemy_fatness): ## If Ship Y-coordinate within bounds of an enemy block vertically
        if ((main_ship.x > enemy_block.x) 
            and (main_ship.x < (enemy_block.x + enemy_fatness)) 
            or (main_ship.x + xbox) > enemy_block.x
            and (main_ship.x + xbox < enemy_block.x + enemy_fatness)):

            enemy_block.y = height + 1000
    
    if enemy_block.y > 800:
        running = False

    screen.fill((20, 20, 30))
    pg.draw.rect(screen, (80, 80, 80), main_ship)
    pg.draw.rect(screen, (80, 10, 10), enemy_block)

    pg.display.flip()

    clock.tick(60)

# End of Game
pg.quit() 
sys.exit()