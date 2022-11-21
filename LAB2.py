from PIL import Image, ImageDraw
img = Image.new('L', (960, 540), 255)
draw = ImageDraw.Draw(img)
with open("DS0.txt", "r") as file:
    for line in file:
        coords=line.split()
        x = int(coords[1])
        y = int(coords[0])
        draw.line((x, y, x + 1, y + 1))
img.show()
img.save('LAB2.png')
