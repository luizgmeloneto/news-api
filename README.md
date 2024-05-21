# Lima Challenge

Repositório com o código e recursos necessários para o desafio técnico da Lima.

### Descrição da Arquitetura

A arquitetura do projeto é composta por várias partes:

- **main**: É aqui que vamos fazer o carregamento dos nossos dados vindos da pasta **"data_request"** e onde faremos todas as nossas chamadas de funções.
- **config**: Contém as credenciais necessárias do Google Cloud Platform (GCP).
- **controller**: É aqui onde está todo o racional do projeto. Nela faremos nossa autenticação, requisição e validação dos dados vindos da news-API.
- **data_request**: Contém todos os parâmetros que iremos precisar para o consumo da news-API.
- **database**: Nesta parte do código iremos fazer nossa autenticação do BigQuery e exportação dos dados para a tabela escolhida.
- **flaskApi**: Aqui é onde iremos criar uma API para disponibilizar os dados armazenados no BigQuery para o usuário.

## Como usar este projeto

Siga as instruções abaixo para clonar e executar este projeto em sua máquina local.

### Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:

- Python 3
- Flask
- Google Cloud SDK

### Clonar o repositório

```bash
git clone 'https://github.com/luizgmeloneto/news-api.git'  
```

## Executar o código

    Certifique-se de configurar suas credenciais do GCP na pasta Credentials.
    Execute o código main.py para coleta dos dados e envio para o BigQuery.
    Execute o código flaskApi.py para criar nossa API e retornar os dados do BigQuery para o usuário.

## Como alterar a requisição da API do BigQuery

    Dentro do arquivo flaskApi.py, a variável query pode ser alterada de acordo com a vontade do usuário e a 
    partir dela podemos fazer filtros e até mesmo alterar a tabela que iremos consultar os dados

## Como acessar os dados pelo flaskApi
    Assim que executarmos nosso arquivo flaskApi.py irá aparecer no terminal a URL que deverá ser acessada para 
    ter a visão dos dados vindos do BigQuery. Ex: * Running on http://127.0.0.1:5000
    
    Para finalizar a execução, basta apertar CTRL + C.
    
## Resultados

    Em results.json podemos ter uma amostra de como serão os resultados oriundos da news-API.

## Autor

Luiz Guimarães
