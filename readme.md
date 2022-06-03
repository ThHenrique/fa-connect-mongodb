# Flask API - Python 🐍

Neste guia iremos configurar o ambiente de desenvolvimento com a instalação e configuração de um ambiente isolado, instalação dos requisitos do projeto, instalação e utilização do Flask e utilização do MongoDB, Redis e Cassandra.


---

### Requisitos mínimos

1. _Python_


---

## Instalação e configuração do ambiente virtual

**Verifique se o pip está instalado**

```bash
  python -m pip --version
```

_Siga a documentação oficial do pip caso você não tenha instalado:_

[Installation - pip documentation v21.1](https://pip.pypa.io/en/stable/installing/)

<br/>

**Instalando o virtualenv**

_Ferramenta para criar ambientes Python isolados._

```bash
  python -m pip install virtualenv
```

**Clone o repositório do backend**

```bash
  git clone https://github.com/ThHenrique/fa-connect-mongodb.git
```

**Abra o projeto no vsCode**

```bash
cd fa-connect-mongodb
code .
```

**Abra o terminal do VsCode e Configure o ambiente**

```bash
python -m venv venv
```

**Ative o ambiente virtual**

<details>
  <summary>Windows PowerShell</summary>

  ```powershell
    venv\Scripts\activate
  ```
</details>

<details>
  <summary>Linux</summary>

  ```bash
    . venv/bin/activate
  ```
</details>


**Instalando as dependências do projeto**

```bash
pip install -r requirements.txt
```

**Setup Completo :)**

---

<br/>
<br/>

# Configurando a conexão com os bancos de dados
<details>
  <summary>MongoDB 🍃</summary>
  
  ### Para realizar conexão com o MongoDB é necessário alterar o usuário e senha no arquivo connectDb em **src/connectDb.py**. Caso necessário, entre em contato comigo.

  ``` python
    db = pymongo.MongoClient("mongodb+srv://<user>:<password>@fa-starting-no-sql.6vnsq.mongodb.net/")
  ```
</details>


<details>
  <summary>Redis 🔴🟥🔺</summary>
  
  ### Para realizar conexão com o Redis é necessário alterar o host, port e password no arquivo connectRedis em **src/connectRedis.py**. Caso necessário, entre em contato comigo.

  ``` python
    db = redis.Redis(
        host='<host>',
        port='<port>',
        password='<password>',
        decode_responses=True
      )
  ```
</details>

<details>
  <summary>Cassandra 👁‍🗨</summary>

  ### Para realizar conexão com o Cassandra é necessário alterar o ASTRA_DB_ID, ASTRA_DB_REGION e ASTRA_DB_APPLICATION_TOKEN no arquivo connectCassandra em **src/connectCassandra.py**. Caso necessário, entre em contato comigo.

  ``` python
    ASTRA_DB_ID = '<BD-ID>'
    ASTRA_DB_REGION = '<DB-REGION>'
    ASTRA_DB_APPLICATION_TOKEN = '<token>'
    ASTRA_DB_KEYSPACE = 'mercadolivre'
    TEST_COLLECTION_NAME = "test"
  ```
</details>

<br/>
<br/> 

## Instalação e configuração do Insomnia
<details>
  <summary>Insomnia</summary>

  Siga a documentação oficial do insomnia caso você não tenha instalado:_

  [Installation - insomnia](https://insomnia.rest/download)

  Caso você não conheça esse software veja o link a seguir para aprender:_

  [Get Started - insomnia](https://docs.insomnia.rest/insomnia/send-your-first-request)

  Você pode baixar e importar no insomnia a configuração de ambiente que deixei na pasta raiz do projeto. Caso tenha alguma dúvida de como importar essa configuração, leia o link abaixo.

  [Import and Export Data - insomnia](https://docs.insomnia.rest/insomnia/import-export-data)


  **/Insomnia_2022-04-25.json**

  ---

  Caso tenha algum problema no processo, entre em contato.
</details>


<br/>

---

# Utilizando o FLASK 🌶️

Com o ambiente virtual ativado ...

```bash
python main.py
```

O servidor foi iniciado e pode ser acessado em [localhost](http://localhost:5000/).

A porta padrão do projeto é 5000.

---


