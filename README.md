# APOD-Lock-Screen

Love NASA's Astronomy Photo of the Day? How about making it your lock screen evey day!

This application fetches the new Astronomy Photo of the Day (APOD) each morning and sets the Windows lock screen to the photo. This repo contains two files, a setup script and a running script to do the file grabbing. 
It takes advantage of the Windows Task Scheduler to take care of the required functions, however, since Windows can be strange about some things the Python files are used to create batch scripts and setup the tasks. 

***

## Installation

To get started, clone the repository and run the `setup.py` script. This will take care of creating the necessary directories and scripts needed for operation. The default installation location is in the users Documents folder, and will clone the `APOD.py` and `setup.py` script into the folder, as well write the required batch scripts. It will then setup the Task Scheduling using `schtask` and will be visible as `APOD-Lockscreen` and `APOD-Lockscreen_bgchanger`. 

Since Windows is strange, we need to change some of the task settings by hand, after running `setup.py` open Task Scheduler either by start menu or doing
- `Win + R`, type in `taskschd.msc`, then press `Enter`


- Go to `Task Scheduler Library` on the left hand menu, and find tasks for `APOD-Lockscreen` and `APOD-Lockscreen_bgchanger`

![image](https://user-images.githubusercontent.com/111789413/233491951-c2406e9c-90c7-42f5-91a3-d12571274930.png)

- Right click on `APOD-Lockscreen` and select `Properties`


- Under `Settings`, check the box next to `- [x] Run task as soon as possible after a scheduled start is missed`, this will run the task on user logon if the computer is off before the scheduled run time. Otherwise the image will only change if the user is logged in at the precoded start time of 06:00.

![image](https://user-images.githubusercontent.com/111789413/233492171-58f07a92-6b71-458c-83b5-9c91036b5f66.png)

- Right click on `APOD-Lockscreen_bgchanger` and select `Properties`
- Repeat the same step as before under `Settings` to run the task as soon as possible after missed start. 

- In the `General` tab under `APOD-Lockscreen_bgchanger`'s properties, make sure `- [x] Run with highest priviledges` is checked as well, as changing the background image needs to done as administrator, if not checked the tasks will run but will not change the lock screen.

![image](https://user-images.githubusercontent.com/111789413/233500907-4a63e740-2444-4789-b95f-abfc715af727.png)

From here there should be nothing left to do except enjoy the daily image from APOD! The code will only save the most recent photo, overwritten daily. 

## Removal

If you would like to remove this from running daily and completely uninstall, just delete the directory containing the batch files and python scripts. Additionally if you would like, removing the Task Scheduler items is as easy and finding them in Task Scheduler, right click each, and delete. 

## Usage

Should all run on its on as scheduled, no additional interaction needed after initial setup.


## Whats next

While this works as is, will not be heavily updating. Would like to add GUI to make more user serviceable, as well as trying to move the Task Scheduling to Powershell possibly reducing the amount of setup steps required as well as make easier to remove

***

### Contact me!

GitHub: @ethan-carr
Email: ethan@ethancarr.dev

