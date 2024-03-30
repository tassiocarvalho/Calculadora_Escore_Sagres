**Título: Automatização da Calculadora de Escore para o Sagres usando Selenium**

**Introdução:**
Este projeto tem como objetivo automatizar o cálculo do escore para o sistema acadêmico Sagres da Universidade Estadual de Feira de Santana (UEFS) utilizando a biblioteca Selenium em Python. O Sagres é um sistema utilizado por estudantes para acessar informações acadêmicas, como notas e faltas, e calcular o escore para determinado período letivo.

**Funcionalidades:**
1. **Acesso ao Sistema:** O programa utiliza o Selenium para acessar a página de login do Sagres e aguarda a interação manual do usuário para inserir suas credenciais e fazer o login.
2. **Extração de Dados:** Após o login bem-sucedido, o programa extrai automaticamente as notas e as cargas horárias das disciplinas para o cálculo do escore.
3. **Cálculo do Escore:** Com as notas e cargas horárias obtidas, o programa realiza o cálculo do escore conforme as especificações do Sagres.
4. **Interface de Usuário Simples:** O programa fornece uma interface de usuário simples para escolher entre adicionar disciplinas de semestre extraordinário, calcular o escore ou exibir a lista de notas e horários.

**Tecnologias Utilizadas:**
- **Python:** Linguagem de programação utilizada para desenvolver o programa.
- **Selenium:** Biblioteca utilizada para automatizar a interação com o navegador web.
- **GitHub:** Plataforma utilizada para hospedar o código-fonte e o documento do projeto.

**Instruções de Uso:**
1. Clone o repositório do projeto do GitHub em sua máquina local.
2. Certifique-se de ter o Python e o Selenium instalados,
   instalando as bibliotecas necessárias utilizando o pip. Abra o terminal ou prompt de comando e execute os seguintes comandos:
   ```
   pip install selenium
   pip install webdriver_manager
   ```
   Isso irá instalar as bibliotecas Selenium e Webdriver Manager, que são utilizadas para automatizar a interação com o navegador web.
4. Execute o script `score.py`.
5. Siga as instruções apresentadas na interface de usuário para adicionar disciplinas de semestre extraordinário, calcular o escore ou exibir a lista de notas e horários.
6. Após a conclusão das operações desejadas, pressione Enter para sair do programa.

**Considerações Finais:**
Este projeto demonstra como é possível automatizar tarefas repetitivas e simplificar processos utilizando ferramentas como o Selenium em conjunto com Python. A automação da calculadora de escore para o Sagres oferece mais praticidade aos estudantes ao calcular seu desempenho acadêmico de forma rápida e eficiente.

**Observações testes realizados em 2024 em uma conta do sagres com todas notas fechadas, o código não faz calculo com algumas disciplinas em aberto(disciplinas que os professores não fecharam nota) por enquanto!**        
