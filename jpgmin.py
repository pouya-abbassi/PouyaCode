#! python3
# -*- coding: utf-8 -*-

from PIL import Image
import sys

def minify(path):
    old_img = Image.open(path)
    old_img.convert('YCbCr').save(path, 'JPEG')
    old_img.save(''.join(path.split('.')[:-1]) + '.old.jpg', 'JPEG')

if __name__ == '__main__':
    extension = sys.argv[1].split('.')[-1].lower()
    if (extension == 'jpg' or extension == 'jpeg'):
        minify(sys.argv[1])
    else:
        print("Not a jpeg file.")
