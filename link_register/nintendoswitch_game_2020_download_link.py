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
    switchgame_list : list = DB_operation.select_switchgame_list(cursor, 2020, 2, 1)

    no_image = list()
    print(switchgame_list)
    print("switch game num: " + str(len(switchgame_list)))
    for count in range(0, len(switchgame_list)):

        switchgame_id : str = switchgame_list[count][0]
        switchgame_title : str = switchgame_list[count][1]
        print("ID: " + str(switchgame_id))
        print("【" + switchgame_title + "】")
        
        # ダウンロードリンク取得
        if "スプラトゥーン2" in switchgame_title or "カービィファイターズ2" in switchgame_title or "ブレイブリーデフォルトII 先行体験版" in switchgame_title or "世界のアソビ大全51 ポケットエディション" in switchgame_title or "ニンジャラ 先行体験会" in switchgame_title or "オーオーオーオー" in switchgame_title or "SUPER MARIO BROS. 35" in switchgame_title or "アメリカン・フュージティブ" in switchgame_title or "リディーマー 僧侶の怒り" in switchgame_title or "滅やばたにえん" in switchgame_title or "アルカディ・スミスの事件簿" in switchgame_title or "メトロラストライトリダックス" in switchgame_title or "Zombie Army Trilogy" in switchgame_title or "アウター・ワールド" in switchgame_title or "アンセスターズレガシー" in switchgame_title or "20th Anniversary World Tour" in switchgame_title or "Observer" in switchgame_title or "NO MORE HEROES" in switchgame_title or "NO MORE HEROES 2 DESPERATE STRUGGLE" in switchgame_title or "Saints Row IV" in switchgame_title or "DOOM Eternal" in switchgame_title:
            download_link = None
        else:
            download_link = switchgame_link_get(switchgame_title)

        db_register = DB_operation.update_switchgame_link(cursor, switchgame_id, download_link)

    DB_operation.mysql_close(cursor, con)

    print("!!!COMPLETE!!!")