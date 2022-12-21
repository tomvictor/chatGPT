"""
Q: improve the code with python functions
Ans :
Here is a revised version of the program that uses functions
to make the code more modular and easier to understand:
"""
from PIL import Image, ImageDraw


def create_blank_image(width, height, background_color):
    """
    Creates a blank image with the specified width, height, and background color.
    """
    image = Image.new("RGB", (width, height), background_color)
    return image


def draw_shape(draw, shape, x, y, width, height, fill_color):
    """
    Draws the specified shape on the draw object at the specified position and with the specified size and fill color.
    """
    if shape == "rectangle":
        draw.rectangle((x, y, x + width, y + height), fill=fill_color)
    elif shape == "ellipse":
        draw.ellipse((x, y, x + width, y + height), fill=fill_color)


def draw_cat_with_cheese(image, width, height):
    """
    Draws a cat with cheese on the specified image.
    """
    # Create a drawing object to draw on the image
    draw = ImageDraw.Draw(image)

    # Draw a cat shape on the image
    cat_x, cat_y = 50, 50
    cat_width, cat_height = 300, 300
    draw_shape(draw, "ellipse", cat_x, cat_y, cat_width, cat_height, "gray")

    # Draw the cheese
    cheese_x, cheese_y = 150, 150
    cheese_width, cheese_height = 100, 100
    draw_shape(
        draw, "rectangle", cheese_x, cheese_y, cheese_width, cheese_height, "yellow"
    )



if __name__ == "__main__":
    # Create a blank image with a white background
    width, height = 400, 400
    image = create_blank_image(width, height, "white")

    # Draw the cat with cheese on the image
    draw_cat_with_cheese(image, width, height)

    # Save the image
    image.save("cat_with_cheese.png")