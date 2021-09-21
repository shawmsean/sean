# -*- coding:utf-8 -*-
import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler

def timedTask():
    print('Hello, the time is %s'%datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

if __name__ == '__main__':
    timedTask()
    scheduler = BackgroundScheduler()
    scheduler.add_job(timedTask,'interval',seconds = 10)
    scheduler.start()
    while True:
        # timedTask()
        print(time.time())
        time.sleep(3)

        

