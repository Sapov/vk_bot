import time, random, os
import vk_api
import auth
from time import sleep

id_gruop = 161962808  # groups


# id_gruop = 58479061
# *************************************************************************
def change_token():
    # count = len(auth.tokens_vk)
    # i = random.randint(0,len(auth.tokens_vk)-1)
    # auth.tokens_vk[i]
    return auth.tokens_vk[random.randint(0, len(auth.tokens_vk) - 1)]


def last_post(session):
    posts = session.method("wall.get", {
        "owner_id": -id_gruop,
    })
    last_post = posts["items"][0]['id']  # получаю id последнего поста в группе
    print(f"Последний пост ID-{last_post}")
    return last_post


def like_post(post, session):
    try:
        like = session.method("wall.addLike", {
            "owner_id": -id_gruop,
            "post_id": post
        })
        print('Лайкаем пост №', post, "в группе", -id_gruop)
    except:
        print("Уже есть лайк")


def read_file_to_list():
    # # ***********************читаем вопросы -  все строки из файла в список *************************
    question = []
    if os.path.exists('text/question_banner.txt'):
        f = open('text/question_banner.txt', 'r', encoding='UTF-8')
        for x in f:
            if (len(x.strip()) > 2):
                question.append(x.strip())
        f.close()
    return question


def camment(last_post, question, session ):
    #         """ Камент в группу  """
    camment = session.method("wall.createComment", {
        "owner_id": -id_gruop,
        "post_id": last_post,
        "message": question[random.randint(0, len(question) - 1)]
    })
    print('Пишем Сamment', 'в группе', -id_gruop)


def question():
    token = change_token()
    session = vk_api.VkApi(token=token)
    vk = session.get_api()

    like_post(last_post(session), session)
    camment(last_post(session), read_file_to_list(), session)


if __name__ == '__main__':
    question()
