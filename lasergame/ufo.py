class Ufo:
    def __init__(self, x = 0.5, y = 0.75, radius = 0.05, velocity = 0.01):
        self.x = x
        self.y = y
        self.target_pos_x = x
        self.target_pos_y = y
        self.radius = radius

    def update(self):
        #TODO: move towards ufo until distance < sqrt(2v^2)
        return
    
    def set_target_pos(self, x, y):
        self.target_pos_x = x
        self.target_pos_y = y
