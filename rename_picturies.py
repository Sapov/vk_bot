import os

path_pic = 'picturies/mobstend'
list_files = os.listdir(path_pic)
print(list_files)
ext ='jpg'
for i in range(len(list_files)):
    if list_files[i].endswith('jpg'):
        # os.rename(list_files[i], f'{i}.{ext}')
        os.rename(f'{path_pic}/{list_files[i]}', f'{path_pic}/{i}.{ext}')

        print(list_files[i])
