import pygame as pg
import math

from lasergame import LaserGame

size = 256
fps = 120

angle = 0

color_bg = (0, 0, 0)
color_go = (0, 255, 0)
color_gui = (255, 0, 0)

def draw_target(surface, pos, radius):
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
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    angle += 2 * math.pi / 360

    if angle > 2 * math.pi:
        angle = 0
    
    clock.tick(fps)

    screen.fill(color_bg)

    target_pos = (int(lasergame.target.x * size), int(lasergame.target.y * size))
    target_radius = int(lasergame.target.radius * size)
    draw_target(screen, target_pos, target_radius)

    lasergun_rotation = lasergame.laser.rotation
    laser_fires = False

    if (laser_fires):
        draw_laserbeam(screen, lasergun_rotation)
    
    draw_lasergun(screen, lasergun_rotation, 10, 20)
    
    fps_gui = font.render("FPS: {}".format(int(clock.get_fps())), True, color_gui)
    screen.blit(fps_gui, (10, 10))
    pg.display.flip()