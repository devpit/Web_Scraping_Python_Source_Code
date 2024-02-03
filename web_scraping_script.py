# ATENÇÃO!!
# ANTES DE RODAR O SCRIPT, RECOMENDO ULTILIZAR UMA VPN
# USANDO A VPN, VOCÊ IRÁ ESCONDER SEU IP REAL NA HORA DE FAZER A SOLICITAÇÃO
# EVITANDO DE FICAR SALVO NOS LOGS DO SITE 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

# URL do site que você deseja acessar
url = "https://www.example.com"

# Fazer uma solicitação GET para a URL
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Capturar o conteúdo da página
    conteudo = response.text

    # Salvar o conteúdo em um arquivo de texto
    with open("source_code.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)

    print("Conteúdo salvo em 'source_code.txt'")
else:
    print(f"A solicitação falhou com código de status {response.status_code}")

# Configurar as opções do Chrome para o modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")

# Inicialize o driver do Chrome com as opções
driver = webdriver.Chrome(options=chrome_options)

# Acesse a URL (mesmo que não seja válida)
driver.get(url)

# Capture uma captura de tela da página atual
screenshot = driver.get_screenshot_as_file("screenshot.png")
print("Imagem capturada e salva em 'screenshot.png'")

# Feche o navegador
driver.quit()
