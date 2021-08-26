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
    switchgame_list : list = DB_operation.select_switchgame_list(cursor, 2019, 1, 1)

    no_image = list()
    print(switchgame_list)
    print("switch game num: " + str(len(switchgame_list)))
    for count in range(0, len(switchgame_list)):

        switchgame_id : str = switchgame_list[count][0]
        switchgame_title : str = switchgame_list[count][1]
        print("ID: " + str(switchgame_id))
        print("【" + switchgame_title + "】")
        
        # ダウンロードリンク取得
        if "フライデー・ザ・13th:ザ・ゲーム" in switchgame_title or "アサシン クリード リベルコレクション" in switchgame_title or "ウィッチャー3 ワイルドハント" in switchgame_title or "Dead by Daylight" in switchgame_title or "ソムニウム ファイル" in switchgame_title or "真 流行り神1・2パック" in switchgame_title or "アサシン クリード III リマスター" in switchgame_title or "THE バラエティゲーム大集合" in switchgame_title or "THE 体感!スポーツパック" in switchgame_title or "ピクセル パズルパック 3-in-1" in switchgame_title or "GUILTY GEAR 20th ANNIVERSARY PACK" in switchgame_title or "オリジンズコレクション" in switchgame_title or "彩京 SHOOTING LIBRARY" in switchgame_title or "エア コンフリクト コレクション" in switchgame_title or "FIFA 20 Legacy Edition" in switchgame_title or "バイオハザード トリプル パック" in switchgame_title or "フォートナイト" in switchgame_title or "ボクらの消しゴム落とし+スポーツセット" in switchgame_title or "爆釣ハンターズ" in switchgame_title:
            download_link = None
        else:
            download_link = switchgame_link_get(switchgame_title)

        db_register = DB_operation.update_switchgame_link(cursor, switchgame_id, download_link)

    DB_operation.mysql_close(cursor, con)

    print("!!!COMPLETE!!!")