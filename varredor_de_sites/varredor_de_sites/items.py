# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join

def tirar_espaco_em_branco(valor):
    return valor.strip()


def processar_caracteres_especiais(valor):
    return valor.replace(u"\n","")

def tirar_tracinho(valor):
    return valor.replace("-"," ")

def nomes_em_maiusculo(valor):
    return valor.upper()


class VarrerFrases(scrapy.Item):
    #defina primeiro cada campo que quer processar
    autor = scrapy.Field(
        input_processor=MapCompose(tirar_espaco_em_branco, processar_caracteres_especiais, nomes_em_maiusculo),
        output_processor=TakeFirst()
    )
    
    frase = scrapy.Field(
        input_processor=MapCompose(tirar_espaco_em_branco, processar_caracteres_especiais),
        output_processor=TakeFirst()
    )
    
    tags = scrapy.Field(
        input_processor=MapCompose(tirar_tracinho),
        output_processor=Join(';')
    )
