import pytest
import pandas as pd

from ..preprocessing import *

def test_make_month():
    df = pd.DataFrame({'month': ['201001', '201002', '201003'], 'correct': ['01', '02', '03']})
    
    df['month'] = make_month(df['month'])

    assert (df['month'] == df['correct']).all()

def test_drop_yearly_aggregate_rows():
    df = pd.DataFrame({
        'month': ['201001', '201002', 'Summe'], \
        'year': [2010, 2010, 2010],\
        'value': [1, 1, 2]
        })
    
    correct = pd.DataFrame({'month': ['201001', '201002']})

    df = drop_yearly_aggregate_rows(df)

    assert (df['month'] == correct['month']).all()

def test_make_date():
    df = pd.DataFrame({
        'month': ['01', '02'], \
        'year': [2010, 2010],
        'correct': ['2010-01', '2010-02']
        })
    
    df['date'] = make_date(df['year'], df['month'])

    assert (df['date'] == df['correct']).all()