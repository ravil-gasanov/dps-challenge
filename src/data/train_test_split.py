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

    train, test = train_test_split(df)

    train.to_csv(train_path, index = False)
    test.to_csv(test_path, index = False)


if __name__ == "__main__":
    raw_path = "./data/raw/data.csv"
    train_path = "./data/train_test/train.csv"
    test_path = "./data/train_test/test.csv"

    parser = argparse.ArgumentParser(description='Description of your program.')
    parser.add_argument('-rn', '--raw_path', help='Path to the raw data file.', required=False)
    args = parser.parse_args()
    
    if args.raw_path:
        raw_path = args.raw_path
    
    split(raw_path, train_path, test_path)


    




