import os
import subprocess
import shutil
import sys

# File directories and copying params
src_dir = '~\\Documents'
app_name = "APOD-Lockscreen"
copied_files = ["APOD.py", "setup.py", "log_functions.py", "usage.txt"]
main_file = "APOD.py"

# Windows Tasks Scheduler params
freq = "hourly /mo 2"
time = "05:58"
time2 = "06:00"
img_name = "img.jpg"

# Get the path to the Documents folder
docs_path = os.path.expanduser(src_dir)

# Get the path to the current Python interpreter
python_path = sys.executable

# Create a directory called "APOD-Lockscreen" in the Documents folder
app_path = os.path.join(docs_path, app_name)
if not os.path.exists(app_path):
    os.makedirs(app_path)

import log_functions as log

target = "APOD-Lockscreen Setup"

log.blank()
log.log(0, target, "Running APOD Setup!")

# Install dependencies
log.log(0, target, "Installing dependencies: requests, beautifulsoup4")
subprocess.check_call(["pip3", "install", "requests"])
subprocess.check_call(["pip3", "install", "beautifulsoup4"])
log.log(0, target, "Installed dependancies")

# Copies the script from the downloaded dir to the app dir
log.log(0, target, "Copying files to Documents")
for file in copied_files:
    file_path = os.path.join(app_path, file)
    shutil.copy(file, file_path)

# Creates a batch file for setting up the script in Task Scheduler
log.log(0, target, "Creating task.bat")
main_path = os.path.join(app_path, main_file)
bat_path = os.path.join(app_path, 'task.bat')
with open(bat_path, 'w') as f:
    f.write('"' + str(python_path) + '" "' + main_path + '"\nexit')

# Creates a batch file for changing the background (has to be separate with admin priv)
log.log(0, target, "Creating background_changer.bat")
img_path = os.path.join(app_path, img_name)
changer_path = os.path.join(app_path, 'background_changer.bat')
with open(changer_path, 'w') as f:
    f.write('set image_path="'+img_path+'"\n')
    f.write('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\PersonalizationCSP" /v LockScreenImagePath /t REG_SZ /d %image_path% /f\n')
    f.write('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\PersonalizationCSP" /v LockScreenImageStatus /t REG_DWORD /d 1 /f')

# Set the command to create the scheduled task
log.log(0, target, "Creating Task Scheduler task")
create_task = 'schtasks /create /tn "' +str(app_name)+ '" /tr "\''+str(bat_path)+'\' " /sc '+str(freq)+' '#/st '+str(time)+' '
subprocess.call(create_task, shell=True)

log.log(0, target, "Running Task")
run_task = 'schtasks /run /tn "'+str(app_name)+'"'
subprocess.call(run_task, shell=True)

log.log(0, target, "Setup complete!")
