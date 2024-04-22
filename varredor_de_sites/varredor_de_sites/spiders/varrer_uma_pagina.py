import scrapy 
from scrapy.loader import ItemLoader
from varredor_de_sites.items import VarrerFrases

class QuotesToScrapeSpider(scrapy.Spider):
    #identidade
    name = 'frasebot'
    
    #Request
    def start_requests(self):
        #defina a url a ser varrida
        urls = ['https://www.goodreads.com/quotes']
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    #Response
    def parse(self,response):
        #aqui é onde você deve processar o que é retornado da response
                    # with open('pagiona.html','wb') as arquivo:
                 #    arquivo.write(response.body)
    
        #extraindo dados do site
        for elemento in response.xpath("//div[@class='quote']"):
            loader = ItemLoader(item=VarrerFrases(),selector=elemento,response=response)
            loader.add_xpath('frase',".//div[@class='quoteText']/text()")
            loader.add_xpath('autor',".//span[@class='authorOrTitle']/text()")
            loader.add_xpath('tags',".//div[@class='greyText smallText left']/a/text()")
            yield loader.load_item()
            # yield {
            #     'frase':elemento.xpath(".//div[@class='quoteText']/text()").get(),
            #     'autor':elemento.xpath(".//span[@class='authorOrTitle']/text()").get(),
            #     'tags':elemento.xpath(".//div[@class='greyText smallText left']/a/text()").getall()
                
            # }
            
            
    
    