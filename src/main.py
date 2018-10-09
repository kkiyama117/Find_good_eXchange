from oandapyV20 import API
from decouple import config
import oandapyV20.endpoints.instruments as inst

if __name__ == '__main__':
    oanda_api_token = config("OANDA_API")
    oanda = API(access_token=oanda_api_token)
