import sys
from switchgame_link import switchgame_link_get
sys.path.append("../")
from db_operation import DB_operation
import re


if __name__ == "__main__":
    # Mysql接続
    mysql_con = DB_operation.mysql_connection()
    con = mysql_con[0]
    cursor = mysql_con[1]
    switchgame_list : list = DB_operation.select_switchgame_list(cursor, 2020, 1, 1)

    no_image = list()
    print(switchgame_list)
    print("switch game num: " + str(len(switchgame_list)))
    for count in range(0, len(switchgame_list)):

        switchgame_id : str = switchgame_list[count][0]
        switchgame_title : str = switchgame_list[count][1]
        print("ID: " + str(switchgame_id))
        print("【" + switchgame_title + "】")
        
        # ダウンロードリンク取得
        if "ベア・ナックルIV スペシャルエディション" in switchgame_title or "Fight of Gods" in switchgame_title or "リマザード ダブルパック" in switchgame_title or "タベオウジャ" in switchgame_title or "Panty Party 完全体" in switchgame_title or "ボクらのスクールバトル+スポーツセット" in switchgame_title or "フォートナイト ラスト・ラフ バンドル" in switchgame_title or "プリニー1・2" in switchgame_title or "リアルタイムバトル将棋オンライン+銀星将棋" in switchgame_title or "ボトルマン デジタル対戦セット" in switchgame_title or "moon PREMIUM EDITION" in switchgame_title or "イース・オリジン スペシャルエディション" in switchgame_title or "LA-MULANA 1&2" in switchgame_title or "医学博士 平岩幹男監修 読むトレGO!" in switchgame_title or "ファンタシースターオンライン2 クラウド エピソード6 デラックスパッケージ" in switchgame_title or "夢現Re:Master バンドルパック" in switchgame_title or "スーパーリアル麻雀" in switchgame_title or "ケムコRPGセレクション Vol.1" in switchgame_title or "ナンプレ10000+パズルの窓" in switchgame_title or "ヒューマン・リソース・マシーン デラックス" in switchgame_title or "デビル メイ クライ トリプル パック" in switchgame_title or "侍道外伝 KATANAKAMI" in switchgame_title or "メトロ リダックス ダブルパック" in switchgame_title or "ゾンビアーミー・トリロジー" in switchgame_title or "アウター・ワールド" in switchgame_title or "コール・オブ・クトゥルフ" in switchgame_title or "アンセスターズレガシー" in switchgame_title or "Dead by Daylight サイレントヒルエディション" in switchgame_title or "セインツロウIV リエレクテッド" in switchgame_title or "Vampyr" in switchgame_title or "バイオショック コレクション" in switchgame_title or "ボーダーランズ レジェンダリー" in switchgame_title:
            download_link = None
        else:
            download_link = switchgame_link_get(switchgame_title)

        db_register = DB_operation.update_switchgame_link(cursor, switchgame_id, download_link)

    DB_operation.mysql_close(cursor, con)

    print("!!!COMPLETE!!!")