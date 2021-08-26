import sys
import requests
from bs4 import BeautifulSoup
sys.path.append("../info")
from href_get_list import HrefGetList

def switchgame_link_get(switchgame_title : str):

    switchgame_title = str(switchgame_title)
    switchgame_title = switchgame_title_conv(switchgame_title)
    image_url = list()

    # Storeの検索Webページを取得して解析する
    search_url = "https://store-jp.nintendo.com/search/?q=" + switchgame_title
    html = requests.get(search_url)
    soup = BeautifulSoup(html.content, "html.parser")

    chap = soup.find("a", class_="c-productList--item__link")
    if chap is None:
        download_link = HrefGetList.href_get(switchgame_title)
        print(download_link)
    else:
        download_link = chap['href']
        download_link = download_link[16:30]
        download_link = HrefGetList.href_get_nourlsoftware(switchgame_title, download_link)
        print(download_link)
    
    if download_link is "nolink":
        return None

    # ダウンロードページのWebページを取得して画像を保存する
    download_url = "https://store-jp.nintendo.com/list/software/" + download_link + ".html"
    print(download_url)

    print("1. Download Page URL Get")

    return download_url


def switchgame_title_conv(switchgame_title : str):

    print("search title: " + str(switchgame_title))

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
