from db_operation import DB_operation
from thumbnail_download import switchgame_thumbnail_download
from thumbnail_download_bing import switchgame_thumbnail_download_bing
from switchgame_thumbnail_upload import switchgame_thumbnail_upload
# from s3_upload import s3_upload
import re


if __name__ == "__main__":
    # Mysql接続
    cursor = DB_operation.mysql_connection()[1]
    switchgame_list : list = DB_operation.select_switchgame_list(cursor, 2021, 1)

    no_image = list()
    print("switch game num: " + str(len(switchgame_list)))
    for count in range(0, len(switchgame_list)):

        switchgame_id : str = switchgame_list[count][0]
        switchgame_title : str = switchgame_list[count][1]
        switchgame_downloadlink : str = switchgame_list[count][2]
        switchgame_agelimit : str = switchgame_list[count][3]
        print("ID: " + str(switchgame_id))
        print("【" + switchgame_title + "】")
        
        # 画像ダウンロード
        image_url = switchgame_thumbnail_download(switchgame_id, switchgame_title, switchgame_downloadlink, switchgame_agelimit)

        # 画像が取得できない場合にbingから画像ダウンロードし、タイトル格納
        if "nolink" in image_url:
            image_url = switchgame_thumbnail_download_bing(switchgame_id, switchgame_title)
            no_image.append(switchgame_title)
            print("Insert nolink: " + switchgame_title)

        # 画像をS3にアップロード
        pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
        if re.match(pattern, image_url[0]):
            # s3_upload(switchgame_id, image_url)
            switchgame_thumbnail_upload(switchgame_id, image_url)

    for no_gametitle in no_image:
        print(no_gametitle)
    
    print("!!!COMPLETE!!!")