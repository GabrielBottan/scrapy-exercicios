import scrapy



class IndeedPythonSpider(scrapy.Spider):
    #Identidade
    name = 'achar_vagas_python'
    
    
    #Request
    def start_requests(self):
        urls = ["https://br.indeed.com/jobs?q=python&l=&from=searchOnHP&vjk=02f2747e765eac4a"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)       
    
    
    #Response
    def parse(self, response):
        #varer cada grupo deinformação e seus detalhes
        for vagas in response.xpath('//td[@class="resultContent css-1qwrrf0 eu4oa1w0"]'):
            yield {
                "cargo": vagas.xpath('.//span[1]//text()').get(),
            }   
    