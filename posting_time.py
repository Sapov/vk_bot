import requests, datetime, glob, schedule, time
from new_post import main


def job():
    schedule.every().day.at("01:03").do(main)

    schedule.every().day.at("22:55").do(main)
    schedule.every().day.at("11:34").do(main)



    while True:
        schedule.run_pending()
        time.sleep(1)
        data = datetime.datetime.now()

        print('каждую сек 00__::__00', data)


if __name__ == '__main__':
    job()
