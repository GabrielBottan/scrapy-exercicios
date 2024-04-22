import scrapy


class ProxyScaperSpider(scrapy.Spider):
    #identidade
    name  = 'proxy'
    
    
    #request 
    def start_requests(self):
        urls = ['https://free-proxy-list.net']
        
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse,meta={'next_url':urls[0]})
            
            
    #Response
    def parse(self,response):
        for linha in response.xpath("//table[@class='table table-striped table-bordered']//tr"):
            yield {
                "ip_adress": linha.xpath("./td[1]/text()").get(),
                "port": linha.xpath("./td[2]/text()").get(),
                "code": linha.xpath("./td[3]/text()").get(),
                "country": linha.xpath("./td[4]/text()").get(),
                "cnonymity": linha.xpath("./td[5]/text()").get(),
                "google": linha.xpath("./td[6]/text()").get(),
                "https": linha.xpath("./td[7]/text()").get(),
                "last_checked": linha.xpath("./td[8]/text()").get()
                
            }
        
    
    
    