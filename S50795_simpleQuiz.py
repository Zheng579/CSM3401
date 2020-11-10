class Square:
    side = 1.0
    def __init__(self, side):
        self.side = side
    
    def setSide(self):
        if self.side < 0:
            self.side = 0
        else:
            print(self.side * self.side)

x = Square(3)
x.setSide()