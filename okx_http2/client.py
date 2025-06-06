import json
import time

import httpx

from . import consts as c, utils, exceptions


class Client(object):

    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, flag='1'):

        self.API_KEY = api_key
        self.API_SECRET_KEY = api_secret_key
        self.PASSPHRASE = passphrase
        self.use_server_time = use_server_time
        self.flag = flag
        self.client = httpx.Client(base_url='https://www.okx.com', http2=True, timeout=15)

    def _flush_client(self):
        self.client = httpx.Client(base_url='https://www.okx.com', http2=True, timeout=15)

    def _request(self, method, request_path, params):
        if method == c.GET:
            request_path = request_path + utils.parse_params_to_str(params)
        timestamp = utils.get_timestamp()
        if self.use_server_time:
            timestamp = self._get_timestamp()
        body = json.dumps(params) if method == c.POST else ""
        sign = utils.sign(utils.pre_hash(timestamp, method, request_path, str(body)), self.API_SECRET_KEY)
        header = utils.get_header(self.API_KEY, sign, timestamp, self.PASSPHRASE, self.flag)
        response = None
        if method == c.GET:
            ## 获取异常，防止程序崩溃
            try:
                response = self.client.get(request_path, headers=header, timeout=5)
            except Exception as e:
                print('[_request] failed to exec client.get: ', request_path, response, e)

                # 报错：api time:  0.0009868144989013672
                # [_request] failed to exec client.get:  None
                # 可能会一直卡在这里（服务端不响应，这个时候通过重启python脚本能恢复，重新执行 __init__ 刷一遍 client 能恢复吗？）
                self._flush_client()

        elif method == c.POST:
            try:
                response = self.client.post(request_path, data=body, headers=header, timeout=5)
            except Exception as e:
                print('[_request] failed to exec client.post: ', request_path, response, e)

                # 报错：api time:  0.0009868144989013672
                # [_request] failed to exec client.get:  None
                # 可能会一直卡在这里（服务端不响应，这个时候通过重启python脚本能恢复，重新执行 __init__ 刷一遍 client 能恢复吗？）
                self._flush_client()

        if isinstance(response, httpx.Response):
            if not str(response.status_code).startswith('2'):
                print('[_request] status_code exception: ', request_path, response)
                #time.sleep(1)
                return ''
                #try:
                    # raise exceptions.OkxAPIException(response)
                    #raise ValueError("response exception: ", response)
                #except ValueError("response exception: ", response) as e:
                    #print("[_request] exception: ", e)
                    #time.sleep(2)
            return response.json()
        else:
            return ''

    def _request_without_params(self, method, request_path):
        return self._request(method, request_path, {})

    def _request_with_params(self, method, request_path, params):
        '''
        # 自带重试，最多尝试6次
        for i in range(5):
            try:
                result = self._request(method, request_path, params)
                if result != '' and result['code'] == '0':
                    return result
            except Exception as e:
                print("[_request_with_params] exception: ", e)
            time.sleep(0.2)
        '''
        return self._request(method, request_path, params)

    def _get_timestamp(self):
        request_path = c.API_URL + c.SERVER_TIMESTAMP_URL
        response = self.client.get(request_path)
        if response.status_code == 200:
            return response.json()['ts']
        else:
            return ""
