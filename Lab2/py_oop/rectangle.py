from py_oop.figure import Figure
from py_oop.color import FigureColor
from PIL import Image, ImageDraw

class Rectangle(Figure):
    FigureType = "Прямоугольник"


    def __init__(self, color_param, width_param, height_param):
        self.width = width_param
        self.height = height_param
        self.fc = FigureColor()
        self.fc.colorproperty = color_param

    def square(self):
        return self.width*self.height #Площадь
    
 


    def __repr__(self):
        
        im = Image.new('RGB', (610, 240), (219, 193, 27))

        draw = ImageDraw.Draw(im)
        draw.rectangle((200, 100, 300, 200), fill='blue', outline=(255, 255, 255))

        im.save('rectangle.jpg', quality=95)
        print('test')
        return ('{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            Rectangle.get_figure_type(),
            self.fc.colorproperty,
            self.width,
            self.height,
            self.square()
        ))