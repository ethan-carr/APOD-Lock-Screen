import os
import subprocess
import shutil
import sys

# Install dependencies
subprocess.check_call(["pip3", "install", "requests"])
subprocess.check_call(["pip3", "install", "beautifulsoup4"])

# File directories and copying params
src_dir = '~\\Documents'
app_name = "APOD-Lockscreen"
copied_files = ["paster.py", "setup.py"]
main_file = "paster.py"

# Windows Tasks Scheduler params
freq = "daily"
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

# Copies the script from the downloaded dir to the app dir
for file in copied_files:
    file_path = os.path.join(app_path, file)
    shutil.copy(file, file_path)

# Creates a batch file for setting up the script in Task Scheduler
main_path = os.path.join(app_path, main_file)
bat_path = os.path.join(app_path, 'task.bat')
with open(bat_path, 'w') as f:
    f.write('"' + str(python_path) + '" "' + main_path + '"\nexit')

# Creates a batch file for changing the background (has to be separate with admin priv)
img_path = os.path.join(app_path, img_name)
changer_path = os.path.join(app_path, 'background_changer.bat')
with open(changer_path, 'w') as f:
    f.write('set image_path="'+img_path+'"\n')
    f.write('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\PersonalizationCSP" /v LockScreenImagePath /t REG_SZ /d %image_path% /f\n')
    f.write('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\PersonalizationCSP" /v LockScreenImageStatus /t REG_DWORD /d 1 /f')

# Set the command to create the scheduled task
command = 'schtasks /create /tn "' +str(app_name)+ '" /tr "\''+str(bat_path)+'\' " /sc '+str(freq)+' /st '+str(time)+' '
subprocess.call(command, shell=True)

command2 = 'schtasks /create /tn "' +str(app_name) + '_bgchanger' + '" /tr "\''+str(changer_path)+'\' " /sc '+str(freq)+' /st '+str(time2)+''
subprocess.call(command2, shell=True)
