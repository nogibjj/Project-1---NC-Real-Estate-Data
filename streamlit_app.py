import streamlit as st
import createdb as db
import filterData as filter

st.title("Nick Carroll's Real Estate Analysis App")

zip = st.text_input("Please input the zip code that you are searching for a home in:", "10001")
beds = int(st.text_input("Please input the number of bed that you are looking for in your home:", "2"))
baths = float(st.text_input("Please input the number of bathrooms that you are looking for in your home:", "2"))
sqft = float(st.text_input("Please input the square footage that you are looking for in your home:", "1000"))

df = db.getData()
st.table(df.tail())
criteria = f"(bed == {beds})"
st.write(criteria)
st.table(data[data.eval(criteria)].head())
# filteredDF = filter.filterdf(df, criteria)
st.subheader("The top homes that match your search criteria are:")
# st.table(filteredDF.head())