# -*- coding: utf-8 -*-
import boto3
import cv2


s3 = boto3.resource('s3')

def lambda_handler(event, context):

	print("Lambdaが呼ばれたよ！！！！！！")
	print(cv2.__version__)
	input_bucket = event['Records'][0]['s3']['bucket']['name']
	fromfolder_image = event['Records'][0]['s3']['object']['key']
	print("bucket =           ", input_bucket)
	print("fromfolder_image = ", fromfolder_image)
	bucket = s3.Bucket("nintendoswitch-game-thumbnail")

	tofolder_image = "/tmp/" + fromfolder_image.split('/')[-1]
	print(tofolder_image)
	bucket.download_file(fromfolder_image, tofolder_image)

	im = cv2.imread(tofolder_image)
	h, w, c = im.shape
	print('before width:  ', w)
	print('before height: ', h)

	tofolder_image = cv2.imread(tofolder_image)
	resize_image = cv2.resize(tofolder_image, dsize=(332, 187))
	# if "000001.jpg" in fromfolder_image:
	# 	resize_image = cv2.resize(tofolder_image, dsize=(820, 461))
	# else:
	# 	resize_image = cv2.resize(tofolder_image, dsize=(332, 187))
	tofolder_resize_image = "/tmp/" + fromfolder_image.split('/')[-1]
	cv2.imwrite(tofolder_resize_image, resize_image)

	im = cv2.imread(tofolder_resize_image)
	h, w, c = im.shape
	print('after width:  ', w)
	print('after height: ', h)

	uploadfolder_image = fromfolder_image
	bucket = s3.Object(input_bucket, fromfolder_image)
	bucket.upload_file(tofolder_resize_image)