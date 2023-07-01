import argparse
import random

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

SEED = 42
random.seed(SEED)
np.random.seed(SEED)

def split(raw_path, train_path, test_path):
    df = pd.read_csv(raw_path)
    
    train = df[df.JAHR <= 2020]
    test = df[df.JAHR > 2020]

    train.to_csv(train_path, index = False)
    test.to_csv(test_path, index = False)


if __name__ == "__main__":
    raw_path = "./data/raw/monatszahlen2209_verkehrsunfaelle.csv"
    train_path = "./data/train_test/train.csv"
    test_path = "./data/train_test/test.csv"
    
    split(raw_path, train_path, test_path)


    




