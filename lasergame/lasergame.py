from laser import Laser
from ufo import Ufo
import math

class LaserGame:
    def __init__(self):
        self.won_by_ufo = 0
        self.won_by_laser = 0

        self.reset()
    
    def reset(self):
        self.laser = Laser()
        self.ufo = Ufo()

        self.alpha = 0 #angle between laserbeam and ufo
        self.gamma = 0 #angle between center and left/right end of ufo circle
        self.hit = False
    
    def rotate_laser(self, clockwise):
        self.laser.rotate(clockwise)
    
    def fire_laser(self):
        self.laser.fire()
    
    def set_ufo_target(self, x, y):
        self.ufo.set_target_pos(x, y)

    def update(self):
        self.ufo.update()
        self.laser.update()
        self.__calculate_angles()
        self.hit = self.laser.fires and self.alpha <= self.gamma

        if (self.hit):
            self.ufo.receive_damage(self.laser.power)
        
        if(not self.ufo.alive):
            self.won_by_laser += 1
            self.reset()
        elif(self.ufo.jumped):
            self.won_by_ufo += 1
            self.reset()

    def __calculate_angles(self):
        lx = math.sin(self.laser.rotation)
        ly = -math.cos(self.laser.rotation)

        ltx = self.ufo.x - 0.5
        lty = self.ufo.y - 0.5

        dot = lx * ltx + ly * lty
        det = lx * lty - ly * ltx
        self.alpha = abs(math.atan2(det, dot))

        d = math.sqrt(ltx * ltx + lty * lty)
        self.gamma = math.asin(self.ufo.radius / d)
