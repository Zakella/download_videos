import urllib.request
import os

name = input("file name: ")
path = input("folder : ")
url = input("url: ")
print(f"Start downloading {name}")
os.makedirs(path, exist_ok=False)
urllib.request.urlretrieve(url, f"{path}/{name}")
print(f"End! {name}")

