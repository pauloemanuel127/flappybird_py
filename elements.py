class Bird:

    def __init__(self, pos_y):

        self.pos_y = pos_y
        self.velocity = 0
        self.gravity = 0.1

    def jump(self):

        self.velocity = -6

    def update(self):

        self.velocity += self.gravity
        self.pos_y += self.velocity

class Pipe:

    def __init__(self):

        self.width = 10
        self.speed = 5

class UpperPipe(Pipe):

    def __init__(self, heigth):

        super().__init__()
        self.heigth = heigth

class LowerPipe(Pipe):

    def __init__(self, heigth):

        super().__init__()
        self.heigth = heigth