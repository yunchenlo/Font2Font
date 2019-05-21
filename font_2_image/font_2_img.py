#!/usr/bin/python3
# Write words to an image with certain font
# Jerry ZJ, May, 22, 2019

from PIL import Image, ImageDraw, ImageFont

font_path = '/home/jerry/Downloads/Fonts/PingFang/PingFangTC-Regular#1.otf'
font_size = 20
White = (255,255,255)
Black = (0,0,0)
# Load font
img = Image.new('RGB', (500,500), color = White)
my_font = ImageFont.truetype(font_path, font_size)
# Write to image
start_pos = (20, 20)
my_str = "測試"
draw = ImageDraw.Draw(img)
draw.text(start_pos, my_str, font = my_font, fill = Black)
# Save file
img.save('test.png')
