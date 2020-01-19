import numpy as np
import pandas as pd

from data import *

__all__ = ['missing_data', 'duplicated_data', 'identify_variables']


def missing_data(df):
    return df[df.columns[df.isnull().any()].tolist()].isnull().sum()


def duplicated_data(df):
    return df.duplicated().sum()


def identify_variables(df):
    # print(df.describe(include=[np.number]))
    # print(df.describe(include=['O']))
    numerical = []
    categorical = []
    for key, item in df.dtypes:
        print(key, item)
        # if item is np.object:
        #     categorical.append()


def main():
    data_df = get_data().drop(['url', 'image_url', 'lat', 'long', 'region', 'region_url', 'vin'], axis=1)
    print('\nCheck for missing data:\n', missing_data(data_df))
    print('\nCheck for duplicated data:\n', duplicated_data(data_df))
    print('\nIdentify variables:\n', identify_variables(data_df))


if __name__ == "__main__":
    main()
