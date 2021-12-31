import requests
from bs4 import BeautifulSoup
from lxml import etree


result = requests.get("https://precodoscombustiveis.com.br/pt-br/city/brasil/rio-de-janeiro/rio-de-janeiro/3239")
soup = BeautifulSoup(result.text, 'html.parser')
dom = etree.HTML(str(soup))

etanol = dom.xpath("/html/body/div[2]/div[3]/div[2]/div[2]/div/span[1]")[0].text
etanol_preco = dom.xpath("/html/body/div[2]/div[3]/div[2]/div[2]/div/span[3]")[0].text
print(dom.xpath("//*[@id='ListCountry']/div[3]/div[2]/div[4]/div/span[3]"))