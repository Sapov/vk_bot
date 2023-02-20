import posting
import schedule
import datetime, time
from auth import group_id


def main():
    '''Запускает постиг по расписанию указанному ниже'''
    schedule.every().day.at("18:58").do(posting.posting, group_id=group_id, dirs='banner')
    while True:
        schedule.run_pending()
        time.sleep(1)
        data = datetime.datetime.now()

        print('ВРЕМЯ', data)


if __name__ == '__main__':
    main()
