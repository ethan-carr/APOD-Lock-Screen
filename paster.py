import os
import datetime


# Get the current date and time
current_time = datetime.datetime.now()

# Format the current date and time
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

docs_path = os.path.expanduser('~\\Documents')
app_path = os.path.join(docs_path, 'APOD-Lockscreen')

log_path = os.path.join(app_path, 'log.txt')
with open(log_path, 'w') as f:
    f.write(formatted_time)