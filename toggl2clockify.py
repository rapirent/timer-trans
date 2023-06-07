import csv
from datetime import datetime, timedelta


with open('a.csv', newline='') as file:
    with open('b.csv', 'w') as file2:
        reader = csv.DictReader(file)
        print('Project,Client,Description,Task,Email,Tags,Billable,Start Date,Start Time,Duration (h)', file=file2)
        for r in reader:
            user = r['\ufeffUser']
            email = r['Email']
            client = ''
            project = r['Project']
            task = ''
            description = r['Description']
            start_date = '/'.join(reversed(r['Start date'].split('-')))
            start_time = r['Start time']
            billable = r['Billable']
            duration = r['Duration']
            tags = '"' + r['Tags'] + '"'
            print(project, client, description, task, email, tags, billable, start_date, start_time, duration, sep=',', file=file2)

