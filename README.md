example:
$ python3 operator_run.py --account mock --action order --side buy --posSide long --ordType limit --sz 0.
05 --px 101300
succeed to trade order for {'instId': 'BTC-USDT-SWAP', 'tdMode': 'cross', 'side': 'buy', 'ordType': 'limit', 'sz': '0.05', 'posSide': 'long', 'px': '101300', 'ccy': 'USDT'}, result: {'code': '0', 'data': [{'clOrdId': '', 'ordId': '2573241586047012864', 'sCode': '0', 'sMsg': 'Order placed', 'tag': '', 'ts': '1749190975328'}], 'inTime': '1749190975327526', 'msg': '', 'outTime': '1749190975328963'}

$ python3 operator_run.py --account mock --action cancel --ordId 2573241586047012864
succeed to cancel order for {'instId': 'BTC-USDT-SWAP', 'ordId': '2573241586047012864'}, result: {'code': '0', 'data': [{'clOrdId': '', 'ordId': '2573241586047012864', 'sCode': '0', 'sMsg': '', 'ts': '1749191081233'}], 'inTime': '1749191081232790', 'msg': '', 'outTime': '1749191081233881'}
