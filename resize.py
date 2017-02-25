from PIL import Image
import config
img = Image.open('grayscale.png')

img = img.resize((config.px_x,config.px_y))
img.save('resized_grayscale.png')