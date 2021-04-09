from db_operation import DB_operation
from thumbnail_download import switchgame_thumbnail_download
from thumbnail_download_bing import switchgame_thumbnail_download_bing
from switchgame_thumbnail_upload import switchgame_thumbnail_upload
# from s3_upload import s3_upload
import re


if __name__ == "__main__":
    # Mysql接続
    cursor = DB_operation.mysql_connection()
    switchgame_list : list = DB_operation.select_switchgame_list(cursor, 2019, 2)

    no_image = list()
    print("switch game num: " + str(len(switchgame_list)))
    for count in range(0, len(switchgame_list)):

        switchgame_id : str = switchgame_list[count][0]
        switchgame_title : str = switchgame_list[count][1]
        print("ID: " + str(switchgame_id))
        print("【" + switchgame_title + "】")

        if "DAEMON X MACHINA Prototype Orders" in switchgame_title or "トライアルズ ライジング オープンベータ" in switchgame_title or "スプラトゥーン2 特別体験版" in switchgame_title or "ゴエティア -千の魔神と無限の塔-" in switchgame_title or "Saints Row: The Third" in switchgame_title or "Wolfenstein: Youngblood" in switchgame_title or "シンキング シティ" in switchgame_title or "Dead by Daylight" in switchgame_title or "The Church in the Darkness" in switchgame_title or "ウィッチャー3 ワイルドハント コンプリートエディション" in switchgame_title or "ディヴィニティ:オリジナル・シン 2" in switchgame_title or "Alien: Isolation" in switchgame_title or "デビルキングダム" in switchgame_title:
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