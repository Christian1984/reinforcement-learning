class Ufo:
    def __init__(self, x = 0.5, y = 0.75, radius = 0.05, velocity = 0.01):
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.radius = radius
        self.velocity = velocity

    def update(self):
        self.x = self.__apply_velocity(self.x, self.target_x)
        self.y = self.__apply_velocity(self.y, self.target_y)

        #TODO: normalize
        
        return
    
    def set_target_pos(self, x, y):
        self.target_x = x
        self.target_y = y

    def __apply_velocity(self, pos, target_pos):
        if abs(pos - target_pos) < self.velocity:
            return target_pos

        dir = 1 if target_pos > pos else -1
        return pos + dir * self.velocity
