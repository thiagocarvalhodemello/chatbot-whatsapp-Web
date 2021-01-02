#Importar Bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#Navegar até Whatsapp Web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(10)

#Definir Grupos / Contatos e mensagens a ser enviadas
contatos = ['NOME_GRUPO','NOME_CONTATO']
mensagem = ['MENSAGEM A SER ENVIADA']

#Buscar Contatos/Grupos
def buscar_contato(contato):
  campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
  time.sleep(3)
  campo_pesquisa.click()
  campo_pesquisa.send_keys(contato)
  campo_pesquisa.send_keys(Keys.ENTER)

#Campo de mensagem privada
def enviar_mensagem(mensagem):
  campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
  campo_mensagem[1].click()
  time.sleep(3)
  campo_mensagem[1].send_keys(mensagem)
  campo_mensagem[1].send_keys(Keys.ENTER)

#Chamada das funções
for contato in contatos:
  buscar_contato(contato)
  enviar_mensagem(mensagem)
