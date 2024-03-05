from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get("https://academico.uefs.br/PortalSagres/Acesso.aspx?st=1")

notas = []
limites_faltas = []
# Aguarde até que o usuário faça login manualmente
input("Faça login manualmente e pressione Enter quando terminar...")

# Verificar se o login foi bem-sucedido verificando a URL atual
if "PortalSagres" in navegador.current_url:
    print("Login realizado com sucesso!")
else:
    print("Erro ao fazer login.")

# Encontra o link pelo atributo href
link_entrar_v1 = navegador.find_element("link text", "Portal do aluno")
link_entrar_v1.click()

time.sleep(1)

# Execute um script JavaScript para clicar no elemento do menu
script = """
document.getElementById("ControleMenuSlide").click();
"""
navegador.execute_script(script)

time.sleep(1)

# Encontra o link pelo atributo href
link_entrar_v1 = navegador.find_element("link text", "Notas e faltas")
link_entrar_v1.click()

# Encontrar o elemento select
select_element = Select(navegador.find_element(By.ID, "ctl00_MasterPlaceHolder_ddPeriodosLetivos_ddPeriodosLetivos"))

# Inicializar uma lista vazia para armazenar os valores
valores = []

# Iterar sobre as opções e extrair o texto selecionado
for option in select_element.options:
    valores.append(option.text.strip())

# Exibir a lista de valores
print(valores)

contador = 0

while contador < len(valores):
    time.sleep(2)
    html_content = navegador.page_source
    # Espera explícita até que pelo menos um elemento seja encontrado
    wait = WebDriverWait(navegador, 2)

    # Iterar sobre os elementos <span> com IDs correspondentes às notas
    for i in range(12):  # Assumindo que os IDs seguem o padrão fornecido
        id_span = f"ctl00_MasterPlaceHolder_ucRepeater_ctl{i:02d}_ucItemBoletim_lblMediaFinal"
        try:
            # Espera até que o elemento esteja presente na página
            nota_element = wait.until(EC.presence_of_element_located((By.ID, id_span)))
            # Obter o valor do atributo textContent do elemento <span>
            nota = nota_element.get_attribute("textContent").strip()
            if nota.startswith('-'):
                nota = '0'
            # Substituir vírgulas por pontos
            nota = nota.replace(',', '.')
            notas.append(nota)
        except Exception as e:
            break

    # Exibir a lista de notas
    print(notas)

    # Lista para armazenar os limites de faltas

    # Espera explícita até que pelo menos um elemento seja encontrado
    wait = WebDriverWait(navegador, 2)

    # Iterar sobre os elementos <span> com IDs correspondentes aos limites de faltas
    for i in range(12):  # Assumindo que os IDs seguem o padrão fornecido
        id_span = f"ctl00_MasterPlaceHolder_ucRepeater_ctl{i:02d}_ucItemBoletim_lblValorLimiteFaltas"
        #print("Tentando encontrar elemento com ID:", id_span)  # Debugging
        try:
            # Espera até que o elemento esteja presente na página
            limite_faltas_element = wait.until(EC.presence_of_element_located((By.ID, id_span)))
            # Obter o valor do atributo textContent do elemento <span>
            limite_faltas = limite_faltas_element.get_attribute("textContent").strip()

            # Converter o texto do limite de faltas conforme as especificações
            if limite_faltas.startswith("15"):
                limite_faltas = "60"
            elif limite_faltas.startswith("22"):
                limite_faltas = "90"
            elif limite_faltas.startswith("7"):
                limite_faltas = "30"
            elif limite_faltas.startswith("11"):
                limite_faltas = "45"

            limites_faltas.append(limite_faltas)
        except Exception as e:
            break

        
    # Exibir a lista de limites de faltas
    print(limites_faltas)

    # Localizar o elemento select pelo ID
    select_element = navegador.find_element(By.ID, "ctl00_MasterPlaceHolder_ddPeriodosLetivos_ddPeriodosLetivos")

    # Inicializar o objeto Select
    select = Select(select_element)

    # Encontrar a opção atualmente selecionada
    opcao_atual = select.first_selected_option

    # Obter o valor da próxima opção
    proxima_opcao_valor = None
    for option in select.options:
        if option == opcao_atual:
            proxima_opcao_valor = select.options[select.options.index(option) - 1].get_attribute("value")
            break

    # Se a próxima opção for encontrada, selecioná-la
    if proxima_opcao_valor:
        select.select_by_value(proxima_opcao_valor)

    # Localizar o botão "Exibir" pelo ID
    exibir_button = navegador.find_element(By.ID, "ctl00_MasterPlaceHolder_imRecuperar")

    # Clicar no botão "Exibir"
    contador += 1
    exibir_button.click()

def calcular(notas, limites_faltas):
    if len(notas) != len(limites_faltas):
        raise ValueError("As listas devem ter o mesmo comprimento")

    soma_numerador = 0
    soma_denominador = 0

    for nota, carga_horaria in zip(notas, limites_faltas):
        soma_numerador += float(nota) * float(carga_horaria)
        soma_denominador += float(carga_horaria)

    resultado = soma_numerador / soma_denominador
    return resultado

while True:    
    print("------------------Menu-----------------")
    print("[1] Adicionar disciplinas de semestre extraordinário")
    print("[2] Calcular Escore")
    print("[3] Lista de notas e horarios")
    escolha = int(input("Escolha a opção: "))
    
    if escolha == 1:
        num_disciplinas = int(input("Quantas disciplinas você tem de semestre extraordinário? "))
        counter = 0
        while counter < num_disciplinas:
            nota = float(input("Nota da disciplina: ").replace(',', '.'))  # Substitui vírgula por ponto e converte para float
            carga_horaria = int(input("Carga horária da disciplina: "))
            # Adicionar as notas e cargas horárias a uma lista ou fazer qualquer outra operação necessária
            notas.append(nota)
            limites_faltas.append(carga_horaria)
            counter += 1
    elif escolha == 2:
        print('a')
        # Chamar a função calcular
        resultado = calcular(notas, limites_faltas)
        print("Resultado do cálculo:", resultado)
    elif escolha == 3:
        print(notas)
        print(limites_faltas)
    else:
        print("Opção inválida")

# Aguarda alguns segundos antes de fechar o navegador (apenas para fins de demonstração)
input("aperte enter para sair")
navegador.quit()
