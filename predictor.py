import pandas as pd
import joblib
# from sklearn.preprocessing import LabelEncoder
def predictRuns(testInput):
    prediction = 0

    with open('teamEncoder.joblib', 'rb') as f:
        teamEncoder = joblib.load(f)

    with open('strikerEncoder.joblib', 'rb') as f:
        batsmanEncoder = joblib.load(f)

    with open('RandomForestRegressor.joblib', 'rb') as f:
        regressor = joblib.load(f)

    df = pd.read_csv(testInput)

    bowling_team = []
    bowling_team.append(df["bowling_team"][0].strip())
    bowling_team = teamEncoder.transform(bowling_team)

    batsmen = str(df['batsmen'][0]).split(',')
    batsmen = [s.strip() for s in batsmen]
    batsmen = batsmanEncoder.transform(batsmen)

    if len(batsmen)==2:
        score1 = regressor.predict([[bowling_team,batsmen[0]]])
        score2 = regressor.predict([[bowling_team,batsmen[1]]])
        if score1>score2:
            prediction = score1*2+score2
        else:
            prediction = score1+score2*2

    elif len(batsmen)>3:
        for men in batsmen:
            score = regressor.predict([[bowling_team,men]])
            prediction += score
        prediction/= 2
    else:
        for men in batsmen:
            score = regressor.predict([[bowling_team,men]])
            prediction += score
    return prediction