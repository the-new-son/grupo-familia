import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Configuração do perfil de usuário
profile_path = 'C:/Users/Dell/AppData/Local/Google/Chrome/User Data/Default'  # Insira o caminho para o perfil de usuário do Chrome, esse é um exemplo

# Configuração do driver do Chrome
options = Options()
options.add_argument(f'--user-data-dir={profile_path}')
options.add_argument("--start-maximized")  # Abre o Chrome maximizado
service = Service('C:/Program Files (x86)Google/Chrome/Application/chrome.exe')  # Insira o caminho para o executável do chromedriver

# Inicializa o driver do Chrome
driver = webdriver.Chrome(service=service, options=options)

# Abre o WhatsApp Web
driver.get('https://web.whatsapp.com')


# Verifica periodicamente a existência do elemento grupo_familia
grupo_familia_xpath = "//span[@title='NOME_DO_GRUPO']"
grupo_familia = None
while not grupo_familia:
    try:
        grupo_familia = driver.find_element(By.XPATH, grupo_familia_xpath)
    except:
        time.sleep(2)


# Localiza o grupo da família (altere o nome do grupo conforme necessário)
grupo_familia = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, grupo_familia_xpath)))
grupo_familia.click()

# Aguarda um tempo para garantir que a conversa seja carregada completamente
time.sleep(3)

# Envia a mensagem de "Bom dia!" no grupo da família
input_box = driver.find_element(By.XPATH, "//div[@contenteditable='true' and @title='Mensagem']")
input_box.send_keys("Booom dia famíliaaa!")
input_box.send_keys(Keys.ENTER)

# Aguarda um tempo para a mensagem ser enviada
time.sleep(3)

# Fecha o navegador
#driver.quit()
