import os, datetime, time
from fuzzywuzzy import fuzz
""" ******************* Бот будет читать каменты под постами и отвечать на них ***********************"""
id_gruop = 161962808
import vk_api
from auth import token_grup_banner
session  = vk_api.VkApi(token=token_grup_banner)

def last_post():
    posts = session.method("wall.get", {
            "owner_id": -id_gruop,
        })
    last_post = posts["items"][0]['id']  # получаю id последнего поста в группе
   # print(f"Последний пост ID-{last_post}")
    return last_post


def read_post(last_post=last_post()):
    posts = session.method("wall.getComments", {
    "owner_id": -id_gruop,
    "post_id": last_post,
              })
    # print(posts)
    # print(posts['items'])
    # print(len(posts['items'][0]))
      # '''Читаем посты '''
    # for i in range(len(posts['items'])):
    #     print ( f"{posts['items'][i]['text']}  : id-{posts['items'][i]['id']}")
    try:
        text = f"{posts['items'][0]['text']}"
        print('Читаем оставленный пользователем пост: ', text)
        return f"{posts['items'][0]['text']}"
    except:
         print("Нет каментов к посту")

def load_file_t_list():
    # """# Загружаем список фраз и ответов в массив """

    mas = []
    if os.path.exists('/home/sasha/vk_bot/text/answer_banner.txt'):
        f = open('/home/sasha/vk_bot/text/answer_banner.txt', 'r', encoding='UTF-8')
        for x in f:
            if (len(x.strip()) > 2):
                mas.append(x.strip().lower())
        f.close()
        return mas

#  # С помощью fuzzywuzzy вычисляем наиболее похожую фразу и выдаем в качестве ответа следующий элемент списка
#
def answer(text,mas):
    try:
        text = text.lower().strip()

        if os.path.exists('/home/sasha/vk_bot/text/answer_banner.txt'):
            a = 0
            n = 0
            nn = 0
            for q in mas:
                if('u: ' in q):
                    # С помощью fuzzywuzzy получаем, насколько похожи две строки
                    aa=(fuzz.token_sort_ratio(q.replace('u: ',''), text))
                    if(aa > a and aa!= a):
                        a = aa
                        nn = n
                n = n + 1
            s = mas[nn + 1]
            print('выбрали ответ для пользователя: ', s)

            return s
        else:
            return 'Ошибка'
    except:
        return 'Ошибка'



#     #""" пишем ответ к каменту"""
def post_recamment(s, id_gruop, last_post):
    print('Постим ответ: ', s, 'в группу', id_gruop, "к посту", last_post)
    camment = session.method("wall.createComment", {
        "owner_id": -id_gruop,
        "post_id": last_post,
        "from_group": id_gruop,
        "message": s,
        "guid": 'posts'
    })
def go_answer():
    mas = load_file_t_list()
    text = read_post(last_post=last_post())
    s=answer(text,mas)
    post_recamment(s, id_gruop=id_gruop,last_post=last_post())
go_answer()