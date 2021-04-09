import boto3
import shutil
from icrawler.builtin import BingImageCrawler

bucket_name = "nintendoswitch-game-thumbnail"
s3 = boto3.resource('s3')

# 画像ダウンロード
crawler = BingImageCrawler(storage={"root_dir": "8547"})
crawler.crawl(keyword="モチ上ガール", max_num=6)
print("Image Download")

# 画像をS3にアップロード
s3.Bucket(bucket_name).upload_file('./8547/000001.jpg', '8547/000001.jpg')
s3.Bucket(bucket_name).upload_file('./8547/000002.jpg', '8547/000002.jpg')
s3.Bucket(bucket_name).upload_file('./8547/000003.jpg', '8547/000003.jpg')
s3.Bucket(bucket_name).upload_file('./8547/000004.jpg', '8547/000004.jpg')
s3.Bucket(bucket_name).upload_file('./8547/000005.jpg', '8547/000005.jpg')
s3.Bucket(bucket_name).upload_file('./8547/000006.jpg', '8547/000006.jpg')
print("AWS S3 Upload")

# ダウンロードしたサーバにあるフォルダを削除
shutil.rmtree("./8547/")
print("Image Folder Remove")
