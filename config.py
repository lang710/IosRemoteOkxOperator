
####### config

class Config(object):
    def __getitem__(self, item):
        return object.__getattribute__(self, item)

    def __init__(self):
        self.account_name = "mock-api"
        self.api_key = "248641f1-b80a-499b-a106-751a2335e388"
        self.secret_key = "E05AE6D3C49D276B98CC0114D8494473"
        self.passphrase = "Ali88SteveJobs!"
        self.flag = '1'  # 模拟盘 demo trading

        return

    def GetMockConfig(self):
        self.account_name = "mock-api"
        self.api_key = "248641f1-b80a-499b-a106-751a2335e388"
        self.secret_key = "E05AE6D3C49D276B98CC0114D8494473"
        self.passphrase = "Ali88SteveJobs!"
        self.flag = '1'  # 模拟盘 demo trading

        return self.api_key, self.secret_key, self.passphrase, self.flag

    def GetSubAccountConfig(self):
        self.account_name = "juyou01"
        self.api_key = "5f540e63-114d-4934-8044-7341d9c130bf"
        self.secret_key = "D97C98190D4C639D149679EF040546B2"
        self.passphrase = "Jiaoyi888@"
        self.flag = '0'

        return self.api_key, self.secret_key, self.passphrase, self.flag

    def GetChilangSubAccountConfig(self):
        self.account_name = "chilangsubaccount1"
        self.api_key = "b571550c-52a3-49a0-94d7-d04726fea122"
        self.secret_key = "6BBFC2153CF429CA95775250A41B31EA"
        self.passphrase = "Ali88SteveJobs!"
        self.flag = '0'

        return self.api_key, self.secret_key, self.passphrase, self.flag


