import pandas as pd
from src.db_connection import get_engine

def load_csv_to_mysql(csv_path):
    df=pd.read_csv(csv_path)
    engine=get_engine()
    df.to_sql('transactions',con=engine, if_exists='replace',index=False)
    print("Dataset successfully loaded into MySQL!")

if __name__ == "__main__":
    load_csv_to_mysql("./data/raw/creditcard.csv")