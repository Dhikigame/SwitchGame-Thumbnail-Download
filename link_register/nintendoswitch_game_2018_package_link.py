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
    switchgame_list : list = DB_operation.select_switchgame_list(cursor, 2018, 1, 1)

    no_image = list()
    print(switchgame_list)
    print("switch game num: " + str(len(switchgame_list)))
    for count in range(0, len(switchgame_list)):

        switchgame_id : str = switchgame_list[count][0]
        switchgame_title : str = switchgame_list[count][1]
        print("ID: " + str(switchgame_id))
        print("【" + switchgame_title + "】")
        
        # ダウンロードリンク取得
        if "プロ野球 ファミスタ エボリューション" in switchgame_title or "ディープフリーズバンドル" in switchgame_title or "HUGっと!プリキュア" in switchgame_title or "ゲームでピラメキ大作戦!" in switchgame_title or "The Elder Scrolls V: Skyrim" in switchgame_title or "DOOM" in switchgame_title or "The New Colossus" in switchgame_title or "FIFA 19" in switchgame_title:
            download_link = None
        else:
            download_link = switchgame_link_get(switchgame_title)

        db_register = DB_operation.update_switchgame_link(cursor, switchgame_id, download_link)

    DB_operation.mysql_close(cursor, con)

    print("!!!COMPLETE!!!")