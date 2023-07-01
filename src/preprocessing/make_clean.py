import pandas as pd

def make_clean(df):
    '''
    df: pd.DataFrame
    returns: pd.DataFrame
    '''
    df = df.copy()

    df = drop_yearly_aggregate_rows(df)

    return df

def drop_yearly_aggregate_rows(df):
    '''
    df: pd.DataFrame
    returns: pd.DataFrame
    '''
    df = df.copy()

    # check that month == 'Summe' rows contain yearly aggregated values
    assert (df[df['month'] == 'Summe'].groupby('year').sum()['value'] \
        == df[df['month'] != 'Summe'].groupby('year').sum()['value']).all()
    
    # drop month == 'Summe' rows
    df = df[df['month'] != 'Summe']

    return df