# SwitchGame-Thumbnail-Download

DBに保存されているNintendo Switchでリリースされているソフトの情報から画像をダウンロードするスクリプト

Script to download images from software information released on Nintendo Switch stored in DB

# Features

- 年度別・パッケージまたはダウンロードソフトごとにDBのカラムにあるタイトルからswitchソフトの画像をNintendo Storeからスクレイピングする
- スクレイピングした情報は指定されたディレクトリに保管される(AWS S3の連携もしているがコメントアウト中)
- Nintendo Storeから画像を正常にスクレイピングできないソフトやCEROがZのソフトに関しては、Bingの画像検索からスクレイピングする
- ダウンロードした画像はサイト公開用のために指定サイズにリサイズされる(AWS Lambdaの連携をしていたがコメントアウト中)
- ダウンロードする画像は最大で7つ
<br>

- By year,Scraping the image of the switch software from the title in the DB column for each package or download software from the Nintendo Store
- Scraped information is stored in the specified directory (AWS S3 is also linked, but commented out)
- For software that cannot scrape images normally from the Nintendo Store or software with CERO Z, scrape from Bing's image search.
- The downloaded image will be resized to the specified size for publishing on the site.(I was working with AWS Lambda, but I'm commenting out)
- Up to 7 images to download

# Requirement
- Python3
- Mysql
- AWS
  - S3
  - Lambda
  - EC2
  
# Author
* Dhiki(Infrastructure engineer & Video contributor)
* https://twitter.com/DHIKI_pico


# License
ご自由に使用いただいて構いません。
このプログラムを利用して起きたいかなる問題に対して責任はとりませんのでご了承ください

Feel free to use it.
Please note that we are not responsible for any problems caused by using this program.
