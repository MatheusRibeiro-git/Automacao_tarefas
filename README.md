# Automação de Cadastro de Produtos

Este projeto em Python automatiza o processo de **login em um sistema web** e o **cadastro de produtos** a partir de uma base de dados CSV.  
A automação é feita utilizando a biblioteca **PyAutoGUI**, que simula cliques, digitação e rolagem de tela, além do **Pandas** para leitura da planilha de produtos.

---

## 🚀 Funcionalidades
- Abre automaticamente o navegador **Google Chrome**.
- Acessa a página de login da empresa.
- Preenche as credenciais de login (e-mail e senha).
- Lê os produtos de uma planilha `produtos.csv`.
- Preenche o formulário do site com os dados de cada produto.
- Envia os cadastros automaticamente.

---

## 📂 Estrutura do Projeto
- automatizar.py # Script principal de automação
- auxiliar.py # Script auxiliar para capturar coordenadas (x, y)
- produtos.csv # Planilha com os produtos a cadastrar
- README.md # Documentação

---

## 🛠️ Tecnologias Utilizadas
- [Python 3.x](https://www.python.org/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
- [Pandas](https://pandas.pydata.org/)

---

## 📋 Pré-requisitos
1. Instale as dependências:
   ```bash
   pip install pyautogui pandas

▶️ Como Executar

1. Coloque o arquivo produtos.csv na mesma pasta do script.
2. Rode o programa:
   python automatizar.py
3. O navegador abrirá, fará o login e começará a cadastrar os produtos.

## ⚠️ Observações Importantes

- O script usa coordenadas fixas (x=600, y=425) para clicar no campo inicial do formulário.
Para ajustar à sua tela, use o auxiliar.py, que imprime no terminal a posição do mouse após 5 segundos:
  python auxiliar.py
Coloque o mouse sobre o campo desejado e aguarde. A posição correta será exibida no console.
- Não mexa no computador durante a execução para evitar erros na automação.
- O campo obs é opcional. Caso esteja vazio no CSV, ele será ignorado.

## 📖 Descrição dos Arquivos

🔹 automatizar.py

Script principal que:
1. Lê os dados da planilha produtos.csv.
2. Abre o Chrome e acessa a URL do sistema.
3. Faz login com e-mail e senha.
4. Percorre a planilha cadastrando os produtos no sistema.

🔹 auxiliar.py

Script auxiliar usado para capturar a posição do mouse:
  import pyautogui
  import time
  
  posicao = pyautogui.position()
  time.sleep(5)
  print(posicao)

## 📌 Aviso

Este código tem fins educacionais (curso Intensivão Python da Hashtag Treinamentos).
Não utilize em sistemas reais sem autorização.
