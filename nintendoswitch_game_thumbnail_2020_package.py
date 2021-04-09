from db_operation import DB_operation
from thumbnail_download import switchgame_thumbnail_download
from thumbnail_download_bing import switchgame_thumbnail_download_bing
from switchgame_thumbnail_upload import switchgame_thumbnail_upload
# from s3_upload import s3_upload
import re


if __name__ == "__main__":
    # Mysql接続
    cursor = DB_operation.mysql_connection()
    switchgame_list : list = DB_operation.select_switchgame_list(cursor, 2020, 1)

    no_image = list()
    print("switch game num: " + str(len(switchgame_list)))
    for count in range(0, len(switchgame_list)):

        switchgame_id : str = switchgame_list[count][0]
        switchgame_title : str = switchgame_list[count][1]
        print("ID: " + str(switchgame_id))
        print("【" + switchgame_title + "】")

        if "ベア・ナックルIV スペシャルエディション" in switchgame_title or "Fight of Gods" in switchgame_title or "リマザード ダブルパック" in switchgame_title or "タベオウジャ" in switchgame_title or "Panty Party 完全体" in switchgame_title or "ボクらのスクールバトル+スポーツセット" in switchgame_title or "フォートナイト ラスト・ラフ バンドル" in switchgame_title or "プリニー1・2" in switchgame_title or "リアルタイムバトル将棋オンライン+銀星将棋" in switchgame_title or "ボトルマン デジタル対戦セット" in switchgame_title or "moon PREMIUM EDITION" in switchgame_title or "イース・オリジン スペシャルエディション" in switchgame_title or "LA-MULANA 1&2" in switchgame_title or "医学博士 平岩幹男監修 読むトレGO!" in switchgame_title or "ファンタシースターオンライン2 クラウド エピソード6 デラックスパッケージ" in switchgame_title or "夢現Re:Master バンドルパック" in switchgame_title or "スーパーリアル麻雀" in switchgame_title or "ケムコRPGセレクション Vol.1" in switchgame_title or "ナンプレ10000+パズルの窓" in switchgame_title or "ヒューマン・リソース・マシーン デラックス" in switchgame_title or "デビル メイ クライ トリプル パック" in switchgame_title or "侍道外伝 KATANAKAMI" in switchgame_title or "メトロ リダックス ダブルパック" in switchgame_title or "ゾンビアーミー・トリロジー" in switchgame_title or "アウター・ワールド" in switchgame_title or "コール・オブ・クトゥルフ" in switchgame_title or "アンセスターズレガシー" in switchgame_title or "Dead by Daylight サイレントヒルエディション" in switchgame_title or "セインツロウIV リエレクテッド" in switchgame_title or "Vampyr" in switchgame_title or "バイオショック コレクション" in switchgame_title or "ボーダーランズ レジェンダリー" in switchgame_title:
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