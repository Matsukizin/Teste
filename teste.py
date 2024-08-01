from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Configuração do serviço do navegador
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# Passos para realizar as ações no site

# 1 - Abrir o site
navegador.get("https://www.salao99.com.br/conta/login?continuacao=https%3A%2F%2Fsalao99.com.br%2Fenterprise%2Fsistema%2Fpainel")
sleep(10)

# 2 - Login no site
# navegador.find_element(By.XPATH, '')
# driver = webdriver.Chrome()
navegador.find_element(By.CLASS_NAME, "xemail")
  
navegador.find_element(By.XPATH, '//*[@id="xsenha"]').send_keys("")
navegador.find_element(By.XPATH, '//*[@id="formLogin"]/div[3]/div[2]/button/span[1]').click()
sleep(10)  # Espera para o login ser processado

# 3 - Abrir atendimentos
# Implemente o código para navegar até a seção de atendimentos aqui
# Exemplo de navegação para "Atendimentos" se a opção estiver disponível no menu
print("Atendimentos")

# 4 - Clicar em "Adicionar"
sleep(20)
navegador.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div[2]/div/div/div[1]/div/div[2]/button/span[1]').click()

# 5 - Colocar nome da cliente
with open('Comandas.txt', 'r') as arquivo:
    for linha in arquivo:
        nome, profissional, servico_feito, horario = linha.strip().split(',')
        
        # Inserir nome do cliente
        input_nome_cliente = navegador.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[3]/div/div[1]/div/div/div/input')
        input_nome_cliente.send_keys(nome)
        sleep(2)  # Espera para que os resultados carreguem
        
        elementos = navegador.find_elements(By.TAG_NAME, "div")

        
        # Selecionar o cliente (supondo que um clique no nome do cliente seja necessário)
        cliente_selector = By.XPATH, f"//*[text()='{nome}']"  # Atualize o seletor conforme a estrutura HTML
        navegador.find_element(*cliente_selector).click()
# //*[@id="root"]/div[2]/div/div[3]/div/div[2]/div[2]/div[1]/div/div/div[4]/div/div[1]/p
# <p class="MuiTypography-root-278 jss8090 MuiTypography-body1-280">Cliente</p>
# 
        # 6 - Selecionar o nome da cliente (este passo pode ser redundante, já está feito acima)
        
        

        # 7 - Apertar no "+"
        navegador.find_element(By.XPATH, 'caminho_para_botoao_mais').click()  # Atualize o XPath

        # 8 - Apertar em "Novo Atendimento"
        navegador.find_element(By.XPATH, 'caminho_para_novo_atendimento').click()  # Atualize o XPath

        # 9 - Adicionar profissional
        # Implementar código para selecionar o profissional aqui
        # Exemplo: navegador.find_element(By.XPATH, 'caminho_para_selecionar_profissional').click()

        # 10 - Selecionar profissional
        # Implementar código para selecionar o profissional aqui

        # 11 - Selecionar serviço
        # Implementar código para selecionar o serviço aqui

        # 12 - Adicionar horário
        # Implementar código para adicionar horário aqui

        # 13 - Salvar
        # Implementar código para salvar o atendimento aqui

        # 14 - Voltar para cliente
        # Implementar código para voltar à tela do cliente aqui

        # 15 - Faturar
        # Implementar código para iniciar o processo de faturamento aqui

        # 16 - Selecionar serviço para faturar
        # Implementar código para selecionar o serviço a ser faturado aqui

        # 17 - Continuar
        # Implementar código para continuar o processo de faturamento aqui

        # 18 - Confirmar
        # Implementar código para confirmar o faturamento aqui

        # 19 - Adicionar pagamento
        # Implementar código para adicionar pagamento aqui

        # 20 - Forma de pagamento
        # Implementar código para selecionar a forma de pagamento aqui

        # 21 - Salvar
        # Implementar código para salvar o pagamento aqui

        # 22 - Apertar no "X"
        # Implementar código para fechar a janela ou modal aqui

        # 23 - Confirmar
        # Implementar código para confirmar o fechamento aqui

# Espera para que todas as ações sejam realizadas
sleep(5000)
navegador.quit()
