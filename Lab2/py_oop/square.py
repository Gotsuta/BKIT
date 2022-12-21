from py_oop.rectangle import Rectangle
from PIL import Image, ImageDraw

class Square(Rectangle):
    FigureType = "Квадрат"

    def __init__(self, color_param, side_param):
        self.side = side_param
        super().__init__(color_param, self.side, self.side)

    def __repr__(self):
        return '{} {} цвета со стороной {} площадью {}.'.format(
            Square.get_figure_type(),
            self.fc.colorproperty,
            self.side,
            self.square()
        )

