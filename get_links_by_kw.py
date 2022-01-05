import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from googlesearch import search

print(search("какие страны открыты", lang="ru"))


# def get_sites_by_kw(kw):
#     search_results = requests.get("https://yandex.ru/search/?text=" + kw.replace(" ", "+"))
#     search_results.encoding = 'utf-8'

#     file = open("content.txt", "w", encoding="utf-8")
#     file.write(search_results.text)
#     file.close()

#     links = []

#     with open("content.txt", "r", encoding="utf-8") as f:
#         content = f.read() 
#         soup = BeautifulSoup(content, 'lxml')

#         for a in soup.find_all("a", attrs={"class": "OrganicTitle-Link"}):
#             print(a)
#             # if a["href"].find("yabs.yandex.ru") == -1:
#                 # links.append("1")

#     # os.remove("content.txt")
#     # return ",".join(links)


# def main():
#     # df = pd.read_csv("kw_1.csv")
#     # df["sites"] = df["kw"].agg(lambda kw: get_sites_by_kw(kw))

#     # print(df)
#     with open("kw_1.csv", "r", encoding="utf8") as f:
#         for l in f:
#             kw = l.strip()
#             if kw.find("kw") == -1:
#                     search_results = requests.get("https://yandex.ru/search/?text=" + kw.replace(" ", "+"))
#                     search_results.encoding = 'utf-8'

#                     file = open("content.txt", "w", encoding="utf-8")
#                     file.write(search_results.text)
#                     file.close()

#                     # links = []

#                     with open("content.txt", "r", encoding="utf-8") as f:
#                         content = f.read() 
#                         soup = BeautifulSoup(content, 'lxml')

#                         for a in soup.find_all("a", attrs={"class": "OrganicTitle-Link"}):
#                             print(a)

# if __name__ == "__main__":
#     main()