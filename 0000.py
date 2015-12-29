# -*- coding = utf=8 -*-
'the first exercise'

__author__ = mark

from PIL import Image

im = open('sec.jpg')
w,h = im.size
print('Original image size: %s%s' % (w, h))

im.rotate(45).show()
