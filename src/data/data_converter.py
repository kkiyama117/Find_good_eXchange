from pathlib import Path

import utils
import pandas

from data.get_data import get_data


def convert_candles(chart_list: list):
    DATA_DIR = Path().resolve().parents[1] / 'data' / "candle.csv"
    filename = str(DATA_DIR)
    candles_dict = [row['mid'] for row in chart_list.response["candles"]]
    candle = pandas.DataFrame.from_dict(candles_dict)
    candle['time'] = [row['time'] for row in chart_list.response['candles']]
    candle.to_csv(filename)
    return candle


if __name__ == '__main__':
    convert_candles(get_data())
