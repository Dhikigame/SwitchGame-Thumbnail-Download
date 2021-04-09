from icrawler.builtin import BingImageCrawler
import os
import shutil
from PIL import Image
import math
import platform
from info.information import Information


pf = platform.system()


def calc_image(img, former_width=187):
    if former_width == 461:
        width = math.floor(461 * img.width / img.height)
    else:
        width = math.floor(187 * img.width / img.height)

    return width


def title_search_conv(switchgame_title):
    # titleから画像をダウンロード
    edition_flag = 0
    # ダウンロード時、タイトルに余計な文字列が含まれていたら除く
    if '（英語版）' in switchgame_title:
        switchgame_title = switchgame_title[:-5] + " switch"
        edition_flag = 1
    if '（フランス語版）' in switchgame_title or '（イタリア語版）' in switchgame_title:
        switchgame_title = switchgame_title[:-8] + " switch"
        edition_flag = 2
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
    if edition_flag == 0:
        switchgame_title = switchgame_title + " switch"
    print("search title: " + switchgame_title)

    return switchgame_title


def switchgame_thumbnail_download_bing(switchgame_id : str, switchgame_title : str):

    if pf == 'Darwin':

        # ダウンロードしたサーバにあるフォルダを削除
        if os.path.exists(Information.download_dir("Darwin") + str(switchgame_id) + "/"):
            shutil.rmtree(Information.download_dir("Darwin") + str(switchgame_id) + "/")

        # 保存先ディレクトリを指定
        os.makedirs(str(switchgame_id), exist_ok=True)
        crawler = BingImageCrawler(storage={"root_dir":  Information.download_dir("Darwin") + str(switchgame_id)})
        print("1. Image Folder Remove Complete")

        # 画像検索のためのswitchソフトのタイトルを変換する
        switchgame_title = title_search_conv(switchgame_title)

        # switchソフトのタイトルを検索し、画像ダウンロード
        crawler.crawl(keyword=switchgame_title, max_num=7)
        print("2. File Server Upload Complete")

        print("000001.jpgのリサイズ")
        img = Image.open(Information.download_dir("Darwin") + str(switchgame_id) + "/000001.jpg")
        img_resize = img.convert('RGB').resize((calc_image(img, 461), 461))
        img_resize.save(Information.download_dir("Darwin") + str(switchgame_id) + "/000001.jpg")
        print("000002.jpgのリサイズ")
        img = Image.open(Information.download_dir("Darwin") + str(switchgame_id) + "/000002.jpg")
        img_resize = img.convert('RGB').resize((calc_image(img, 187), 187))
        img_resize.save(Information.download_dir("Darwin") + str(switchgame_id) + "/000002.jpg")
        print("000003.jpgのリサイズ")
        img = Image.open(Information.download_dir("Darwin") + str(switchgame_id) + "/000003.jpg")
        img_resize = img.convert('RGB').resize((calc_image(img, 187), 187))
        img_resize.save(Information.download_dir("Darwin") + str(switchgame_id) + "/000003.jpg")
        print("000004.jpgのリサイズ")
        img = Image.open(Information.download_dir("Darwin") + str(switchgame_id) + "/000004.jpg")
        img_resize = img.convert('RGB').resize((calc_image(img, 187), 187))
        img_resize.save(Information.download_dir("Darwin") + str(switchgame_id) + "/000004.jpg")
        print("000005.jpgのリサイズ")
        img = Image.open(Information.download_dir("Darwin") + str(switchgame_id) + "/000005.jpg")
        img_resize = img.convert('RGB').resize((calc_image(img, 187), 187))
        img_resize.save(Information.download_dir("Darwin") + str(switchgame_id) + "/000005.jpg")
        print("000006.jpgのリサイズ")
        img = Image.open(Information.download_dir("Darwin") + str(switchgame_id) + "/000006.jpg")
        img_resize = img.convert('RGB').resize((calc_image(img, 187), 187))
        img_resize.save(Information.download_dir("Darwin") + str(switchgame_id) + "/000006.jpg")
        print("000007.jpgのリサイズ")
        img = Image.open(Information.download_dir("Darwin") + str(switchgame_id) + "/000007.jpg")
        img_resize = img.convert('RGB').resize((calc_image(img, 187), 187))
        img_resize.save(Information.download_dir("Darwin") + str(switchgame_id) + "/000007.jpg")

        print("3. Image Resize Complete")



    if pf == 'Linux':

        # ダウンロードしたサーバにあるフォルダを削除
        if os.path.exists(Information.download_dir("Linux") + str(switchgame_id) + "/"):
            shutil.rmtree(Information.download_dir("Linux") + str(switchgame_id) + "/")

        # 保存先ディレクトリを指定
        os.makedirs(str(switchgame_id), exist_ok=True)
        crawler = BingImageCrawler(storage={"root_dir":  Information.download_dir("Linux") + str(switchgame_id)})
        print("1. Image Folder Remove Complete")

        # 画像検索のためのswitchソフトのタイトルを変換する
        switchgame_title = title_search_conv(switchgame_title)

        # switchソフトのタイトルを検索し、画像ダウンロード
        crawler.crawl(keyword=switchgame_title, max_num=7)
        print("2. File Server Upload Complete")

        print("000001.jpgのリサイズ")
        img = Image.open(Information.download_dir("Linux") + str(switchgame_id) + "/000001.jpg")
        img_resize = img.convert('RGB').resize((calc_image(img, 461), 461))
        img_resize.save(Information.download_dir("Linux") + str(switchgame_id) + "/000001.jpg")
        print("000002.jpgのリサイズ")
        img = Image.open(Information.download_dir("Linux") + str(switchgame_id) + "/000002.jpg")
        img_resize = img.convert('RGB').resize((calc_image(img, 187), 187))
        img_resize.save(Information.download_dir("Linux") + str(switchgame_id) + "/000002.jpg")
        print("000003.jpgのリサイズ")
        img = Image.open(Information.download_dir("Linux") + str(switchgame_id) + "/000003.jpg")
        img_resize = img.convert('RGB').resize((calc_image(img, 187), 187))
        img_resize.save(Information.download_dir("Linux") + str(switchgame_id) + "/000003.jpg")
        print("000004.jpgのリサイズ")
        img = Image.open(Information.download_dir("Linux") + str(switchgame_id) + "/000004.jpg")
        img_resize = img.convert('RGB').resize((calc_image(img, 187), 187))
        img_resize.save(Information.download_dir("Linux") + str(switchgame_id) + "/000004.jpg")
        print("000005.jpgのリサイズ")
        img = Image.open(Information.download_dir("Linux") + str(switchgame_id) + "/000005.jpg")
        img_resize = img.convert('RGB').resize((calc_image(img, 187), 187))
        img_resize.save(Information.download_dir("Linux") + str(switchgame_id) + "/000005.jpg")
        print("000006.jpgのリサイズ")
        img = Image.open(Information.download_dir("Linux") + str(switchgame_id) + "/000006.jpg")
        img_resize = img.convert('RGB').resize((calc_image(img, 187), 187))
        img_resize.save(Information.download_dir("Linux") + str(switchgame_id) + "/000006.jpg")
        print("000007.jpgのリサイズ")
        img = Image.open(Information.download_dir("Linux") + str(switchgame_id) + "/000007.jpg")
        img_resize = img.convert('RGB').resize((calc_image(img, 187), 187))
        img_resize.save(Information.download_dir("Linux") + str(switchgame_id) + "/000007.jpg")

        print("3. Image Resize Complete")


    image_url = list()
    image_url.append("image_uploaded")

    return image_url