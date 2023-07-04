import pandas as pd

def make_month(month):
    '''
    month: pd.Series
    returns: pd.Series
    '''
    return month.str.extract(r'\d\d\d\d(\d\d)')

def make_date(year, month):
    '''
    year: pd.Series
    month: pd.Series
    returns: pd.Series
    '''
    return pd.to_datetime(year.astype(str) + '-' + month.astype(str)).dt.to_period('M').dt.to_timestamp('M')