from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from datetime import datetime

# Create a new Scheduler instance
scheduler = BackgroundScheduler()

# Create a new Flask instance
app = Flask(__name__)

# Define dicts for scheduler configuration
jobstores = {'default': {'type': 'memory'}}
executors = {'default': {'type': 'threadpool', 'max_workers': 10}}
job_defaults = {'max_instances': 3}


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


@app.route('/', methods=['GET'])
def home():
    return 'OK'


@app.route('/callback', methods=['POST'])
def callback():
    # curl -X POST -d "name=John&age=30" http://localhost:5000/callback
    name = request.form['name']
    age = request.form['age']
    print(request.headers)
    # do something with name and age...
    return f'Name is {name} and age is {age}\n'


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
        app.run(host='0.0.0.0', port=5000)
    except (KeyboardInterrupt, SystemExit):
        # Handle keyboard interrupts or system exits by shutting down the scheduler
        print('\nShutting down')
        scheduler.shutdown()
