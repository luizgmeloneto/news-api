from google.cloud import bigquery
from google.cloud.bigquery import Table
from google.oauth2 import service_account
from pandas.io import gbq
import pandas_gbq

## classe responsável por efetuar a comunicação com o banco de dados BigQuery
class BigQuery:

    client = None

    def __init__(self, certificado_path, project_id):
        self.certificado_path = certificado_path
        self.project_id = project_id

    def auth(self):
        self.credentials = service_account.Credentials.from_service_account_file(self.certificado_path)
        self.client = bigquery.Client(credentials=self.credentials, project=self.project_id)
        return self.is_auth()

    def is_auth(self):
        return self.client != None
    
    def query(self, sql):
        query = self.client.query(sql)
        return query.to_dataframe()

    def export(self, df, destination_table, project_id, if_exists):

        print(f"inserindo dados em project_id: {project_id}, destination_table: {destination_table}")
        pandas_gbq.to_gbq(df, destination_table=destination_table, project_id=project_id, if_exists=if_exists, credentials=self.credentials)

        return len(df.index)  