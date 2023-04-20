'''Example using the json module to read and write JSON data'''
import os

from json_data import rotate_duty

PATENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.dirname(PATENT_DIR) + '/files/data.json'

if __name__ == '__main__':
    rotate_duty(FILE, 'Groceries')