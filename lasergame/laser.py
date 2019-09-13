import math
from helper import *

class Laser:
    def __init__(self, initial_rotation = 0, rotation_velocity = 6 * math.pi / 360,
        energy_depletion = 0.05, energy_recharge = 0.025, power = 0.02):
        self.rotation = initial_rotation
        self.rotation_velocity = rotation_velocity

        self.power = power
        self.energy = 1
        self.energy_depletion = energy_depletion
        self.energy_recharge = energy_recharge
        self.recharges = False
        self.fires = False
    
    def update(self):
        if self.recharges:
            self.fires = False
            self.energy += self.energy_recharge

            if self.energy >= 1:
                self.recharges = False

        elif self.energy > 0 and self.fires:
            self.energy -= self.energy_depletion

            if self.energy <= 0:
                self.fires = False
                self.recharges = True
        
        self.energy = clamp(self.energy, 0, 1)
    
    def rotate(self, clockwise):
        self.rotation += self.rotation_velocity if clockwise else -self.rotation_velocity
        self.rotation = clamp_angle(self.rotation)

    def fire(self):
        if self.energy > 0 and not self.recharges:
            self.fires = True