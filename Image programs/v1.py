"""
write a python program togenerate an image of a cat with cheese
"""
from PIL import Image, ImageDraw

# Create a blank image with a white background
width, height = 400, 400
image = Image.new("RGB", (width, height), "white")

# Create a drawing object to draw on the image
draw = ImageDraw.Draw(image)

# Draw a cat shape on the image
cat_x, cat_y = 50, 50
cat_width, cat_height = 300, 300
draw.ellipse((cat_x, cat_y, cat_x + cat_width, cat_y + cat_height), fill="gray")

# Draw the cheese
cheese_x, cheese_y = 150, 150
cheese_width, cheese_height = 100, 100
draw.rectangle(
    (cheese_x, cheese_y, cheese_x + cheese_width, cheese_y + cheese_height),
    fill="yellow",
)

# Save the image
image.save("cat_with_cheese.png")
