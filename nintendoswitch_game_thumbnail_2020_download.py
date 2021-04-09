from db_operation import DB_operation
from thumbnail_download import switchgame_thumbnail_download
from thumbnail_download_bing import switchgame_thumbnail_download_bing
from switchgame_thumbnail_upload import switchgame_thumbnail_upload
# from s3_upload import s3_upload
import re


if __name__ == "__main__":
    # Mysql接続
    cursor = DB_operation.mysql_connection()
    switchgame_list : list = DB_operation.select_switchgame_list(cursor, 2020, 2)

    no_image = list()
    print("switch game num: " + str(len(switchgame_list)))
    for count in range(0, len(switchgame_list)):

        switchgame_id : str = switchgame_list[count][0]
        switchgame_title : str = switchgame_list[count][1]
        print("ID: " + str(switchgame_id))
        print("【" + switchgame_title + "】")

        if "スプラトゥーン2" in switchgame_title or "カービィファイターズ2" in switchgame_title or "ブレイブリーデフォルトII 先行体験版" in switchgame_title or "世界のアソビ大全51 ポケットエディション" in switchgame_title or "ニンジャラ 先行体験会" in switchgame_title or "オーオーオーオー" in switchgame_title or "SUPER MARIO BROS. 35" in switchgame_title or "アメリカン・フュージティブ" in switchgame_title or "リディーマー 僧侶の怒り" in switchgame_title or "滅やばたにえん" in switchgame_title or "アルカディ・スミスの事件簿" in switchgame_title or "メトロラストライトリダックス" in switchgame_title or "Zombie Army Trilogy" in switchgame_title or "アウター・ワールド" in switchgame_title or "アンセスターズレガシー" in switchgame_title or "20th Anniversary World Tour" in switchgame_title or "Observer" in switchgame_title or "NO MORE HEROES" in switchgame_title or "NO MORE HEROES 2 DESPERATE STRUGGLE" in switchgame_title or "Saints Row IV" in switchgame_title or "DOOM Eternal" in switchgame_title:
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