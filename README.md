# Sistema de Recomendação - Conceitos

### Alunos:
- Felipe Nicoletti Reis Mario
- Gabriel Fernandes Giraud

## Configurando o banco de dados

Para executar esse projeto é necessário ter instalado na maquina o BD Maria DB

Se já tiver instalado basta executar o arquivo DDL.sql da pasta "db" para setar o banco de dados

## Baixando dependencias

Para baixar dependências bastar executar o seguinte comando:

```pip install -r requirements.txt```

Além disso será necessário baixar a biblioteca apriori para a execução da opção de Apriori, para isso rode o seguinte comando:

```git clone https://github.com/FelipeNicolettiRMario/explore-basket.git```

## Setando Variáveis de ambiente

Para o funcionamento do projeto é necessário que sejam setado
variáveis de ambiente em um arquivo '.env' na raiz do projeto.
Os dados que precisam ser setados terão que ter esse modelo

```
user=<USUARIO MARIADB>
password=<SENHA MARIADB>
host=<HOST MARIADB>
port=<PORTA MARIADB>
database=<NOME DA BASE DE DADOS MARIADB>
table=<NOME DA TABELA MARIADB>
BD_URI=mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}
```

## Para executar a aplicação
```python run.py```
