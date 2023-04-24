import datetime
import os  

date = datetime.datetime.now().strftime("%Y-%m-%d")

# General format of the logs: "(DATE)-(TIME) | (MESSAGE LEVEL) | (TARGET) | (MESSAGE)"
INFO = 0
WARNING = 1
ERROR = 2

# Location of log files
app_name = "APOD-Lockscreen"
src_dir = '~\\Documents'
docs_path = os.path.expanduser(src_dir)
app_path = os.path.join(docs_path, app_name)
log_file = os.path.join(app_path, "logs.txt")

def write(message):
    with open(log_file, 'a') as f:
        f.write(message + "\n")

def log(level,target,message):
    ti = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    level = enum2str(level)
    dat = str(ti) + " | " + str(level) + " | " + str.upper(target) + " | " + str(message)

    print(dat)
    write(dat)
    return dat

def blank():
    print("")
    write("")


def enum2str(level):
    if(level == 0):
        return "INFO"
    elif(level == 1):
        return "WARNING"
    elif(level == 2):
        return "ERROR"
    
    # Ensuring the daily log is created and available
if(os.path.exists(log_file)==False):
   print("New log created! " + log_file)
   open(log_file, 'a')
   write(app_name + " logs")