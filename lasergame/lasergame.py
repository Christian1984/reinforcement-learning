from laser import Laser
from target import Target
import math

class LaserGame:
    def __init__(self):
        self.laser = Laser()
        self.target = Target()

        self.alpha = 0 #angle between laserbeam and target
        self.gamma = 0 #angle between center and left/right end of target circle
        self.hit = False

    def update(self):
        self.laser.rotation += 2 * math.pi / 360

        if self.laser.rotation > 2 * math.pi:
            self.laser.rotation = 0

        self.calculate_angles()
        self.hit = self.alpha <= self.gamma
        
    def calculate_angles(self):
        lx = math.sin(self.laser.rotation)
        ly = -math.cos(self.laser.rotation)

        ltx = self.target.x - 0.5
        lty = self.target.y - 0.5

        dot = lx * ltx + ly + lty
        det = lx * lty - ly * ltx
        self.alpha = abs(math.atan2(det, dot))

        d = math.sqrt(ltx * ltx + lty + lty)
        self.gamma = math.asin(self.target.radius / d)
