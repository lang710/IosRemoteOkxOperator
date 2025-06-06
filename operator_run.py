import sys
import time

import okx_http2.Market_api as OkxMarketApi
import okx_http2.Public_api as OkxPublicApi
import okx_http2.Trade_api as OkxTradeApi
import okx_http2.Account_api as OkxAccountApi

from config import *

class OperatorRun(object):
    def __getitem__(self, item):
        return object.__getattribute__(self, item)

    def __init__(self, api_key, secret_key, passphrase, flag, swap_inst_list):
        # client init
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase
        self.flag = flag

        self.swap_inst_list = swap_inst_list

        # api
        self.market_api = OkxMarketApi.MarketAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        self.public_api = OkxPublicApi.PublicAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        self.trade_api = OkxTradeApi.TradeAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        self.account_api = OkxAccountApi.AccountAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)

    def checkApiCorrect(self):
        swap_res = self.market_api.get_tickers(instType='SWAP')
        if swap_res != '' and swap_res['code'] == '0':
            print('correct!')
        else:
            print('incorrect')

if __name__ == '__main__':
    okxConfig = Config()
    api_key, secret_key, passphrase, flag = okxConfig.GetChilangSubAccountConfig()

    calc = OperatorRun(api_key, secret_key, passphrase, flag, [])
    calc.checkApiCorrect()
