# Import the necessary packages
import dask.dataframe as dd
import dask
from dask.distributed import Client
import numpy as np
from sklearn import linear_model

# Read in the data
def readData(file):
    datadf = dd.read_csv(file, parse_dates=['sold_date'], infer_datetime_format=True)
    return datadf

# Use a linear regression function to predict prices (expected input groupby)
def groupbyRegr(data):
    groupRegr = linear_model.LinearRegression()
    droppedData = data[['bed', 'bath', 'acre_lot', 'house_size','price']].dropna()
    if droppedData.shape[0] > 0:
        groupRegr.fit(droppedData[['bed', 'bath', 'acre_lot', 'house_size']], droppedData['price'])
        droppedData['Predicted Price'] = np.round(groupRegr.predict(droppedData[['bed', 'bath', 'acre_lot', 'house_size']]))
        data['Predicted Price'] = droppedData['Predicted Price']
    return data

# Use a groupby function for a linear regression for each zip code
def zipGroupArray(data):
    data['Predicted Price'] = 0.
    return data.groupby('zip_code').apply(groupbyRegr, meta = data)

# Plot data predictions against actual data (unused needs to be modified for plotting since regression functions have changed)
#def plotPrediction(data, zipCode, predictions):
    #x, yActual, yPredicted = dask.compute(data[data['zip_code']==zipCode].loc[:,'acre_lot'], data[data['zip_code']==zipCode].loc[:,'price'], predictions)
    #plt.scatter(x, yActual)
    #plt.scatter(x, yPredicted)
    #plt.show()
    #pass

# Run the regression
def runRegressor(data):
    return dask.compute(zipGroupArray(data))[0]

# Analyze data
def dfanalysis(file, workers=4, exportFile = 'datasets/predicted-data.csv'):
    # Set up a Dask Client
    client = Client(n_workers=workers)

    # Predict values
    datadf = readData(file)
    predicteddf = runRegressor(datadf)

    # Export dataframe to csv
    exportData(predicteddf, exportFile)
    
    # Close the client
    client.close()


# Exports the data to csv
def exportData(data, file = 'datasets/predicted-data.csv'):
    data.to_csv(file)
    pass

# Filters data based on criteria in a dictionary
def filterData(data, criteria):
    return data[data.eval(criteria)]

# Test the entire program 
if __name__ == '__main__':
    # Set file where data can be found
    file = 'datasets/realtor-data.csv'
    
    # Analyze file
    dfanalysis(file)