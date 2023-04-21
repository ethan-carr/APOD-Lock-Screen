import os
import requests
from bs4 import BeautifulSoup
import datetime
import ctypes
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )

src_dir = '~\\Documents'
app_name = "APOD-Lockscreen"
img_name = "img.jpg"
today = datetime.datetime.today().strftime("%y%m%d")

# Get the path to the Documents and app folder
docs_path = os.path.expanduser(src_dir)
app_path = os.path.join(docs_path, app_name)
last_success = os.path.join(app_path, "lastran.txt")

# Send a request to the webpage
url_base = "https://apod.nasa.gov/apod/"
url_full = url_base + "ap" + today + ".html"

try:

    # Checks the last time successfully ran
    try:
        last = ""
        with open(last_success, 'r') as f:
            last = f.readline()
            print(last)
    except FileNotFoundError:
        with open(last_success, 'w') as f:
            f.write("None Fetched")

    if(str(today) == str(last)):
        print("Already fetched, exiting")
        exit()

    response = requests.get(url_full)

    # Use BeautifulSoup to parse the HTML response
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the image element using the XPath
    image_link = soup.find_all("a")[1]
    image_url = url_base + image_link['href']
    print(image_url)

    # Download and save the image
    response = requests.get(image_url)
    img_path = os.path.join(app_path, img_name)
    print(img_path)
    with open(img_path, 'wb') as f:
        f.write(response.content)

    # Successful, 
    with open(last_success, 'w') as f:
        f.write(str(today))

except Exception as e:
    print("Error!")
    print(e.with_traceback)
