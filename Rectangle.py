from Point import Point


class Rectangle:
    def __init__(self, xCord, yCord, width, height, XO):
        self.upperLeftPoint = Point(xCord, yCord)
        self.width = width
        self.height = height
        self.inside = XO

    def is_inside_rectangle(self, xCord, yCord):
        if self.upperLeftPoint.xCord < xCord < (self.upperLeftPoint.xCord + self.width) and self.upperLeftPoint.yCord < yCord < (self.upperLeftPoint.yCord + self.height):
            return True
        return False

    def img_place(self):
        x = self.upperLeftPoint.xCord + (self.width / 4)
        y = self.upperLeftPoint.yCord + (self.height / 4)
        return x, y

    def x_inside(self):
        self.inside = 'x'

    def o_inside(self):
        self.inside = 'o'



