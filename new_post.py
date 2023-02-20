import requests, datetime, glob, schedule
import time, random, os, json
from time import sleep
from auth import token_grup_banner, group_id
from random import randint



def posting_text(folder_path: str) -> str:
    '''
    выбираем среди файлов текст для поста
    '''
    path_text = f'text/{folder_path}/'
    files = os.listdir(path_text)  # Читаем каталог в список
    name_file = randint(1, len(files))  # генерим случайную переменную от 1 до len чтоб выбрать случайный файл

    path_text_file = f'{path_text}{name_file}.txt'  # собираем путь до файла

    with open(path_text_file, 'r', -1, 'utf-8') as file:
        # print(file.read())
        # message_post = file.read()
        return file.read()


def pic_for_post(folder_path):
    pics = glob.glob(f'picturies/{folder_path}/*.jpg')
    pic2post = random.choice(pics)
    return pic2post


def new_post(message_post: str, pic2post):
    url = 'https://api.vk.com/method/photos.getWallUploadServer?group_id=%d&v=5.28&access_token=%s' % (
        group_id, token_grup_banner)

    resp = requests.get(url).json()['response']
    upload_url = resp['upload_url']
    files = {'file1': open(pic2post, 'rb')}
    resp = requests.post(upload_url, files=files)
    resp = resp.json()
    server = resp['server']
    photo = resp['photo']
    vkhash = resp['hash']
    sleep(0.4)
    url = 'https://api.vk.com/method/photos.saveWallPhoto?group_id=%s&server=%s&photo=%s&hash=%s&v=5.28&access_token=%s' % (
        group_id, server, photo, vkhash, token_grup_banner)
    resp = requests.get(url).json()['response']
    print(resp)
    resp = resp[0]
    photo_id = resp['id']
    owner_id = resp['owner_id']
    atts = 'photo%s_%s' % (owner_id, photo_id)
    sleep(0.4)
    url = f'https://api.vk.com/method/wall.post?owner_id={-group_id}&from_group=1&message={message_post}&attachments={atts}&v=5.28&access_token={token_grup_banner}'
    resp = requests.get(url).json()['response']
    files = 0


def main():
    path_pic = pic_for_post('banner')
    text = posting_text('banner')
    new_post(text, path_pic)


if __name__ == '__main__':
    main()
