import json
import os
import random
import requests
import vk_api
from auth import token_grup_banner, group_id

session = vk_api.VkApi(token=token_grup_banner)
vk = session.get_api()


def count_files(path_dir: str):
    ''' считаем файлы в директории'''
    list_files = os.listdir(path_dir)  # cмотрим сколько у нас файлов
    return len(list_files)


def text_message(dirs):
    # собираем путь до файла
    name_path_text = f'text/{dirs}/'

    name_file = random.randint(1, count_files(name_path_text)) # выбираем рандомный путь или name_file = randome.choice(count_files(name_path_text))
    text_path = f'{name_path_text}{name_file}.txt'
    with open(text_path, 'r', -1, 'utf-8') as text_file:
        message_post = text_file.read()
        print(message_post)
        return message_post


def pic_post(dirs):
    '''рандомно выбираются фотографии'''

    name_path_text = f'picturies/{dirs}/'
    name_file = random.randint(1, count_files(name_path_text))
    pic_path = f'{name_path_text}{name_file}.jpg'
    print(pic_path)
    return pic_path


def posting(group_id, dirs):
    photo_id = pic_post(dirs)

    # сначала загружаем фотку на сервер методом getWallUploadServer

    upload_url = vk.photos.getWallUploadServer(group_id=group_id)['upload_url']

    request = requests.post(upload_url, files={'photo': open(photo_id, "rb")})
    params = {'server': request.json()['server'],
              'photo': request.json()['photo'],
              'hash': request.json()['hash'],
              'group_id': group_id}
    # сохраняем на сервере
    data = vk.photos.saveWallPhoto(**params)

    photo_id = data[0]['id']

    params = {'attachments': 'photo' + str(data[0]['owner_id']) + '_' + str(photo_id),
              'message': text_message(dirs),
              'owner_id': '-' + str(group_id),
              'from_group': '1'}
    vk.wall.post(**params)


if __name__ == '__main__':
    posting(group_id, 'banner')

