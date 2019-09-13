import pygame as pg
import math
from helper import *

from lasergame import LaserGame

size = 256
fps = 120

angle = 0

color_bg = (0, 0, 0)
color_go = (0, 255, 0)
color_gui = (255, 0, 0)

def draw_ufo(surface, pos, radius):
    pg.draw.circle(surface, color_go, pos, radius)

def draw_lasergun(surface, angle, gun_width, gun_length):
    offset = pg.math.Vector2(0.5 * size, 0.5 * size)
    angle_deg = 360 * angle / (2 * math.pi)

    p1 = pg.math.Vector2(0, - 0.5 * gun_length).rotate(angle_deg) + offset
    p2 = pg.math.Vector2(- 0.5 * gun_width, 0.5 * gun_length).rotate(angle_deg) + offset
    p3 = pg.math.Vector2(0.5 * gun_width, 0.5 * gun_length).rotate(angle_deg) + offset

    pg.draw.polygon(surface, color_go, (p1, p2, p3))

def draw_laserbeam(surface, angle):
    pg.draw.line(screen, color_go, 
        (size / 2, size / 2), ((math.sin(angle) + 0.5) * size, 
        (math.cos(angle + math.pi) + 0.5) * size))

pg.init()

clock = pg.time.Clock()

screen = pg.display.set_mode((size, size))
font = pg.font.Font(None, 20)

lasergame = LaserGame()

while True:
    clock.tick(fps)

    #catch and process input
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        #elif event.type == pg.KEYDOWN:
        #    if event.key == pg.K_LEFT:
        #        lasergame.rotate_laser(False)
        #    if event.key == pg.K_RIGHT:
        #        lasergame.rotate_laser(True)

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        lasergame.rotate_laser(False)
    if keys[pg.K_RIGHT]:
        lasergame.rotate_laser(True)
    if keys[pg.K_SPACE]:
        lasergame.fire_laser()
    

    #update internal game logic
    lasergame.update()

    #render
    screen.fill(color_bg)

    ufo_pos = (int(lasergame.ufo.x * size), int(lasergame.ufo.y * size))
    ufo_radius = int(lasergame.ufo.radius * size)
    draw_ufo(screen, ufo_pos, ufo_radius)

    lasergun_rotation = lasergame.laser.rotation
    laser_fires = lasergame.laser.fires

    if (laser_fires):
        draw_laserbeam(screen, lasergun_rotation)
    
    draw_lasergun(screen, lasergun_rotation, 10, 20)
    
    fps_gui = font.render("FPS: {}".format(int(clock.get_fps())), True, color_gui)
    screen.blit(fps_gui, (10, 10))

    debug_gui = font.render("alpha: {}, gamma: {}, energy: {}%{}".format(
            int(rads_to_degs(lasergame.alpha)), 
            int(rads_to_degs(lasergame.gamma)),
            int(lasergame.laser.energy * 100),
            ", HIT" if lasergame.hit else ""),
        True, color_gui)
    screen.blit(debug_gui, (10, 236))
    pg.display.flip()