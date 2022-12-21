from py_oop.figure import Figure
from py_oop.color import FigureColor
from PIL import Image, ImageDraw
import math

class Circle(Figure):
    FigureType = "Круг"


    def __init__(self, color_param, r_param):
        self.r = r_param
        self.fc = FigureColor()
        self.fc.colorproperty = color_param
    
    def square(self):
        return math.pi * (self.r ** 2)

    def __repr__(self):
        im1 = Image.new('RGB', (610, 240), (219, 193, 27))

        draw = ImageDraw.Draw(im1)
        draw.ellipse((100, 100, 200, 200), fill='green', outline=(0, 0, 0))

        im1.save('cicle.jpg', quality=95)
        return '{} {} цвета радиусом {} площадью {}.'.format(
            Circle.get_figure_type(),
            self.fc.colorproperty,
            self.r,
            self.square()
        )

