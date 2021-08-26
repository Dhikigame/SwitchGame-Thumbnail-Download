import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time


def cero_Z_irac_18_download_link(switchgame_title : str, switchgame_downloadlink : str):
    
    #ブラウザを開く
    # driver = webdriver.Chrome()

    # NintendoStoreのソフトのダウンロードサイトを開く
    # driver.get("https://store-jp.nintendo.com/age-gate/?pid=" + switchgame_downloadlink)
    # driver.get("https://store-jp.nintendo.com/list/software/" + switchgame_downloadlink + ".html")
    #https://store-jp.nintendo.com/on/demandware.store/Sites-MNS-Site/ja_JP/Product-Show?pid=https%3a%2f%2fstore-jp%2enintendo%2ecom%2flist%2fsoftware%2f70010000001370%2ehtml
    # driver.get("https://store-jp.nintendo.com/on/demandware.store/Sites-MNS-Site/ja_JP/AgeGate-Yes?pid=" + switchgame_downloadlink[44:-5])
    # https://store-jp.nintendo.com/on/demandware.store/Sites-MNS-Site/ja_JP/AgeGate-Yes?pid=70010000001370

    # 「あなたは18歳以上ですか？」の画面で「はい」をクリックする
    # driver.find_element_by_class_name("ageVerification--buttonGroup__button").click()

    # download_url = "https://store-jp.nintendo.com/list/software/" + switchgame_downloadlink + ".html"
    # html2 = requests.get(download_url)
    # soup2 = BeautifulSoup(html2.content, "html.parser")
    
    # time.sleep(1)

    # 対象のゲームのダウンロードページのHTMLをBeautifulSoupに流し込む
    html = requests.get("https://store-jp.nintendo.com/on/demandware.store/Sites-MNS-Site/ja_JP/AgeGate-Yes?pid=" + switchgame_downloadlink[44:-5])
    soup = BeautifulSoup(html.content, "html.parser")
    # soup = BeautifulSoup(driver.page_source, "html.parser")
    
    # 画像のURLを保存する
    image_url = list()
    i : int = 0
    for element in soup.find_all("li", class_="c-heroCarousel__image--squareRectangle"):
        print(1)
        print("【" + str(i) + "】")
        chap = element.find("source")
        if chap is None:
            continue
        else:
            image_url.append(chap['srcset'])
        print(image_url[i])
        i = i + 1
        if i == 7:
            break

    # #ブラウザを閉じる
    # driver.close()

    return image_url