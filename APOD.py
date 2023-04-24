import os
import requests
from bs4 import BeautifulSoup
import datetime
import ctypes
import log_functions as log
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )

target = "APOD-LS"
src_dir = '~\\Documents'
app_name = "APOD-Lockscreen"
img_name = "img.jpg"
today = datetime.datetime.today().strftime("%y%m%d")

# Get the path to the Documents and app folder
docs_path = os.path.expanduser(src_dir)
app_path = os.path.join(docs_path, app_name)
last_success = os.path.join(app_path, "lastran.txt")

log.blank()
log.log(0, target, "Starting APOD Lock Screen")



# Send a request to the webpage
url_base = "https://apod.nasa.gov/apod/"
url_full = url_base + "ap" + today + ".html"

try:

    # Checks the last time successfully ran
    try:
        last = ""
        with open(last_success, 'r') as f:
            last = f.readline()

        log.log(0, target, "Last Read: " + str(last))
    except FileNotFoundError:
        with open(last_success, 'w') as f:
            f.write("None Fetched")
        log.log(1, target, "No last_success, writing")

    if(str(today) == str(last)):
        log.log(0, target, "Already fetched today, exiting")
        exit()

    response = requests.get(url_full)

    # Use BeautifulSoup to parse the HTML response
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the image element using the XPath
    image_link = soup.find_all("a")[1]
    image_url = url_base + image_link['href']
    log.log(0, target, "Fetched image! " + str(image_url))

    # Download and save the image
    response = requests.get(image_url)
    img_path = os.path.join(app_path, img_name)

    with open(img_path, 'wb') as f:
        f.write(response.content)

    # Successful, 
    with open(last_success, 'w') as f:
        f.write(str(today))

    log.log(0, target, "Success! Fetched new image, " + str(img_path))

except Exception as e:
    log.log(2, target, e.with_traceback())
