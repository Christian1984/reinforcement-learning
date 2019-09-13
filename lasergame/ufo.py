class Ufo:
    def __init__(self, x = 0.5, y = 0.75, radius = 0.05, velocity = 0.005, hyperdrive_chargerate = 0.001):
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.radius = radius
        self.velocity = velocity

        self.hull_integrity = 1
        self.alive = True
        self.jumped = False

        self.hyperdrive_chargerate = hyperdrive_chargerate
        self.hyperdrive_charge = 0

    def update(self):
        self.hyperdrive_charge += abs(self.hyperdrive_chargerate)
        if (self.hyperdrive_charge >= 1):
            self.jumped = True

        self.x = self.__apply_velocity(self.x, self.target_x)
        self.y = self.__apply_velocity(self.y, self.target_y)
        #TODO: vectorize and normalize
    
    def set_target_pos(self, x, y):
        self.target_x = x
        self.target_y = y

    def receive_damage(self, damage):
        self.hull_integrity -= abs(damage)

        if (self.hull_integrity <= 0):
            self.die()
    
    def die(self):
        self.alive = False
    
    def target_reached(self):
        return self.target_x == self.x and self.target_y == self.y

    def __apply_velocity(self, pos, target_pos):
        if abs(pos - target_pos) < self.velocity:
            return target_pos

        dir = 1 if target_pos > pos else -1
        return pos + dir * self.velocity
