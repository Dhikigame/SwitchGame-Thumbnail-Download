from db_operation import DB_operation
from thumbnail_download import switchgame_thumbnail_download
from thumbnail_download_bing import switchgame_thumbnail_download_bing
from switchgame_thumbnail_upload import switchgame_thumbnail_upload
# from s3_upload import s3_upload
import re


if __name__ == "__main__":
    # Mysql接続
    cursor = DB_operation.mysql_connection()
    switchgame_list : list = DB_operation.select_switchgame_list(cursor, 2018, 1)

    no_image = list()
    print("switch game num: " + str(len(switchgame_list)))
    for count in range(0, len(switchgame_list)):

        switchgame_id : str = switchgame_list[count][0]
        switchgame_title : str = switchgame_list[count][1]
        print("ID: " + str(switchgame_id))
        print("【" + switchgame_title + "】")

        if "プロ野球 ファミスタ エボリューション" in switchgame_title or "ディープフリーズバンドル" in switchgame_title or "HUGっと!プリキュア" in switchgame_title or "ゲームでピラメキ大作戦!" in switchgame_title or "The Elder Scrolls V: Skyrim" in switchgame_title or "DOOM" in switchgame_title or "The New Colossus" in switchgame_title or "FIFA 19" in switchgame_title:
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