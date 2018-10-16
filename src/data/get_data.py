from oandapyV20 import API
from decouple import config
import oandapyV20.endpoints.instruments as inst

def get_candles_data() -> inst.InstrumentsCandles:
    """
    get data of chart as list of dict

    :return: dict
    """
    # get API token
    oanda_api_token = config("OANDA_API")
    # access to API
    oanda_api = API(access_token=oanda_api_token,environment="practice")
    params = {
        "alignmentTimezone": "Japan",
        "count": 200,
        "granularity": "M15"
    }
    data = inst.InstrumentsCandles(instrument="EUR_USD", params=params)
    oanda_api.request(data)
    return data

if __name__ == '__main__':
    print(get_data())