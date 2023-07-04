import numpy as np
import pandas as pd 
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
from sklearn.metrics import r2_score, mean_absolute_error

from sklearn.linear_model import LinearRegression, PoissonRegressor
from sklearn.ensemble import RandomForestRegressor

from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.dynamic_factor_mq import DynamicFactorMQ
# from statsmodels.tsa.holtwinters import ExponentialSmoothing

from prophet import Prophet

# from croston import croston
# y_pred = croston.fit_croston(train_y, len(test_y),'original')['croston_forecast']

from preprocessing import make_date
from models.wrappers import ProphetWrapper, SMWrapper

models = [
    ('rfr', RandomForestRegressor()),
    ('lr', LinearRegression()),
    ('pr', PoissonRegressor()),

    ('prophet', ProphetWrapper()),

    ('arima', SMWrapper(ARIMA)),
    ('dfmq', SMWrapper(DynamicFactorMQ))
]

def make_pipe(model):
    if model[0] == 'prophet':
        ct = None
    else:
        ct = ColumnTransformer([
            ('passthrough', 'passthrough', ['year']),
            ('ohe', OneHotEncoder(sparse=False), ['month'])
        ], remainder='drop')

    steps = [('ct', ct), model]

    return Pipeline(steps = steps)

def choose_model(X, y):
    model_score = dict()

    for model in models:
        tscv = TimeSeriesSplit(n_splits=20)

        scores = []

        for train_idx, test_idx in tscv.split(X):
            train_X = X.loc[train_idx]
            train_y = y.loc[train_idx]

            test_X = X.loc[test_idx]
            test_y = y.loc[test_idx]

            pipe = make_pipe(model)
            pipe.fit(train_X, train_y)
            pred_y = pipe.predict(test_X)

            mae = mean_absolute_error(test_y, pred_y)
            scores.append(mae)

            # print(train_X['year'].unique())
            # print(test_X['year'].unique())
            # print(f"MAE: {mae:.2f}")
        
        print(f"{model[0]} average MAE: {np.mean(scores):.2f}")
        model_score[model[0]] = np.mean(scores)
    
    print(model_score)

    best_model_name = min(model_score, key = model_score.get)
    best_model_score = model_score[best_model_name]

    best_model = [model for model in models if best_model_name == model[0]]
    model = make_pipe((best_model_name, best_model))[1]
    

    print(f"Best model: {best_model_name} with MAE = {best_model_score}")

    return model, best_model_name, best_model_score


def tune_model(X, y, best_model_name):
    pass