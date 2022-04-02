import requests
from bs4 import BeautifulSoup
from lxml import etree


def getFuelList():
    html = requests.get("https://precodoscombustiveis.com.br/pt-br/city/brasil/rio-de-janeiro/rio-de-janeiro/3239")
    soup = BeautifulSoup(html.text, 'html.parser')
    dom = etree.HTML(str(soup))

    etanol = dom.xpath("/html/body/div[2]/div[3]/div[2]/div[2]/div/span[3]")[0].text
    gasoline = dom.xpath('//*[@id="ListCountry"]/div[3]/div[2]/div[1]/div/span[3]')[0].text
    diesel = dom.xpath('//*[@id="ListCountry"]/div[3]/div[2]/div[3]/div/span[3]')[0].text

    return [etanol, gasoline, diesel]
