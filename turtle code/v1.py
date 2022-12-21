import turtle

# Parent class for basic shapes
class Shape:
    def __init__(self, color='black'):
        self.color = color

    def draw(self):
        raise NotImplementedError("Subclass must implement this method")

# Circle class
class Circle(Shape):
    def __init__(self, radius, color='black'):
        super().__init__(color)
        self.radius = radius

    def draw(self):
        turtle.color(self.color)
        turtle.circle(self.radius)

# Line class
class Line(Shape):
    def __init__(self, x1, y1, x2, y2, color='black'):
        super().__init__(color)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        turtle.color(self.color)
        turtle.penup()
        turtle.goto(self.x1, self.y1)
        turtle.pendown()
        turtle.goto(self.x2, self.y2)

# Rectangle class
class Rectangle(Shape):
    def __init__(self, x, y, width, height, color='black'):
        super().__init__(color)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        turtle.color(self.color)
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(self.width)
            turtle.right(90)
            turtle.forward(self.height)
            turtle.right(90)
        turtle.end_fill()

# Triangle class
class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3, color='black'):
        super().__init__(color)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def draw(self):
        turtle.color(self.color)
        turtle.penup()
        turtle.goto(self.x1, self.y1)
        turtle.pendown()
        turtle.begin_fill()
        turtle.goto(self.x2, self.y2)
        turtle.goto(self.x3, self.y3)
        turtle.goto(self.x1, self.y1)
        turtle.end_fill()

# Ellipse class
class Ellipse(Shape):
    def __init__(self, x, y, width, height, color='black'):
        super().__init__(color)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        turtle.color(self.color)
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(self.width)
            turtle.left(45)
            turtle.forward(self.height)
            turtle.left(45)
        turtle.end_fill()

# Create a list of shapes to draw
shapes = [Circle(50), Line(-100, 0, 100, 0), Rectangle(-50, -50, 100, 100), Triangle(-50, 50, 0, -50, 50, 50), Ellipse(0, 0, 100, 50)]

# Loop through the list of shapes and draw them
for shape in shapes:
    shape.draw()

turtle.done()
