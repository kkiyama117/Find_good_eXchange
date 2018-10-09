from get_data import get_data
import panda as pd

def data_to_pd():
    # 為替レートのdictをDataFrameへ変換
    rate = pd.DataFrame.from_dict(
        {r.response['candles'][i]['time']: r.response['candles'][i]['mid']
         for i in range(0, len(r.response['candles']))
         for j in r.response['candles'][i]['mid'].keys()},
        orient='index',
        )
if __name__ == '__main__':
    print(get_data())
