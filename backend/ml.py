import shap
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing


def predict(algo):
    apt = pd.read_csv("https://raw.githubusercontent.com/noghte/datasets/main/apartments.csv", nrows=500)
    apt.dropna(subset = ['resale_price'], axis = 0, inplace = True)

    normalizer = preprocessing.Normalizer()
    df = pd.DataFrame(normalizer.fit_transform(apt), columns=apt.columns, index=apt.index)

    X = df.drop('resale_price',axis =1)
    y = df['resale_price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1144)

    pred = -1
    if algo == "lr":
        model_reg = LinearRegression()  
        model_reg.fit(X_train, y_train)
        pred_reg = model_reg.predict(X_test)
        pred = pred_reg[0]

    elif algo == "rf":
        rf_model = RandomForestRegressor(n_estimators=10, max_features=2)
        rf_model.fit(X_train, y_train)
        rf_pred = rf_model.predict(X_test)
        pred = rf_pred[0]

    return pred # return the first prediction