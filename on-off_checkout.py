import os
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_URL = "https://suaURL.sults.com.br/"
USER = "SEU_USUÁRIO"
PASS = "SUA_SENHA"
LOG_FILE = "historico_auditoria.txt"

# Aqui o caractere "X" está substituindo números referentes a perfis e funcionalidades que variaM de empresa para empresa!
URLS_TO_TOGGLE = [
    "https://suaURL.sults.com.br/permissao/acesso-tela/XXX/X/XXX",
    "https://suaURL.sults.com.br/permissao/acesso-tela/XXX/X/XXXX",
    "https://suaURL.sults.com.br/permissao/acesso-tela/XXX/X/XXXX"
]

def registrar_log(mensagem):
    timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {mensagem}\n")
    print(mensagem)

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--log-level=3")

print(f"Bloqueio de pedidos iniciou as {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 20)

try:
    driver.get(LOGIN_URL)

    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form:login-usuario-inputText"]'))).send_keys(USER)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form:login-user-password"]'))).send_keys(PASS)

    btn_login = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[contains(text(), 'Entrar')] | //button[contains(text(), 'Entrar')]")))
    btn_login.click()

    # Nota: O Sults não utiliza o termo "Home" na URL de seu endereço principal, mas o "solucoes"
    wait.until(EC.url_contains("solucoes"))

    for url in URLS_TO_TOGGLE:
        print(f"Navegando para: {url}")
        driver.get(url)
        try:
            css_selector = "tr[data-rk='0_2'] div.ui-inputswitch"
            toggle_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", toggle_btn)
            driver.execute_script("arguments[0].click();", toggle_btn)
            registrar_log(f"SUCESSO: Alteração realizada na URL final ...{url[-5:]}")

        except Exception as e:
            registrar_log(f"ERRO: Falha ao alterar URL {url}. Detalhe: {e}")
            timestamp_erro = datetime.now().strftime('%H%M%S')
            driver.save_screenshot(f"erro_log_{timestamp_erro}.png")

except Exception as main_error:
    registrar_log(f"ERRO FATAL: O script parou inesperadamente. {main_error}")
    if 'driver' in locals():
        driver.save_screenshot(f"erro_fatal_{datetime.now().strftime('%H%M%S')}.png")

finally:
    if 'driver' in locals():
        driver.quit()
    registrar_log(">>> FIM DO PROCESSO\n" + "-" * 50)