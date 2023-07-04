import pandas as pd
import statsmodels.api as sm
from sklearn.base import BaseEstimator, RegressorMixin

from prophet import Prophet


class ProphetWrapper(BaseEstimator, RegressorMixin):
    additional_regs = ['is_jan', 'is_feb', 'is_mar', 'is_apr', 'is_may', 'is_jun',\
             'is_jul', 'is_aug', 'is_sep', 'is_oct', 'is_nov', 'is_dec']
    
    def get_month_dummies(self, month):
        dummies = pd.get_dummies(month)
        dummies.columns = [r for r in self.additional_regs]

        return dummies

    def fit(self, X, y):
        df = pd.DataFrame()
        df['ds'] = X['date']
        df['y'] = y
        
        self.model = Prophet(yearly_seasonality=False)
        
        dummies = self.get_month_dummies(X['month'])
        df = pd.concat([df, dummies], axis = 1)
        
        for r in self.additional_regs:
            self.model.add_regressor(r)
        
        self.model_fit = self.model.fit(df)

        return self
    
    def predict(self, X):
        future = pd.DataFrame()
        future['ds'] = X['date']
        dummies = self.get_month_dummies(X['month'])
        future = pd.concat([future, dummies], axis = 1)

        return self.model_fit.predict(future)['yhat']


class SMWrapper(BaseEstimator, RegressorMixin):
    '''
    Sklearn wrapper for sm models
    '''
    def __init__(self, model_class):
        self.model_class = model_class
    def fit(self, X, y):
        self.model = self.model_class(y)
        self.model_fit = self.model.fit()

        return self
    
    def predict(self, X):
        return self.model_fit.get_forecast(steps=len(X)).predicted_mean