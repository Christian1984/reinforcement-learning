import pygame as pg
import math

width = 256
height = 256
fps = 120

angle = 0

color_bg = (0, 0, 0)
color_go = (0, 255, 0)
color_gui = (255, 0, 0)

def draw_target(surface, pos, radius):
    pg.draw.circle(surface, color_go, pos, radius)

def draw_lasergun(surface, angle, gun_width, gun_length):
    p1 = pg.math.Vector2(0.5 * width, 0.5 * (height - gun_length))
    p2 = pg.math.Vector2(0.5 * (width - gun_width), 0.5 * (height + gun_length))
    p3 = pg.math.Vector2(0.5 * (width + gun_width), 0.5 * (height + gun_length))

    pg.draw.polygon(surface, color_go, (p1, p2, p3))

def draw_laserbeam(surface, angle):
    pg.draw.line(screen, color_go, 
        (width / 2, height / 2), ((math.sin(angle) + 0.5) * width, 
        (math.cos(angle + math.pi) + 0.5) * height))

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

    screen.fill(color_bg)

    target_pos = (int(0.5 * width), int(0.75 * height))
    draw_target(screen, target_pos, 10)

    lasergun_angle = angle
    laser_fires = True

    if (laser_fires):
        draw_laserbeam(screen, lasergun_angle)
    
    draw_lasergun(screen, lasergun_angle, 10, 20)
    
    fps_gui = font.render("FPS: {}".format(int(clock.get_fps())), True, color_gui)
    screen.blit(fps_gui, (10, 10))
    pg.display.flip()