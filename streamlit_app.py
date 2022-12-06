import streamlit as st
import createdb as db
import filterData as filter

st.title("Nick Carroll's Real Estate Analysis App")

zip = st.text_input("Please input the zip code that you are searching for a home in:", "10001")
beds = int(st.text_input("Please input the number of bed that you are looking for in your home:", "2"))
baths = float(st.text_input("Please input the number of bathrooms that you are looking for in your home:", "2"))
sqft = float(st.text_input("Please input the square footage that you are looking for in your home:", "1000"))

query = f"SELECT * FROM real_estate WHERE bed = {beds} LIMIT 10"
df = db.queryData(query)
criteria = f"(bed == {beds})"
st.table(df)
# st.table(df[df.eval(criteria)].head())
# filteredDF = filter.filterdf(df, criteria)
st.subheader("The top homes that match your search criteria are:")
# st.table(filteredDF.head())