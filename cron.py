import requests
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=615)
def job():
    j=requests.get('https://posta-ke.herokuapp.com/email')
    print(j)

sched.start()
