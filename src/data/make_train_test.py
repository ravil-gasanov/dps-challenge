import random

import numpy as np
import pandas as pd

SEED = 42
random.seed(SEED)
np.random.seed(SEED)

def make_train_test(raw_path, train_path, test_path):
    df = pd.read_csv(raw_path)

    # the challenge-related features are the first 5 columns
    df = df[['MONATSZAHL', 'AUSPRÄGUNG', 'JAHR', 'MONAT', 'WERT']]
    # map column names to English translations for convenience
    df = df.rename(columns={
        'MONATSZAHL':'category',
        'AUSPRÄGUNG': 'type',
        'JAHR': 'year',
        'MONAT': 'month',
        'WERT': 'value'
        })
    
    # train-test split
    train = df[df.year <= 2020]
    test = df[df.year > 2020]

    train.to_csv(train_path, index = False)
    test.to_csv(test_path, index = False)


if __name__ == "__main__":
    raw_path = "./data/raw/monatszahlen2209_verkehrsunfaelle.csv"
    train_path = "./data/train_test/train.csv"
    test_path = "./data/train_test/test.csv"
    
    make_train_test(raw_path, train_path, test_path)


    




