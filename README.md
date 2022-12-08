# Project-1---NC-Real-Estate-Data

Analysis of real estate dataset.

This project is based upon analyzing and querying real estate data from USA Real Estate Dataset taken from Kaggle (https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset).

Web Application (new feature):

This project is set-up as a Streamlit web application.  Please visit the web application here (https://nick-carroll1-project-1---nc-real-estate-d-streamlit-app-gfwnrw.streamlit.app/).  Screenshot below.

![image](https://user-images.githubusercontent.com/112578073/206327042-24fe8cdb-a229-40e7-8425-a54146bf4900.png)

This project allows a user to input five features that they are looking for in a home: zip code, number of bedrooms, number of bathrooms, home square footage, and lot size.  From these features, the web application estimates the expected price of the home using multiple linear regression estimated for each zip code separately.  The app also plots the prices of the zip code with the regression line and confidence interval.  Finally, the application shows a table of up to ten homes in the dataset that match the search criteria.

On the back end, the Kaggle dataset is stored in a MySQL database on AWS to query the data.  A linear regression model is run everytime the query is updated as the model is not saved on disk.  The createdb file provides functionality for interacting with the database: uploading new data, querying the data, etc.

Command Line tool (original features): 

This project has set-up a command line tool allowing someone to download an updated version of this dataset to their datasets folder, analyze the data to provide price predictions for each listing, and query the analyzed data as desired.

Data is analyzed by separating all of the listings by zip code and running a multiple linear regression along all of the predictor variables: bed, bath, acre lot, and house size.  This analysis assumes that listings from different zip codes are unrelated, and that pricing within a zip code is only based on these 4 predictor variables.  This analysis ignores multicollinearity between the predictor variables.  

Data is analyzed as a Dask Dataframe for parallelized computing, but for the purposes of this project, the dask client has only been set-up with 4 local workers.

![Project I Flowchart](https://user-images.githubusercontent.com/112578073/190929188-85fae215-7e64-41dd-bee0-a12c64517565.png)
