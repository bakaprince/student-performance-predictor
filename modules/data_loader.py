import pandas as pd

def load_dataset(path='data/dataset.csv'):
    x= pd.read_csv(path)
    print("Dataset loaded successfully!")
    print(x.head())
    return x