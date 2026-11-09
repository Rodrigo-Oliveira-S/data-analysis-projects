import pandas as pd
from sqlalchemy import text
from database import get_engine

def importar_csv_para_banco():
    engine = get_engine()

    df1 = pd.read_csv('../raw/Customers.csv', encoding='latin1')
    df2 = pd.read_csv('../raw/Data_Dictionary.csv', encoding='latin1')
    df3 = pd.read_csv('../raw/Exchange_Rates.csv', encoding='latin1')

    df4 = pd.read_csv('../raw/Products.csv', encoding='latin1')
    
    df4['Unit Cost USD'] = (
        df4['Unit Cost USD']
        .astype(str)
        .str.replace('$', '')
        .str.replace(',', '')
        .str.strip()
        .astype(float)
    )

    df4['Unit Price USD'] = (
        df4['Unit Price USD']
        .astype(str)
        .str.replace('$', '')
        .str.replace(',', '')
        .str.strip()
        .astype(float)
    )

    df5 = pd.read_csv('../raw/Sales.csv', encoding='latin1')
    df6 = pd.read_csv('../raw/Stores.csv', encoding='latin1')


    df1.to_sql('Customers', engine, if_exists='replace', index=False)
    df2.to_sql('Data_Dictionary', engine, if_exists='replace', index=False)
    df3.to_sql('Exchange_Rates', engine, if_exists='replace', index=False)
    df4.to_sql('Products', engine, if_exists='replace', index=False)
    df5.to_sql('Sales', engine, if_exists='replace', index=False)
    df6.to_sql('Stores', engine, if_exists='replace', index=False)

    print("CSVs importados com sucesso!")

    with engine.connect() as conn:
        resultado = conn.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"))
        for linha in resultado:
            print(linha[0])

if __name__ == "__main__":
    importar_csv_para_banco()
