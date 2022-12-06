import streamlit as st
import createdb as db
import pandas as pd
from sklearn import linear_model
import numpy as np

st.title("Nick Carroll's Real Estate Analysis App")

zip = st.text_input("Please input the zip code that you are searching for a home in:", "10001")
beds = int(st.text_input("Please input the number of bed that you are looking for in your home:", "2"))
baths = float(st.text_input("Please input the number of bathrooms that you are looking for in your home:", "2"))
sqft = float(st.text_input("Please input the square footage that you are looking for in your home:", "1000"))
acre = float(st.text_input("Please input the lot size that you are looking for in your home:", "0.5"))

zipQuery = f"SELECT DISTINCT * FROM real_estate WHERE zip_code = {zip}"
regressiondf = db.queryData(zipQuery)
regr = linear_model.LinearRegression()
droppedData = regressiondf[['bed', 'bath', 'acre_lot', 'house_size','price']].dropna()
if droppedData.shape[0] > 0:
    regr.fit(droppedData[['bed', 'bath', 'acre_lot', 'house_size']], droppedData['price'])
    predictor = pd.DataFrame({'bed': beds, 'bath': baths, 'acre_lot': acre, 'house_size': sqft})
    st.write(f'The expected price for your home search is: {np.round(regr.predict(predictor))}')
else:
    st.write('Insufficient data found for that zip code to make a price prediction.')

st.subheader("The top homes that match your search criteria are:")
query = f"SELECT DISTINCT * FROM real_estate WHERE zip_code = {zip} AND bed = {beds} AND bath = {baths} AND (house_size BETWEEN {.8 * sqft} AND {1.2 * sqft})LIMIT 10"
df = db.queryData(query)
st.table(df)