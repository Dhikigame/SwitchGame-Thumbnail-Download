from db_operation import DB_operation
from thumbnail_download import switchgame_thumbnail_download
from thumbnail_download_bing import switchgame_thumbnail_download_bing
from switchgame_thumbnail_upload import switchgame_thumbnail_upload
# from s3_upload import s3_upload
import re


if __name__ == "__main__":
    # Mysql接続
    cursor = DB_operation.mysql_connection()
    switchgame_list : list = DB_operation.select_switchgame_list(cursor, 2021, 2)

    no_image = list()
    print("switch game num: " + str(len(switchgame_list)))
    for count in range(0, len(switchgame_list)):

        switchgame_id : str = switchgame_list[count][0]
        switchgame_title : str = switchgame_list[count][1]
        print("ID: " + str(switchgame_id))
        print("【" + switchgame_title + "】")

        if "HITMAN 3 - Cloud Version" in switchgame_title or "ウィッチャー3 ワイルドハント" in switchgame_title or "Kingdoms of Amalur: Re-Reckoning" in switchgame_title or "ピラー:パズル・エスケープ" in switchgame_title or "クレイジーキャプチャー" in switchgame_title:
            image_url = switchgame_thumbnail_download_bing(switchgame_id, switchgame_title)
        else:
            # 画像ダウンロード
            image_url = switchgame_thumbnail_download(switchgame_id, switchgame_title)

        # 画像が取得できない場合にタイトル格納
        if "nolink" in image_url:
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