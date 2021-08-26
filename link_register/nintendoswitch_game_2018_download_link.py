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
    switchgame_list : list = DB_operation.select_switchgame_list(cursor, 2018, 2, 1)

    no_image = list()
    print(switchgame_list)
    print("switch game num: " + str(len(switchgame_list)))
    for count in range(0, len(switchgame_list)):

        switchgame_id : str = switchgame_list[count][0]
        switchgame_title : str = switchgame_list[count][1]
        print("ID: " + str(switchgame_id))
        print("【" + switchgame_title + "】")
        
        # ダウンロードリンク取得
        if "VS.アーバンチャンピオン" in switchgame_title or "VS.エキサイトバイク" in switchgame_title or "アサシン クリード オデッセイ - クラウドバージョン" in switchgame_title or "resident evil cloud version" in switchgame_title or "Unbox: Newbie's Adventure" in switchgame_title or "マリオテニス エース 発売前先行オンライン大会" in switchgame_title or "暁のブレイカーズ" in switchgame_title or "スーパーファミスタレトロ2018" in switchgame_title or "ドラゴンボール ファイターズ オープンβ" in switchgame_title or "NBA 2K19 20周年記念エディション" in switchgame_title or "DARK SOULS REMASTERED NETWORK TEST Ver." in switchgame_title or "ファミコレADV シュタインズ・ゲート" in switchgame_title or "ドラゴンボールZ 超武闘伝" in switchgame_title or "助けてタコさん" in switchgame_title or "Fight of Gods" in switchgame_title or "ゲットアンプドモバイル" in switchgame_title:
            download_link = None
        else:
            download_link = switchgame_link_get(switchgame_title)

        db_register = DB_operation.update_switchgame_link(cursor, switchgame_id, download_link)

    DB_operation.mysql_close(cursor, con)

    print("!!!COMPLETE!!!")