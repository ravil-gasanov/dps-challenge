import pandas as pd

def extract_month(month):
    '''
    month: pd.Series
    returns: pd.Series
    '''
    return month.str.extract(r'\d\d\d\d(\d\d)')