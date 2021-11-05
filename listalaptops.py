# importacao de bibliotecas
import json
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from model import Notbook


# navegador acessa url da página web
navegador = webdriver.Chrome()
navegador.get("https://webscraper.io/test-sites/e-commerce/allinone/product/545")
time.sleep(2)

# clica no menu computers
navegador.find_element_by_class_name('category-link').click()
time.sleep(1)
navegador.find_element_by_class_name('subcategory-link').click()

# coloca todas as div de notbook em uma lista de elementos
notbooks = navegador.find_elements_by_class_name('col-sm-4')

# itera por cada objeto notbook
for notbook in notbooks:
    marca = notbook.find_element_by_tag_name('a').get_attribute('title')
    # verifica se o Notbook é da marca Lenovo
    if(marca[:6] == 'Lenovo'):
        # marca
        print(notbook.find_element_by_tag_name('a').get_attribute('title'))
        # pega primeiro tag h4 com preco
        print(notbook.find_element_by_tag_name('h4').text)
        # url imagem
        print(notbook.find_element_by_tag_name('img').get_attribute('src'))
        # reviews
        print(notbook.find_element_by_class_name('ratings').
              find_element_by_class_name('pull-right').text)
        # estrelas 
        print("Estrelas: " + notbook.find_element_by_class_name('ratings').
              find_elements_by_tag_name('p')[1].get_attribute('data-rating'))
        
        print(notbook.find_element_by_class_name('description').text)
        print()

#próximo passo colocar todos objetos em uma lista e gerar um arquivo json        


