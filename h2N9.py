import os, bs4
import urllib.request, urllib.error

keywords = ['rose', 'sunflower', 'lilium']

def get_soup(url, header):
    return bs4.BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')

def search_image(keyword):
    url="https://www.google.co.jp/search?q="+keyword+"&source=lnms&tbm=isch"
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    soup = get_soup(url,header)
    return soup

for keyword in keywords:
    print("download now ...",  keyword)

    save_directory = "./dataset/" + keyword
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # イメージ検索をする
    soup = search_image(keyword)
    print(soup)