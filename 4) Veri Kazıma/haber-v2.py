"""
@author: Ritalin
problem: Donanım haber sitesinden veri çekmek
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.donanimhaber.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.encoding = "utf-8"

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("a", class_="baslik")
    authors = soup.find_all("a", class_="lnk")

    data = []

    for i in range(min(len(titles), len(authors))):
        title = titles[i].text.strip()
        author = authors[i].text.strip()

        data.append([title, author])

    df = pd.DataFrame(data, columns=["Başlık", "Yazar"])
    print(df)
else:
    print("Bağlantı başarısız, HTTP Kodu:", response.status_code)
