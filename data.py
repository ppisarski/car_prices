import os
import pandas as pd
from zipfile import ZipFile

__all__ = ['get_data']

FILE_PATH = './data'
FILE_NAME = 'vehicles.csv'


def get_data():
    if not os.path.isdir(FILE_PATH):
        os.mkdir(FILE_PATH)
        raise FileNotFoundError('You need to download the dataset.')

    if os.path.isfile(os.path.join(FILE_PATH, 'craigslist-carstrucks-data.zip') and len(os.listdir(FILE_PATH)) == 1):
        with ZipFile(os.path.join(FILE_PATH, 'craigslist-carstrucks-data.zip'), 'r') as zipObj:
            zipObj.extractall(FILE_PATH)

    data_df = pd.read_csv(os.path.join(FILE_PATH, FILE_NAME))
    return data_df


def main():
    print(get_data().head())


if __name__ == "__main__":
    main()
