import sys
import time

import okx_http2.Market_api as OkxMarketApi
import okx_http2.Public_api as OkxPublicApi
import okx_http2.Trade_api as OkxTradeApi
import okx_http2.Account_api as OkxAccountApi
import okx_http2.Funding_api as OkxFundingApi

from config import *
from parse_okx import *

class OperatorRun(object):
    def __getitem__(self, item):
        return object.__getattribute__(self, item)

    def __init__(self, api_key, secret_key, passphrase, flag):
        # client init
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase
        self.flag = flag

        # api
        self.market_api = OkxMarketApi.MarketAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        self.public_api = OkxPublicApi.PublicAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        self.trade_api = OkxTradeApi.TradeAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        self.account_api = OkxAccountApi.AccountAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        self.funding_api = OkxFundingApi.FundingAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)

    def checkApiCorrect(self):
        swap_res = self.market_api.get_tickers(instType='SWAP')
        if swap_res != '' and swap_res['code'] == '0':
            print('correct!')
        else:
            print('incorrect')

    def makeOrder(self, side, posSide, ordType, sz, px):
        order_data = {
            'instId': 'BTC-USDT-SWAP',
            'tdMode': 'cross',
            'side': side,
            'ordType': ordType,
            'sz': sz,
            'posSide': posSide,
            'px': px,
            'ccy': 'USDT',
        }

        order_resp = self.trade_api.place_multiple_orders(orders_data=[order_data])
        if order_resp == '' or order_resp['code'] != '0':
            print_format = 'failed to trade order for {}, result: {}'.format( order_data,
                         order_resp)
            print(print_format)
        else:
            print_format = 'succeed to trade order for {}, result: {}'.format(order_data,
                                                                             order_resp)
            print(print_format)

    def cancelOrder(self, ord_id):
        order_data = {
            'instId': 'BTC-USDT-SWAP',
            'ordId': ord_id
        }

        cancel_resp = self.trade_api.cancel_multiple_orders(orders_data=[order_data])
        if cancel_resp == '' or cancel_resp['code'] != '0':
            print_format = 'failed to cancel order for {}, result: {}'.format( order_data,
                         cancel_resp)
            print(print_format)
        else:
            print_format = 'succeed to cancel order for {}, result: {}'.format(order_data,
                                                                             cancel_resp)
            print(print_format)

    def listAll(self):
        print(self.trade_api.get_order_list(instId='BTC-USDT-SWAP'))
        print(self.trade_api.get_orders_history(instId='BTC-USDT-SWAP', instType='SWAP'))

        print(self.account_api.get_account(ccy='USDT'))
        print(self.account_api.get_positions(instId='BTC-USDT-SWAP'))
        print(self.account_api.set_leverage(instId='BTC-USDT-SWAP', mgnMode='cross', lever='100'))
        print(self.account_api.get_leverage(instId='BTC-USDT-SWAP', mgnMode='cross'))

        print(self.funding_api.get_balances(ccy='USDT'))

if __name__ == '__main__':
    args = ParserOkx()
    account, action = args.account, args.action

    okxConfig = Config()
    api_key, secret_key, passphrase, flag = okxConfig.GetMockConfig()
    if account == 'mock':
        api_key, secret_key, passphrase, flag = okxConfig.GetMockConfig()
    elif account == 'chilang':
        api_key, secret_key, passphrase, flag = okxConfig.GetChilangSubAccountConfig()
    elif account == 'juyou':
        api_key, secret_key, passphrase, flag = okxConfig.GetJuyouSubAccountConfig()
    opr = OperatorRun(api_key, secret_key, passphrase, flag)

    if action == 'order':
        side, posSide, ordType, sz, px = args.side, args.posSide, args.ordType, args.sz, args.px
        # 下单
        opr.makeOrder(side, posSide, ordType, sz, px)
    elif action == 'cancel':
        ord_id = args.ordId
        # 取消订单
        opr.cancelOrder(ord_id)
    elif action == 'list':
        # 列出所有基本信息
        opr.listAll()
    else:
        print("cannot understand action: {}".format(action))
