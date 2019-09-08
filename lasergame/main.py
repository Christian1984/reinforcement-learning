import pygame as pg
import math

width = 256
height = 256
fps = 120

angle = 0

pg.init()

clock = pg.time.Clock()

screen = pg.display.set_mode((width, height))
font = pg.font.Font(None, 20)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    angle += 2 * math.pi / 360

    if angle > 2 * math.pi:
        angle = 0
    
    clock.tick(fps)

    screen.fill((0, 0, 0))
    pg.draw.line(screen, (0, 255, 0), 
        (width / 2, height / 2), ((math.sin(angle) + 1) * width / 2, 
        (math.cos(angle + math.pi) + 1) * height / 2))
    
    fps_gui = font.render(str(int(clock.get_fps())), True, (255, 255, 255))
    screen.blit(fps_gui, (10, 10))
    pg.display.flip()