import os, bs4, json
import urllib.request, urllib.error

keywords = ['rose', 'sunflower', 'lilium']

def get_soup(url, header):
    return bs4.BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')

def search_image(keyword):
    url="https://www.google.co.jp/search?q="+keyword+"&source=lnms&tbm=isch"
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    soup = get_soup(url,header)
    return soup

def download_image(soup, save_directory):
    ActualImages=[]
    for a in soup.find_all("div",{"class":"rg_meta"}):
        link, Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
        ActualImages.append((link,Type))
    print(ActualImages)

for keyword in keywords:
    print("download now ...",  keyword)

    save_directory = "./dataset/" + keyword
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    soup = search_image(keyword)

    download_image(soup, save_directory)
