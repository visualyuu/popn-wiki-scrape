import requests
from bs4 import BeautifulSoup


i = 29
while i <= 50:
    URL = f"https://popn.wiki/%E9%9B%A3%E6%98%93%E5%BA%A6%E8%A1%A8/lv{i}"
    page = requests.get(URL)


    soup = BeautifulSoup(page.content, "html.parser")


    cf = open(f"popn{i}s.txt","w", encoding="utf-8")
    names = soup.find_all(class_="col3")

    for name in names:
        name = name.get_text()
        cf.write(f"{name}\n")

    cf.close()
    i+= 1
