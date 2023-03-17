import csv

def append_new_line(file_path, dict_to_append):
    with open(file_path, 'a') as file_object:
        name = dict_to_append['name']
        email = dict_to_append['email']
        subject = dict_to_append['subject']
        message = dict_to_append['message']
        csv_writer = csv.writer(file_object)
        csv_writer.writerow([name, email, subject, message])