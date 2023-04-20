import os

src_dir = '~\\Documents'
app_name = "APOD-Lockscreen"

# Get the path to the Documents and app folder
docs_path = os.path.expanduser(src_dir)
app_path = os.path.join(docs_path, app_name)