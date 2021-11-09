# importacao de bibliotecas
import json
from selenium import webdriver
import time
from models.model import Notbook

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
# poderia colocar os objetos em uma lista
lista = []
def retorna_str_json():
    # itera por cada objeto de notbooks
    for notbook in notbooks:
        marca = notbook.find_element_by_tag_name('a').get_attribute('title')
        # verifica se o Notbook é da marca Lenovo
        if(marca[:6] == 'Lenovo'):
            marca = notbook.find_element_by_tag_name('a').get_attribute('title')
            # pega primeiro tag h4 com preco
            preco = notbook.find_element_by_tag_name('h4').text
            imagem = notbook.find_element_by_tag_name('img').get_attribute('src')
            resenhas = notbook.find_element_by_class_name('ratings').\
                find_element_by_class_name('pull-right').text
            estrelas = notbook.find_element_by_class_name('ratings').\
                find_elements_by_tag_name('p')[1].get_attribute('data-rating')
            descricao = notbook.find_element_by_class_name('description').text
            
            obj = Notbook(marca, preco, imagem, resenhas, estrelas, descricao)
            lista.append({ "marca": obj.marca, "preco": obj.preco \
                 , "imagem": obj.imagem , "avaliacoes":  obj.resenhas \
                , "estrelas": obj.estrelas, "descricao ":obj.descricao })
    return lista
                  
print(retorna_str_json()) 

# gera arquivo .json passando uma estrutura python
with open('dados.json', 'w') as json_file:
    json.dump(lista, json_file, indent=4)


