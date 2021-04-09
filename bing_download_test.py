from icrawler.builtin import BingImageCrawler
crawler = BingImageCrawler(storage={"root_dir": "4969"})
crawler.crawl(keyword="アモーング・ザ・スリープ エンハンスド・エディション", max_num=6)