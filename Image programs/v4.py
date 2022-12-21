from PIL import Image, ImageDraw

class Shape:
  """
  A base class for shapes that can be drawn on an image.
  """
  def __init__(self, x, y, width, height, fill_color):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.fill_color = fill_color

  def draw(self, draw):
    """
    Draws the shape on the specified draw object.
    """
    raise NotImplementedError

class Rectangle(Shape):
  """
  A class for drawing rectangles on an image.
  """
  def draw(self, draw):
    draw.rectangle((self.x, self.y, self.x + self.width, self.y + self.height), fill=self.fill_color)

class Ellipse(Shape):
  """
  A class for drawing ellipses on an image.
  """
  def draw(self, draw):
    draw.ellipse((self.x, self.y, self.x + self.width, self.y + self.height), fill=self.fill_color)

class ImageGenerator:
  """
  A class for generating an image of a cat with cheese.
  """
  def __init__(self, width, height, background_color):
    self.width = width
    self.height = height
    self.background_color = background_color
    self.shapes = []

  def create_blank_image(self):
    """
    Creates a blank image with the specified width, height, and background color.
    """
    image = Image.new('RGB', (self.width, self.height), self.background_color)
    return image

  def draw_cat_with_cheese(self):
    """
    Draws a cat with cheese on the image.
    """
    # Create the cat body and cheese shapes
    self.shapes.append(Ellipse(50, 50, 300, 300, 'gray'))
    self.shapes.append(Rectangle(150, 150, 100, 100, 'yellow'))

    # Create the eyes
    eye_radius = 20
    self.shapes.append(Ellipse(120 - eye_radius, 80 - eye_radius, 2 * eye_radius, 2 * eye_radius, 'white'))
    self.shapes.append(Ellipse(260 - eye_radius, 80 - eye_radius, 2 * eye_radius, 2 * eye_radius, 'white'))

    # Create the pupils
    pupil_radius = 10
    self.shapes.append(Ellipse(120 - pupil_radius, 80 - pupil_radius, 2 * pupil_radius, 2 * pupil_radius, 'black'))
    self.shapes.append(Ellipse(260 - pupil_radius, 80 - pupil_radius, 2 * pupil_radius, 2 * pupil_radius, 'black'))

    # Create the mouth
    self.shapes.append(Line(150, 180, 250, 180, 'black', 5))

    # Create the teeth
    tooth_spacing = 15
    for i in range(4):
      tooth_x = 150 + (2 * i + 1) * tooth_spacing
      self.shapes.append(Line(tooth_x, 170, tooth_x, 190, 'white', 5))

    # Create the tail
    self.shapes.append(Line(350, 150, 375, 300, 'gray', 5))
    self.shapes.append(Line(375, 300, 350, 250, 'gray', 5))
    self.shapes.append(Line(375, 300, 400, 250, 'gray', 5))

