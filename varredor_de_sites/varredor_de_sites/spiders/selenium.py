import scrapy
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as CondicaoExperada
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from scrapy.selector import Selector
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    LOGGER.setLevel(logging.WARNING)
    arguments = ['--lang=pt-BR', '--window-size=1920,1080', '--headless']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    return driver, wait


class F1RaceSpider(scrapy.Spider):
    #identidade
    name = "bot"
    
    

    #request
    def start_requests(self):
        urls = ["https://f1races.netlify.app/?_gl=1*fhm61s*_ga*MTMzNTc2MDA0MS4xNzA2NjIxNzY4*_ga_37GXT4VGQK*MTcxMzc5NjAyMi4xMDYuMS4xNzEzNzk4ODQ1LjAuMC4w"] 
    
    
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse,meta={'next_url':url})
            
            
            
   
   
    #response
    def parse(self, response):
        driver,wait = iniciar_driver()
        driver.get(response.meta['next_url'])
        sleep(10)
    
        
        
        
        
        response_webdriver = Selector(text=driver.page_source)
        
        for infos in response_webdriver.xpath("//div[@class='sc-bZQynM llbHfj']"):
            yield {
                "nome": infos.xpath('./div[1]/text()').get(),
                "local": infos.xpath('./div[2]/text()').get(),
                "vencedor": infos.xpath('.//a/text()').get(),
                "tempo": infos.xpath('./div[4]/text()').get()
            }
        
        driver.close()
       
    
    