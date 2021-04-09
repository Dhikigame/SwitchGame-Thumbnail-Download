from db_operation import DB_operation
from thumbnail_download import switchgame_thumbnail_download
from thumbnail_download_bing import switchgame_thumbnail_download_bing
from switchgame_thumbnail_upload import switchgame_thumbnail_upload
# from s3_upload import s3_upload
import re


if __name__ == "__main__":
    # Mysql接続
    cursor = DB_operation.mysql_connection()
    switchgame_list : list = DB_operation.select_switchgame_list(cursor, 2019, 1)

    no_image = list()
    print("switch game num: " + str(len(switchgame_list)))
    for count in range(0, len(switchgame_list)):

        switchgame_id : str = switchgame_list[count][0]
        switchgame_title : str = switchgame_list[count][1]
        print("ID: " + str(switchgame_id))
        print("【" + switchgame_title + "】")

        if "フライデー・ザ・13th:ザ・ゲーム" in switchgame_title or "アサシン クリード リベルコレクション" in switchgame_title or "ウィッチャー3 ワイルドハント" in switchgame_title or "Dead by Daylight" in switchgame_title or "ソムニウム ファイル" in switchgame_title or "真 流行り神1・2パック" in switchgame_title or "アサシン クリード III リマスター" in switchgame_title or "THE バラエティゲーム大集合" in switchgame_title or "THE 体感!スポーツパック" in switchgame_title or "ピクセル パズルパック 3-in-1" in switchgame_title or "GUILTY GEAR 20th ANNIVERSARY PACK" in switchgame_title or "オリジンズコレクション" in switchgame_title or "彩京 SHOOTING LIBRARY" in switchgame_title or "エア コンフリクト コレクション" in switchgame_title or "FIFA 20 Legacy Edition" in switchgame_title or "バイオハザード トリプル パック" in switchgame_title or "フォートナイト" in switchgame_title or "ボクらの消しゴム落とし+スポーツセット" in switchgame_title or "爆釣ハンターズ" in switchgame_title:
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