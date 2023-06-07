import csv
from datetime import datetime, timedelta


with open('a.csv', newline='') as file:
    with open('b.csv', 'w') as file2:
        reader = csv.DictReader(file)
        print('User,Email,Client,Project,Task,Description,Billable,Start date,Start time,Duration,Tags', file=file2)
        for r in reader:
            user = r['User'].strip('\"')
            email = r['Email'].strip('\"')
            client = ''
            project = r['Project'].strip('\"')
            task = ''
            description = r['Description'].strip('\"')
            start_date = '-'.join(reversed(r['Start Date'].split('/')))
            start_time = r['Start Time']
            billable = r['Billable'].strip('\"')
            end_date = '-'.join(reversed(r['End Date'].split('/')))
            end_time =  r['End Time']
            s = datetime.fromisoformat(f'{start_date}T{start_time}')
            e = datetime.fromisoformat(f'{end_date}T{end_time}')
            duration = str(e-s)
            tags = '"' + r['Tags'] + '"'
            print(user, email, client, project, task, description, billable, start_date, start_time, duration, tags, sep=',', file=file2)

