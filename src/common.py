import requests
import unittest

class Common(unittest.TestCase):

    # common的构造函数
    def __init__(self, url_root):
        # 被测系统根路由
        self.url_root = url_root

    # 封装 get 请求
    def get(self, uri='', params=''):
        url = self.url_root + uri
        # url = self.url_root + uri + params 也可以写成这样
        if len(params) > 0:
            res = requests.get(url, params=params)
        else:
            res = requests.get(url)
        return res

    # 封装 post 请求
    def post(self, uri, params=''):
        url = self.url_root + uri
        if len(params) > 0:
            res = requests.post(url, data=params)
        else:
            res = requests.post(url)
        return res
