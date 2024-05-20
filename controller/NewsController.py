import requests
import json
import pandas as pd
from pandas import DataFrame
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from datetime import timedelta
from google.cloud import bigquery
import pandas_gbq
import os
from requests import get
from requests import get
from json import load
import time
import numpy as np


class NewsController:
    
    def __init__(self, sources, apiKey):
    
        self.sources = sources
        self.apiKey = apiKey

    def auth(self):
        #função que verifica se a autenticação foi bem sucedida
        params = {
            "sources": self.sources,
            "apiKey": self.apiKey
        }

        
            # URL da API de Anúncios do Facebook
        url = "https://newsapi.org/v2/top-headlines"
        print(url)
            # Faz a requisicao para cada account_id
        response = get(url, params)
        if response.status_code == 200:
                print("Autenticação bem sucedida!\n")
        else:
                print("Autenticação falhou!\n")
                raise Exception("Autenticação Falhou" + response.text)
                    
        
    def is_auth(self):
        return self.auth()
    
    
    def request_report(self, df):   
        

        params = {
            "sources": self.sources,
            "apiKey": self.apiKey
        }
        

        # Lista de dados de reposta da requisicao

        url = "https://newsapi.org/v2/top-headlines"
                        # Faz a requisicao para cada account_id
        response = get(url, params)
        params.pop('after', None)
            
                

        if response.status_code == 200:
            print('Dados Encontrados\n')

        else:
            'Sem Dados\n'

        # Extrai apenas os valores de data de cada resposta
    
        # Cria o DataFrame apenas com os valores de data
        self.df = response.json()['articles']
        self.df = pd.json_normalize(self.df)
        self.df = self.df.rename(columns={"source.id":"source",
                        "source.name":"source_name"})
        self.df['publishedAt'] = self.df['publishedAt'].astype(str)

        print(self.df)
        return self.df
    

