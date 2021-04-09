import boto3
import shutil
import os
import requests
from info.information import Information


def s3_upload(switchgame_id : str, image_url : list):

    bucket_name = Information.s3_name()
    s3 = boto3.resource('s3')

    # 画像をダウンロードしてS3へアップロードする
    print("画像ダウンロード数：" + str(len(image_url)))
    from_pass = list()
    to_pass = list()
    for i in range(len(image_url)):
        image_name_num : int = i + 1
        from_pass.append(Information.download_dir("Darwin") + "00000" + str(image_name_num) + ".jpg")
        to_pass.append(str(switchgame_id) + "/00000" + str(image_name_num) + ".jpg")
        response = requests.get(image_url[i])
        image = response.content
        with open(from_pass[i], "wb") as download_dir:
            download_dir.write(image)
            print("ダウンロード：" + from_pass[i])
            if os.path.exists(from_pass[i]):
                s3.Bucket(bucket_name).upload_file(from_pass[i], to_pass[i])
                print("S3 Upload：" + to_pass[i])
        
    print("2. AWS S3 Upload Complete")
