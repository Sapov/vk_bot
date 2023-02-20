import requests, datetime, glob, schedule
# import vk_api, time, random, os, json
# from time import sleep
from auth import token_grup_banner
# -*- coding: utf-8 -*-

from random import randint
from question import *
from bot_answer import go_answer


def post_pic_vk(folder_path_text, tema):
    """ проверка по id группы для подстановки пути нужной папки"""

    # #проверка в какую группу писать
    global group_id
    if folder_path_text == "banner" and tema == "banner":
        group_id = 161962808
        folder_path_text = "banner"
        print("номер группы-------", group_id)
    elif folder_path_text == "banner" and tema == "mobstend":
        folder_path_text = "mobstend"
        group_id = 161962808
        print("Постим Моб. стенды в группу", group_id, "меняем путь: ", folder_path_text)
    else:
        if folder_path_text == "oboi" and tema == '1':
            group_id = 58479061
            print("номер группы------", group_id)
    # путь к папке с фотками

    pics = glob.glob(f'picturies/{folder_path_text}/*.jpg')
    if len(pics) == 0:
        print('Нет изображений для постинга')
        exit()
    # --------------------    #будем читать посты из txt файлов

    path_text = f'text/{folder_path_text}/'
    # генерим случайную переенную от 1 до 12 чтоб выбрать случайный файл
    name_fail = randint(1, 12)
    # собираем путь до файла
    fukk_path = f'{path_text}{name_fail}.txt'

    f = open(fukk_path, 'r', -1, 'utf-8')
    # print(f.read())
    message_post = f.read()
    print(message_post)
    f.close()
    pic2post = random.choice(pics)
    url = 'https://api.vk.com/method/photos.getWallUploadServer?group_id=%d&v=5.28&access_token=%s' % (
        group_id, token_grup_banner)
    print(pic2post)
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
    resp = resp[0]
    photo_id = resp['id']
    owner_id = resp['owner_id']
    atts = 'photo%s_%s' % (owner_id, photo_id)
    print(atts)
    print(photo_id)
    sleep(0.4)
    # url = 'https://api.vk.com/method/wall.post?owner_id=%s&from_group=1&attachments=%s&v=5.28&access_token=%s' % (
    url = 'https://api.vk.com/method/wall.post?owner_id=%s&from_group=1&message=%s&attachments=%s&v=5.28&access_token=%s' % (
        -group_id, message_post, atts, token_grup_banner)
    resp = requests.get(url).json()['response']
    files = 0
    # os.remove(pic2post) # раньше удалял файлы изображений и искал другие, теперь просто добавляю новые в новый пост выбираем рандомно


post_pic_vk(folder_path_text = "banner", tema = 'banner')
#
# def job():
#     schedule.every().day.at("08:12").do(post_pic_vk, folder_path_text = "oboi", tema = '1')
#
#     schedule.every().day.at("01:45").do(post_pic_vk, folder_path_text = "banner", tema = 'mobstend')
#     schedule.every().day.at("09:39").do(main)
#     schedule.every().day.at("09:58").do(go_answer)
#
#     schedule.every().day.at("10:53").do(post_pic_vk, folder_path_text = "oboi", tema = '1')
#
#     schedule.every().day.at("10:10").do(post_pic_vk, folder_path_text = "banner", tema = 'banner')
#     schedule.every().day.at("10:13").do(main)
#     schedule.every().day.at("10:17").do(go_answer)
#
#
#     schedule.every().day.at("11:50").do(post_pic_vk, folder_path_text = "oboi", tema = '1')
#
#     schedule.every().day.at("22:43").do(post_pic_vk, folder_path_text = "banner", tema = 'banner')
#     schedule.every().day.at("22:45").do(main)
#     schedule.every().day.at("11:22").do(go_answer)
#
#     schedule.every().day.at("13:05").do(post_pic_vk, folder_path_text = "banner", tema = 'banner')
#     schedule.every().day.at("13:12").do(main)
#     schedule.every().day.at("13:22").do(go_answer)
#
#     schedule.every().day.at("15:05").do(post_pic_vk, folder_path_text = "banner", tema = 'banner')
#     schedule.every().day.at("16:35").do(main)
#     schedule.every().day.at("16:40").do(go_answer)
#
#     schedule.every().day.at("14:15").do(post_pic_vk, folder_path_text = "oboi", tema = '1')
#
#     schedule.every().day.at("19:20").do(post_pic_vk, folder_path_text = "banner", tema='mobstend')
#     schedule.every().day.at("20:25").do(main)
#     schedule.every().day.at("20:30").do(go_answer)
#
#     schedule.every().day.at("23:25").do(post_pic_vk, folder_path_text = "banner", tema = 'banner')
#     schedule.every().day.at("23:40").do(main)
#     schedule.every().day.at("23:41").do(go_answer)
#
#     schedule.every().day.at("18:35").do(post_pic_vk, folder_path_text = "oboi", tema = '1')
#     schedule.every().day.at("21:22").do(post_pic_vk, folder_path_text = "oboi", tema = '1')
#     schedule.every().day.at("16:34").do(post_pic_vk, folder_path_text = "oboi", tema = '1')
#
#     text = "-------------------------Пост!! ----------- в  "
#     data = datetime.datetime.now()
#     print(text, data)
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
#         data = datetime.datetime.now()
#
#         print('каждую сек __::__', data)
# job()
