import urllib.request
from pathlib import Path

name = input("file name: ")
path = input("folder : ")
url = input("url: ")
print(f"Start downloading {name}")
Path(path).mkdir(parents=True, exist_ok=True)
urllib.request.urlretrieve(url, f"{path}/{name}")
print(f"End! {Path(path).absolute()}/{name}")


