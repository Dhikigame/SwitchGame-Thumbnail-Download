import requests
from bs4 import BeautifulSoup
from info.information import Information
from info.href_get_list import HrefGetList
from agelimit_download_link import cero_Z_irac_18_download_link

def switchgame_thumbnail_download(switchgame_id : str, switchgame_title : str, switchgame_downloadlink : str, switchgame_agelimit : str):

    switchgame_title = switchgame_title_conv(switchgame_title)
    image_url = list()

    # # Storeの検索Webページを取得して解析する
    # search_url = "https://store-jp.nintendo.com/search/?q=" + switchgame_title
    # html = requests.get(search_url)
    # soup = BeautifulSoup(html.content, "html.parser")

    # chap = soup.find("a", class_="c-productList--item__link")
    # if chap is None:
    #     download_link = HrefGetList.href_get(switchgame_title)
    #     print(download_link)
    # else:
    #     download_link = chap['href']
    #     download_link = download_link[16:30]
    #     download_link = HrefGetList.href_get_nourlsoftware(switchgame_title, download_link)
    #     print(download_link)
    
    # if download_link is "nolink":
    #     return "nolink"
    if switchgame_downloadlink in "None":
        return "nolink"

    # ダウンロードページのWebページを取得して画像を保存する
    # download_url = "https://store-jp.nintendo.com/list/software/" + download_link + ".html"
    download_url = switchgame_downloadlink
    html2 = requests.get(download_url)
    soup2 = BeautifulSoup(html2.content, "html.parser")

    # IRAC/CERO:Z/18+の場合サイト操作TODO
    if switchgame_agelimit == "Z" or switchgame_agelimit == "18+":
        return cero_Z_irac_18_download_link(switchgame_title, switchgame_downloadlink)


    i : int = 0
    for element in soup2.find_all("li", class_="c-heroCarousel__image--squareRectangle"):
        print(1)
        print("【" + str(i) + "】")
        chap2 = element.find("source")
        if chap2 is None:
            continue
        else:
            image_url.append(chap2['srcset'])
        print(image_url[i])
        i = i + 1
        if i == 7:
            break

    i : int = 0
    for element in soup2.find_all("li", class_="c-heroCarousel__image--rectangle"):
        print(1)
        print("【" + str(i) + "】")
        chap2 = element.find("img")
        if chap2 is None:
            continue
        else:
            image_url.append(chap2['src'])
        print(image_url[i])
        i = i + 1
        if i == 7:
            break
    print(image_url[0])
    print("1. Image URL Download Complete")

    return image_url


def switchgame_title_conv(switchgame_title : str):

    print("search title: " + switchgame_title)

    # ダウンロード時、タイトルに余計な文字列が含まれていたら覗く
    if '（英語版）' in switchgame_title:
        switchgame_title = switchgame_title[:-5]
    if '（フランス語版）' in switchgame_title or '（イタリア語版）' in switchgame_title:
        switchgame_title = switchgame_title[:-8]
    if '-' in switchgame_title:
        switchgame_title = switchgame_title.replace('-', ' ')
    if '・' in switchgame_title:
        switchgame_title = switchgame_title.replace('・', ' ')
    if '#' in switchgame_title:
        switchgame_title = switchgame_title.replace('#', ' ')
    if ':' in switchgame_title:
        switchgame_title = switchgame_title.replace(':', ' ')
    if '〜' in switchgame_title:
        switchgame_title = switchgame_title.replace('〜', ' ')
    if 'ドラゴンクエストXI' in switchgame_title:
        switchgame_title = 'ドラゴンクエストXI'
        return switchgame_title
    if 'ドラゴンクエストX' in switchgame_title:
        switchgame_title = 'ドラゴンクエストX'
        return switchgame_title

    print("search title conv: " + switchgame_title)

    return switchgame_title
