import scrapy 



class QuotesToScrapy(scrapy.Spider):
    name = 'varrer'
    
    
    def start_requests(self):
        urls = ['https://www.goodreads.com/quotes']
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
            
    def parse(self,response):
        for elemento in response.xpath('//div[@class="quote"]'):
            yield {
                'frase':elemento.xpath(".//div[@class='quoteText']/text()").get().strip(),
                'autor':elemento.xpath(".//span[@class='authorOrTitle']/text()").get().strip().replace(',',''),
                'tags':elemento.xpath(".//div[@class='greyText smallText left']/a/text()").getall()
            }
            
            
    # Como varrer várias páginas
    # Tentar encontrar o botao de proximo, se encontrar ou varer as paginas
    # Se nao encontrar a automação para
    #o url join literalmente junta um url com alguma string se desejável trocar de página
    
    
        try:
            link_next_page = response.xpath("//div/a[@class='next_page']/@href").get()
            if link_next_page is not None:
                link_complet = response.urljoin(link_next_page)
                yield scrapy.Request(url=link_complet,callback=self.parse)
            
        except:
            print("Chegamos na última página...")