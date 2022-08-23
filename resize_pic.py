# ресайз картинок по ширине 510 px
import os
# in terminal run command: pip install pillow
from PIL import Image

# Функция ресайза картинок для постинга в вк
def resize_pic(path_out):
    directory = f'picturies/{path_out}/'
    print("Резайзим картинки для постинга в нужный размер")
    # only one value from three you should set !!!
    resize_in_percent = 0      # percent to resize images in folder
    resize_x_to_min = 510         # min width in pixels to resize images in folder
    resize_y_to_min = 0         # min height in pixels to resize images in folder
    if resize_x_to_min+resize_y_to_min != 0:
        resize_in_percent = False

    with os.scandir(path=directory) as it:
        for entry in it:
            if not entry.is_file():
                print("dir:\t" + entry.name)
            else:
                print("file:\t" + entry.name)
                img_obj = Image.open(directory + entry.name)
                width_size = height_size = 0
                if resize_in_percent:
                    percent = 100 / resize_in_percent
                    width_size = int(float(img_obj.size[0])/percent)
                    height_size = int(float(img_obj.size[1])/percent)
                else:
                    if resize_x_to_min:
                        delta = resize_x_to_min / float(img_obj.size[0])
                        width_size = int(float(img_obj.size[0]) * delta)
                        height_size = int(float(img_obj.size[1]) * delta)
                    else:
                        delta = resize_y_to_min / float(img_obj.size[1])
                        width_size = int(float(img_obj.size[0]) * delta)
                        height_size = int(float(img_obj.size[1]) * delta)
                img_obj = img_obj.resize((width_size, height_size), Image.ANTIALIAS)
                img_obj.save(directory + entry.name)