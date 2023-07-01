import pytest
import pandas as pd

from ..preprocessing import *

def test_extract_month():
    df = pd.DataFrame({'month': ['201001', '201002', '201003'], 'correct': ['01', '02', '03']})
    
    df['month'] = extract_month(df['month'])

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