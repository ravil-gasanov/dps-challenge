import pandas as pd
import matplotlib.pyplot as plt

from preprocessing import make_clean, make_month, make_date

color_map = {'Verkehrsunfälle': 'red', 'Alkoholunfälle': 'green', 'Fluchtunfälle': 'blue'}


def plot_historical_values_by_category(df, category, period):
    '''
    df: pd.DataFrame
    category: 'Verkehrsunfälle', 'Alkoholunfälle' or 'Fluchtunfälle'
    period: 'year' or 'date'
    '''
    f = plt.figure()
    f.set_figwidth(16)
    f.set_figheight(9)

    df = df.copy()
    df = make_clean(df)
    
    df['month'] = make_month(df['month'])
    df['date'] = make_date(df['year'], df['month'])

    df = df[df['category'] == category]

    grouped = df.groupby(period).sum()

    plt.plot(grouped.index, grouped['value'], \
        color = color_map[category], label = category, marker = 'o', markersize = 8)
    
    if period == "year":
        plt.xticks(ticks = list(range(2000, 2021)))
    
    plt.legend()
    plt.savefig(f"../reports/number_of_{category}_accidents_by_{period}.png")

    plt.show()

    

if __name__ == "__main__":
    train = pd.read_csv("../data/train_test/train.csv")

    for period in ['date', 'year']:
        for category in train['category'].unique():
            plot_historical_values_by_category(train, category, period)