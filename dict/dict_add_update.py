from random import randint

dict1 = {}

def func():
    global dict1
    for key in range(5):
        value = [randint(10, 99)]
        print(value)
        # adding new
        dict1.update({key: value})
        print(dict1)
    # updating
    dict1[1] = dict1[1] + [50]
    dict1[1] = dict1[1] + [52]


func()
print(dict1)

