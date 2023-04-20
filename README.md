# APOD-Lock-Screen

Love NASA's Astronomy Photo of the Day? How about making it your lock screen evey day!

This application fetches the new Astronomy Photo of the Day (APOD) each morning and sets the Windows lock screen to the photo. This repo contains two files, a setup script and a running script to do the file grabbing. 
It takes advantage of the Windows Task Scheduler to take care of the required functions, however, since Windows can be strange about some things the Python files are used to create batch scripts and setup the tasks. 

## Installation

To get started, clone the repository and run the `setup.py` script. This will take care of creating the necessary directories and scripts needed for operation. The default installation location is in the users Documents folder, and will clone the `APOD.py` and `setup.py` script into the folder, as well write the required batch scripts. It will then setup the Task Scheduling using `schtask` and will be visible as `APOD-Lockscreen` and `APOD-Lockscreen_bgchanger`. 

Since Windows is strange, we need to change some of the task settings by hand, after running `setup.py` open Task Scheduler either by start menu or doing
- `Win + R`, type in `taskschd.msc`, then press `Enter`

![image](https://user-images.githubusercontent.com/111789413/233491951-c2406e9c-90c7-42f5-91a3-d12571274930.png)
- Go to `Task Scheduler Library` on the left hand menu, and find tasks for `APOD-Lockscreen` and `APOD-Lockscreen_bgchanger`

- Right click on `APOD-Lockscreen` and select `Properties`

![image](https://user-images.githubusercontent.com/111789413/233492171-58f07a92-6b71-458c-83b5-9c91036b5f66.png)
- Under `Settings`, check the box next to "Run task as soon as possible after a scheduled start is missed", this will run the task on user logon if the computer is off before the scheduled run time. Otherwise the image will only change if the user is logged in at the precoded start time of 06:00.

- Right click on `APOD-Lockscreen_bgchanger` and select `Properties`
- Repeat the same step as before under `Settings` to run the task as soon as possible after missed start. 
- 
