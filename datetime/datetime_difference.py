from datetime import datetime

def time_difference(start_time: object, end_time: object) -> tuple:
    '''Return the time difference between two dates in weeks and months'''
    difference = end_time - start_time
    weeks = difference.days // 7
    months = difference.days // 30
    return weeks, months

data = {"updated": ""}

current = datetime.now()
data['updated'] = str(current)
print(data)
last = '2023-03-27 22:29:25.312117'
datetime_obj = datetime.strptime(last, '%Y-%m-%d %H:%M:%S.%f')
weeks, months = time_difference(datetime_obj, current)
print(weeks, months)
