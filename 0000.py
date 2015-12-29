# -*- coding = utf=8 -*-
'the first exercise'

__author__ = 'mark'

from PIL import Image, ImageDraw, ImageFont

def add_num():
	#打开图片
	im = Image.open('sex.jpg')
	draw = ImageDraw.Draw(im)

	#设定图片上要写的字体
	myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf',size = 40)
	fillcolor = '#ff0000'


	width, heigh = im.size
	draw.text((width-40, 50), '99', font = myfont, fill=fillcolor)
	im.save('sex01.jpg', 'jpeg')

if __name__=='__main__':
	add_num()
