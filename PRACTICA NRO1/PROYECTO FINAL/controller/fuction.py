from config.app import *
from modelos.model import *
# 
import pandas as pd

def IngestDataProducts(app:App):
    bd=app.bd
    conn=bd.getConection()
    dataPais=GetDataSourcePais()
    


def GetDataSourcePais():
    pathData="//workspaces/WORKSPACEPY1/PRACTICA NRO1/PROYECTO FINAL/modelos/files/datafuente.xls"
    df=pd.read_excel(pathData,sheet_name="Orders")
    print(df.shape)
    print(df.keys())
    df_country=df['Country'].unique()
    print(df_country.shape)
    country_tuples = [(country,) for country in df_country] 
    