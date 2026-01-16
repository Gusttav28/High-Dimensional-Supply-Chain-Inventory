import pandas as pd
import numpy as np
import mysql.connector
from sqlalchemy import create_engine

# %%
def extracting_data(file_path):
    return pd.read_csv(file_path)
    

# %%
def transforming_data(df):
    df.dropna()
    df[df.duplicated()] 
    pd.to_datetime(df['Date'])
    df[df['Unit_Price'] > 0]
    df[df['Unit_Cost'] > 0]
    return df



def loading_data(df, db_name):
    connection_string = f'mysql+mysqlconnector://root:30696222@localhost/{db_name}'
    engine = create_engine(connection_string)
    df.to_sql(db_name, con=engine, if_exists='append', index=False)

if __name__ == "__main__":
    raw_df = extracting_data("supply_chain_dataset1.csv")
    clean_df = transforming_data(raw_df)
    print(clean_df)
    load_data = loading_data(clean_df, "aws-cors")
    print("Data successfully merge into the mysql")
    