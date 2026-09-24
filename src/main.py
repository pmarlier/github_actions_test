import pandas as pd
import numpy as np

# throw an error
# sncf_df = pd.read_csv("regularite-mensuelle-tgv-aqst.csv")

def load_data():
    data_df = pd.read_table("./data/regularite-mensuelle-tgv-aqs.csv",
                            delimiter=';')
    return data_df

if "__name__" == "__main__":
    data_df = load_data