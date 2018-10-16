from pathlib import Path

import pandas

from data.get_data import get_candles_data

# data dir
DATA_DIR = Path().resolve().parents[1] / 'data' / "candle.csv"


def convert_candles_dict_to_panda(candles):
    candles_dicts = [row['mid'] for row in candles.response["candles"]]
    candles = pandas.DataFrame(candles_dicts)
    candles['time'] = [row['time'] for row in candles.response['candles']]
    return candles


def save_candles_data(candles, data_dir=DATA_DIR):
    # save
    filename = str(data_dir)
    candles.to_csv(filename)


if __name__ == '__main__':
    print(convert_candles_dict_to_panda(get_candles_data()))
