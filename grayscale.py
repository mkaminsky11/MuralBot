from PIL import Image
img = Image.open('yellow_smile.jpg').convert('LA')
img.save('greyscale.png')