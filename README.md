# APOD-Lock-Screen

Love NASA's Astronomy Photo of the Day? How about making it your lock screen every day!

This application fetches the new Astronomy Photo of the Day (APOD) each morning and sets the Windows lock screen to the photo. This repo contains two files, a setup script, and a running script to do the file grabbing. 
It takes advantage of the Windows Task Scheduler to take care of the required functions, however, since Windows can be strange about some things the Python files are used to create batch scripts and setup the tasks. 

***

## Installation

To get started, clone the repository, and run the `setup.py` script. This will take care of creating the necessary directories and scripts needed for operation. The default installation location is in the users Documents folder and will clone the `APOD.py` and `setup.py` script into the folder, as well write the required batch scripts. It will then set up the Task Scheduling using `schtask` and will be visible as `APOD-Lockscreen`.

The Task works by checking if a new image is available, if not then the script just exits until new is released.

From here there should be nothing left to do except enjoy the daily image from APOD! The code will only save the most recent photo, overwritten daily. 

## Removal

If you would like to remove this from running daily and completely uninstall, just delete the directory containing the batch files and python scripts. Additionally, if you would like, removing the Task Scheduler items is as easy and finding them in Task Scheduler, right click each, and delete. 

## Usage

Should all run on its own as scheduled, no additional interaction needed after initial setup.

## Updates

- 04/21/2023: Removed the background changer task, as it does not need to run more than once. Updated frequency to every couple hours, daily only works if computer is logged in at the scheduled run time. Removed annoying steps of setting up `schtask` from the Windows GUI. Task made to run minimized now.
- 04/24/2023: Adding additional logging for tracing back errors, also updated the batch script to fix small error, functioning as expected now.

## What’s next

While this works as is, will not be heavily updating. Would like to add GUI to make it more user serviceable.

***

### Contact me!

GitHub: @ethan-carr

Email: ethan@ethancarr.dev

