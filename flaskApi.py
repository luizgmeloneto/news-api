from flask import Flask, jsonify, render_template
from google.cloud import bigquery
from google.oauth2 import service_account
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from google.cloud import bigquery
from google.cloud.bigquery import Table
from google.oauth2 import service_account


PATH_CRED_SA = 'config/big_query.json'


app = Flask(__name__)

project_id= "news-information-423715"
destination_table= "news.raw"


@app.route('/')
def dados_do_bigquery():
    # Configurar o cliente do BigQuery
    creds = service_account.Credentials.from_service_account_file(PATH_CRED_SA)
    client = bigquery.Client(project=project_id,credentials=creds)
    # Query para puxar os dados
    query = (
        """SELECT * 
        FROM `news-information-423715.news.raw` 
        LIMIT 10"""
    )

    # Executar a query
    query_job = client.query(query)

    # Transformar os resultados em um formato que possa ser retornado pelo Flask (por exemplo, JSON)
    results = [dict(row) for row in query_job]

    return results

if __name__ == '__main__':
    app.run(debug=True)
