'''
APScheduler example with explicit default configuration.
Background scheduler is running an interval job to execute a func every 5 sec.
Main thread is simulated and listener is attached to track scheduler events.
'''

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
import time
from datetime import datetime

# Define dicts for scheduler configuration
jobstores = {'default': {'type': 'memory'}}
executors = {'default': {'type': 'threadpool', 'max_workers': 10}}
job_defaults = {'max_instances': 3}

# Create a new Scheduler instance
scheduler = BackgroundScheduler()


def my_listener(event):
    '''Listens for execution and crash events and logs the message'''
    if event.exception:
        print('The job crashed :( %s' %
              datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    else:
        print('The job worked :) %s' %
              datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def things_todo(text):
    '''Definge the function to execute on the schedule here'''
    print(text)


if __name__ == '__main__':
    # Add listener to log the execution for debugging purposes
    scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

    # Add jobs here and print pending jobs
    scheduler.add_job(lambda: things_todo('Doing a thing'),
                      trigger='interval',
                      seconds=5,
                      timezone='Asia/Tokyo',
                      id='001')
    scheduler.print_jobs()

    # Configure the scheduler
    # After the scheduler has been started, you can no longer alter its settings
    scheduler.configure(jobstores=jobstores,
                        executors=executors,
                        job_defaults=job_defaults)

    # Start the scheduler
    scheduler.start()
    print('Scheduler started')

    # Modify the name of the job and check the updated list
    scheduler.modify_job(job_id='001', name='Reminder')
    scheduler.print_jobs()

    try:
        # This is here to simulate application activity (which keeps the main thread alive)
        while True:
            time.sleep(2)
            print('This is main thread running')
    except (KeyboardInterrupt, SystemExit):
        # Handle keyboard interrupts or system exits by shutting down the scheduler
        print('\nShutting down')
        scheduler.shutdown()
