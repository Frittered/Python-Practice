import os
from PIL import Image
#import sys

'''
This is a program that converts jpg images into png thumbnails to make a repository of images with manageable sizes.
It will have to command line arguments: python3 image_converter.py x y
where x will be the source path and y will be the output path, which will or will not already exist.
'''
old_folder = 'C:\\Users\\fritz\\Desktop\\python_image_test'
new_folder = 'C:\\Users\\fritz\\Desktop\\New_Folder'

#old_folder will be sys.argv[1]
#new_folder will be sys.argv[2]


image_list = os.listdir(path=(old_folder))


if not os.path.exists('C:\\Users\\fritz\\Desktop\\New_Folder'):
    os.mkdir('C:\\Users\\fritz\\Desktop\\New_Folder')


for image in image_list:
    if image.endswith('.jpg')
      img = Image.open(old_folder+'\\'+image)
      img.thumbnail((400,400))
      image.replace('jpg','png')
      img.save(f'C:\\Users\\fritz\\Desktop\\New_Folder\\{image}', 'png')
