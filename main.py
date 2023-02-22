import posting
import schedule
import datetime, time
from auth import group_id
import question
import bot_answer


def main():
    '''Запускает постиг по расписанию указанному ниже'''
    schedule.every().day.at("08:37").do(posting.posting, group_id=group_id, dirs='mobstend')
    schedule.every().day.at("08:38").do(question.question)
    schedule.every().day.at("08:40").do(bot_answer.answer_main)

    schedule.every().day.at("12:00").do(posting.posting, group_id=group_id, dirs='banner')
    schedule.every().day.at("12:30").do(question.question)
    schedule.every().day.at("12:56").do(bot_answer.answer_main)

    schedule.every().day.at("20:00").do(posting.posting, group_id=group_id, dirs='mobstend')
    schedule.every().day.at("20:08").do(question.question)
    schedule.every().day.at("20:40").do(bot_answer.answer_main)

    schedule.every().day.at("16:00").do(posting.posting, group_id=group_id, dirs='banner')
    schedule.every().day.at("16:33").do(question.question)
    schedule.every().day.at("17:01").do(bot_answer.answer_main)

    while True:
        schedule.run_pending()
        time.sleep(1)
        data = datetime.datetime.now()

        print('ВРЕМЯ', data)


if __name__ == '__main__':
    main()
