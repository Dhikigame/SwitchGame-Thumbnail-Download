import os
import requests
from PIL import Image
import platform
import time
from info.information import Information

pf = platform.system()


def switchgame_thumbnail_upload(switchgame_id : str, image_url : list):

    print("画像ダウンロード数：" + str(len(image_url)))
    target_pass = list()

    if pf == 'Darwin':
        os.makedirs(Information.download_dir("Darwin") + str(switchgame_id), exist_ok=True)
    else:
        os.makedirs(Information.download_dir("Linux") + str(switchgame_id), exist_ok=True)

    for i in range(len(image_url)):
        image_name_num : int = i + 1
        if pf == 'Darwin':
            target_pass.append(Information.download_dir("Darwin") + str(switchgame_id) + "/00000" + str(image_name_num) + ".jpg")
        else:
            target_pass.append(Information.download_dir("Linux") + str(switchgame_id) + "/00000" + str(image_name_num) + ".jpg")
        response = requests.get(image_url[i])
        image = response.content
        # 画像ダウンロード
        with open(target_pass[i], "wb") as download_dir:
            download_dir.write(image)
            print("ダウンロード：" + target_pass[i])

    print("2. File Server Upload Complete")

    for i in range(len(image_url)):
        image_name_num : int = i + 1
        img = Image.open(target_pass[i])
        if "000001.jpg" in target_pass[i]:
            img_resize = img.convert('RGB').resize((820, 461))
        else:
            img_resize = img.convert('RGB').resize((332, 187))
        img_resize.save(target_pass[i])
        print("リサイズ完了" + str(image_name_num) + ":" + target_pass[i])

    print("3. Image Resize Complete")
