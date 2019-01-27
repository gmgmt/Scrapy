from scrapy import cmdline

cmdline.execute(("scrapy crawl wenku_data".split()))#运行
# cmdline.execute(("scrapy crawl quotes -o quotes.json".split()))#保存为想要的格式到本地