import scrapy


class ProxyScraperSpider2(scrapy.Spider):
    #identidade
    name = "proxy2"
    
    def start_requests(self):
        #requisição
        urls = ["https://free-proxy-list.net/web-proxy.html"]
        
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
            
            
           #response 
    def parse(self,response):
        for linha in response.xpath("//table[@class='table table-striped table-bordered']//tr"):
            yield {
                "Proxy Name": linha.xpath("./td[1]/a/text()").get(),
                "Domain": linha.xpath("./td[2]/text()").get(),
                "Country": linha.xpath("./td[3]/text()").get(),
                "Speed": linha.xpath("./td[4]/text()").get(),
                "Popularity": linha.xpath("./td[5]/div/div/text()").get()
            }
        