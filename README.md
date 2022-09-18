# Project-1---NC-Real-Estate-Data
Analysis of real estate dataset.

This project is based upon analyzing and querying real estate data from USA Real Estate Dataset taken from Kaggle (https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset).  This project has set-up a command line tool allowing someone to download an updated version of this dataset to their datasets folder, analyze the data to provide price predictions for each listing, and query the analyzed data as desired.

Data is analyzed by separating all of the listings by zip code and running a multiple linear regression along all of the predictor variables: bed, bath, acre lot, and house size.  This analysis assumes that listings from different zip codes are unrelated, and that pricing within a zip code is only based on these 4 predictor variables.  This analysis ignores multicollinearity between the predictor variables.  Based on the set-up of the original dataset, zip codes are treated as floats; for example, zip code 00601 is in the data as 601.0.

Data is analyzed as a Dask Dataframe for parallelized computing, but for the purposes of this project, the dask client has only been set-up with 4 local workers.

![Project I Flowchart](https://user-images.githubusercontent.com/112578073/190929188-85fae215-7e64-41dd-bee0-a12c64517565.png)
