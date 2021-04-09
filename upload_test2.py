import boto3

bucket_name = "nintendoswitch-game-thumbnail"
s3 = boto3.resource('s3')

s3.Bucket(bucket_name).upload_file('./天穂のサクナヒメ/000001.jpg', 'sakuna/test1.jpg')
s3.Bucket(bucket_name).upload_file('./天穂のサクナヒメ/000002.jpg', 'sakuna/test2.jpg')
s3.Bucket(bucket_name).upload_file('./天穂のサクナヒメ/000003.jpg', 'sakuna/test3.jpg')
s3.Bucket(bucket_name).upload_file('./天穂のサクナヒメ/000004.jpg', 'sakuna/test4.jpg')
s3.Bucket(bucket_name).upload_file('./天穂のサクナヒメ/000005.jpg', 'sakuna/test5.jpg')
s3.Bucket(bucket_name).upload_file('./天穂のサクナヒメ/000006.jpg', 'sakuna/test6.jpg')