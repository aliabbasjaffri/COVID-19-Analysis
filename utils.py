import pandas as pd

def load_file(csv_path):
    df = pd.read_csv(csv_path, infer_datetime_format=True)
    df.drop(["Lat", "Long"],axis=1, inplace=True)
    df.rename({"Country/Region": "Country", "Province/State": "Province"}, 
              axis='columns', 
              inplace =True)
    
    return df