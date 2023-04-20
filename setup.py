import os
import subprocess
import shutil
import sys

# File directories and copying params
src_dir = '~\\Documents'
app_name = "APOD-Lockscreen"
copied_files = ["paster.py", "setup.py"]
main_file = "paster.py"

# Windows Tasks Scheduler params
freq = "daily"
time = "06:00"

# Get the path to the Documents folder
docs_path = os.path.expanduser(src_dir)

# Get the path to the current Python interpreter
python_path = sys.executable

# Create a directory called "APOD-Lockscreen" in the Documents folder
app_path = os.path.join(docs_path, app_name)
if not os.path.exists(app_path):
    os.makedirs(app_path)

# Copies the script from the downloaded dir to the app dir
for file in copied_files:
    file_path = os.path.join(app_path, file)
    shutil.copy(file, file_path)

# Creates a batch file for setting up the script in Task Scheduler
main_path = os.path.join(app_path, main_file)
bat_path = os.path.join(app_path, 'task.bat')
with open(bat_path, 'w') as f:
    f.write('"' + str(python_path) + '" "' + main_path + '"\nexit')

# Set the command to create the scheduled task
command = 'schtasks /create /tn "' +str(app_name)+ '" /tr "\''+str(bat_path)+'\' " /sc '+str(freq)+' /st '+str(time)+' '
print(command)

# Run the command in the Windows command prompt
subprocess.call(command, shell=True)
