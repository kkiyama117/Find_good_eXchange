from oandapyV20 import API
from decouple import config
import oandapyV20.endpoints.instruments as inst

if __name__ == '__main__':
    oanda_api_token = config("OANDA_API")
    oanda_api = API(access_token=oanda_api_token,environment="practice")
    params = {
        "alignmentTimezone": "Japan",
        "count": 200,
        "granularity": "M15"
    }
    data = inst.InstrumentsCandles(instrument="EUR_USD", params=params)
    oanda_api.request(data)
    print(data.responce)
