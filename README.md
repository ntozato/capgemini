# Academia Java Capgemini 2022


## Contexto

Esse é um repositório criado para armazenar os desafios de programação do processo seletivo da Academia Java Capgemini 2022. Os desafios e testes unitários foram solucionados utilizando a linguagem Python.


## Requisitos

O Python já vem instalado nos sistemas Linux e Mac OS. O Python não vem instalado por padrão no Windows e o download deverá ser feito no site https://www.python.org/ além de algumas configurações extras.


## Instalação

Obs: Após clonar o repositório, para executar os testes será necessário primeiro **criar e ativar o ambiente virtual**, além de também instalar a biblioteca `pytest`. No terminal, isso pode ser feito através dos seguintes comandos:

1. Clone o repositório

- `git clone https://github.com/ntozato/capgemini.git`.
- Entre na pasta do repositório que você acabou de clonar:
  - `capgemini`

2. Crie e ative o ambiente virtual 

- `python3 -m venv .venv && source .venv/bin/activate`
- Caso dê algum erro pelo fato de o venv não estar instalado, utilize o comando `sudo apt install python3-venv` e rode o comando acima novamente.

3. Instale a biblioteca pytest

- `python3 -m pip install pytest`


## Desenvolvimento

Os desafios estão localizados dentro da pasta `challenges` em seus respectivos arquivos:

- `challenge1.py`
- `challenge2.py`
- `challenge3.py`

#### Visualizando retorno das funções
 
 Para visualizar o retorno de cada função, ao final de cada arquivo, há a chamada da função dentro de uma função `print()`. Insira no terminal o seguinte comando:
  
  - `python3 challenges/nome-do-arquivo.py`
 
 Exemplo: 
  
  No arquivo `challenges/challenge3.py`, na linha 23:
  
  `print(anagrams('ifailuhkqq'))`
  
  
Para visualizar o retorno da função, execute no terminal `python3 challenges/challenge3.py`. Para visualizar o retorno de diferentes entradas, você poderá substituir o valor passado como parâmetro 'ifailuhkqq' para o valor que desejar e executar o comando novamente.

  Exemplo:
  
    `print(anagrams('ovo'))  
    
 
## Testes

Os testes unitários estão localizados dentro da pasta `tests` em seus respectivos arquivos:

- `test_challenge1.py`
- `test_challenge2.py`
- `test_challenge3.py`

Com o ambiente virtual já criado e ativado e com a biblioteca pytest já instalada, para executar os testes basta usar o comando:

- `python3 -m pytest`
