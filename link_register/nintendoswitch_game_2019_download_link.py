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
    switchgame_list : list = DB_operation.select_switchgame_list(cursor, 2019, 2, 1)

    no_image = list()
    print(switchgame_list)
    print("switch game num: " + str(len(switchgame_list)))
    for count in range(0, len(switchgame_list)):

        switchgame_id : str = switchgame_list[count][0]
        switchgame_title : str = switchgame_list[count][1]
        print("ID: " + str(switchgame_id))
        print("【" + switchgame_title + "】")
        
        # ダウンロードリンク取得
        if "DAEMON X MACHINA Prototype Orders" in switchgame_title or "トライアルズ ライジング オープンベータ" in switchgame_title or "スプラトゥーン2 特別体験版" in switchgame_title or "ゴエティア -千の魔神と無限の塔-" in switchgame_title or "Saints Row: The Third" in switchgame_title or "Wolfenstein: Youngblood" in switchgame_title or "シンキング シティ" in switchgame_title or "Dead by Daylight" in switchgame_title or "The Church in the Darkness" in switchgame_title or "ウィッチャー3 ワイルドハント コンプリートエディション" in switchgame_title or "ディヴィニティ:オリジナル・シン 2" in switchgame_title or "Alien: Isolation" in switchgame_title or "デビルキングダム" in switchgame_title:
            download_link = None
        else:
            download_link = switchgame_link_get(switchgame_title)

        db_register = DB_operation.update_switchgame_link(cursor, switchgame_id, download_link)

    DB_operation.mysql_close(cursor, con)

    print("!!!COMPLETE!!!")