from PIL import Image
import config

img = Image.open('resized_grayscale.png').convert('RGB')

test_text = []
for y in range(0,config.px_y):
	line_text = ""
	for x in range(0,config.px_x):
		px = img.getpixel((x,y))
		val = 0
		if px[0] == px[1] and px[0] == px[2]:
			# alright, all rgb
			val = px[0]
		if val < 125:
			line_text = line_text + "@"
		else:
			line_text = line_text + " "

	test_text.append(line_text)
print("\n".join(test_text))