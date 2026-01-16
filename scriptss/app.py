import kagglehub
import pandas as pd

# 
def read_file(file):    
    read_file = file
    file_readed = pd.read_csv(read_file, keep_default_na=False, na_values = ['NA', '0'])
    df = pd.DataFrame(file_readed)
    # date = file_readed['Date']
    # order_quantity = file_readed["Order_Quantity"]
    # for i in order_quantity:
    #     if i == 0:
    #         print("There's a cero")
    # print(date, '\n',  order_quantity)
    print(df)
    
read_file("supply_chain_dataset1.csv")