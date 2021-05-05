"# IPL-Run-Prediction" 
**IPL Score Predition**
we have all_matches.csv file 
    Predicting how much run scored by indivitual team in 6 overs 
    1. Data Cleaning(data_cleaning.ipynb)
        i) create batsmen.csv(our dataset) file
    
    2. Data Training(data_training.ipynb)
        i) normalize String columns(venue,batting_team,bowling_team,striker)
        ii)predict based on bowling_team and striker
        iii) fit the finalize dataset into RandomForestRegressor Algo
        iv) save joblib file of string columns
<<<<<<< HEAD
    
    3. Prediting runs using inputFile.csv as input in Predictor.py file
        in this we have PredictRuns() which return predic runs
    
    4. Run main.py file to get the output file
=======
>>>>>>> 5068eafd8f616176b153434afa8d391adc247cd9
