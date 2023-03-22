import schedule
import time

def job():
    print('I`m working...')

schedule.every().wednesday.at('13:03').do(job)

while True:
    schedule.run_pending()
    time.sleep(1)