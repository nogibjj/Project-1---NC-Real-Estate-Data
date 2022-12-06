# Filters data based on criteria written in a string of Python syntax

# Import the necessary packages
import dask.dataframe as dd
import dask
from dask.distributed import Client
import pandas as pd

# Read in the data
def readData(file = 'datasets/predicted-data.csv'):
    datadf = dd.read_csv(file, parse_dates=['sold_date'], infer_datetime_format=True)
    return datadf

# Filters data based on criteria in a string formatted to python boolean evaluation
def filterdf(data, criteria):
    if type(data) == type(pd.DataFrame()):
        return data[data.eval(criteria)]
    elif type(data) == type(dd.DataFrame()):
        return dask.compute(data[data.eval(criteria)])[0]
    else:
        return "Type Error"

# Test a filter 
if __name__ == '__main__':
    # Set up a Dask Client
    client = Client(n_workers=4)
    # Analyze file
    print(dask.compute(filterdf(readData(), '(bath ==2) & (bed == 3)'))[0])

