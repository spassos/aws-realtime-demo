# Projeto de ingestão de dados em tempo real 

### Ferramentas utilizadas 

- [Lambda](https://aws.amazon.com/pt/lambda/) 
- [SNS](https://aws.amazon.com/pt/sns)
- [S3](https://aws.amazon.com/pt/s3/)
- [Firehose](https://aws.amazon.com/pt/kinesis/data-firehose/)
- [DynamoDB](https://aws.amazon.com/pt/dynamodb)
- [Databricks](https://www.databricks.com/)
- [Delta Lake](https://delta.io/)
- [Spark Streaming](https://spark.apache.org/docs/latest/streaming-programming-guide.html)
- [Python](https://www.python.org/)
- [Pyspark](https://spark.apache.org/docs/latest/api/python/)

#### Projeto Python Lambda Serveless

Para rodar o projeto é necessário configurar o aws cli na sua máquina e em seguida instalar o poetry e o zappa com os seguintes comandos:

- Instalar e configurar um ambiente virtual python (Pycharm faz automático, mas caso precise configurar manualmente segue o material)

[venv](https://realpython.com/python-virtual-environments-a-primer/)

- Instalar e configurar o AWS cli no ambiente:

[Install](https://docs.aws.amazon.com/pt_br/cli/latest/userguide/getting-started-install.html)
[Config](https://docs.aws.amazon.com/pt_br/cli/latest/userguide/cli-configure-quickstart.html)

- Configurar o [poetry](https://python-poetry.org/docs/) no ambiente:
```shell
pip install poetry
poetry install
```
- Configurar o [Zappa](https://github.com/zappa/Zappa)

````shell
poetry add --dev zappa
zappa init
````
- Fazer o deploy do projeto python na AWS Lambda

````shell
zappa deploy dev
````

- Deletar o projeto no AWS Lambda
````shell
zappa undeploy dev
````

- Atualizar o projeto no AWS Lambda existente
````shell
zappa update dev
````
> ⚠️ **O zappa pode ser uma opção para CI/CD da solução**