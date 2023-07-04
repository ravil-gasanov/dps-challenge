import joblib
import pandas as pd

from preprocessing import make_clean, make_month, make_date
from models import choose_model, tune_model

def train_model(train_path):
    train = pd.read_csv(train_path)

    train = make_clean(train)

    # since we are asked to predict for this sub-population only
    train = train[(train['category'] == 'Alkoholunfälle') & (train['type'] == 'insgesamt')]

    train['month'] = make_month(train['month'])
    train['date'] = make_date(train['year'], train['month'])
    
    train = train.sort_values('date').reset_index()

    X = train[['date', 'year', 'month']]
    y = train['value']

    model, model_name, model_score = choose_model(X, y)
    
    joblib.dump(model, '../models/model.pkl')


if __name__ == "__main__":
    train_path = "../data/train_test/train.csv"

    train_model(train_path)
