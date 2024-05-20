import json
import pandas as pd
import pandas_gbq
from pandas.io import gbq
import os
from datetime import datetime, timedelta
from pytz import timezone
from controller.NewsController import NewsController
from database.BigQuery import BigQuery
from google.cloud import logging
import logging as log

def get_parameter(json, parametro):
    valor = json[parametro]
    if valor == None:
        raise Exception(f"O parâmetro {parametro} precisa ser preenchido.")
    return valor 

def main(request_json):

    with open(f"data_request/request.json") as f:
      request_json = json.load(f)
    
    
    log.info("Iniciando execução news-api")
        
    
    rst = None

    
    # variáveis de ambiente
    certificate_big_query = f"config/big_query.json"
   
    # days_reprocess = 14
   
    
    # parametros
    project_id = get_parameter(request_json, 'project_id')
    destination_table = get_parameter(request_json, 'destination_table')
    if_exists = get_parameter(request_json, 'if_exists')
    sources= get_parameter(request_json, 'sources')
    apiKey= get_parameter(request_json, 'apiKey')


    log.info(f"Project_id: {request_json['project_id']}")
    log.info(f"Project_id get_parameter: {project_id}")
    log.info(f"All JSON: {request_json}")
    
    

    
        
        # Cria uma instância de NewsController
    newsapi = NewsController(sources,apiKey)

        # Autentica a instância
    newsapi.auth()
            
        # Chama o método request_report com as datas e dataframe apropriados
    df = newsapi.request_report('df')

        # instancia classe responsável pela comunicação com BigQuery
    bq = BigQuery(certificate_big_query, project_id)

        ## efetua autenticação com BigQuery
    bq.auth()

        ## exporta os dados para o BigQuery
    rstLinesLoading = bq.export(df, destination_table, project_id, if_exists)

    rst = {
            "status": "Ok",
            "message": "Data Loaded",
            "lines": rstLinesLoading
            }
    
      


    return json.dumps(rst), 200, {'Content-Type': 'application/json'}

with open(f"data_request/request.json") as f:
      request_json = json.load(f)
      main(request_json)