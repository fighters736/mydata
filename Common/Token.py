#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 16:32
# @Author  : wujiali
# @Site    : 
# @File    : Token.py
# @Software: PyCharm

"""
封装获取Token方法
"""

from Common import Log
from Conf import Config
import requests

class Token:
    def __init__(self):
        self.config = Config.Config()
        self.log = Log.MyLog()

    def get_token(self,env):
        """
        获取环境登录后的token
        :param evn: 环境变量
        :return: token
        """
        headers = {
            "Content-Type": "application/json"
        }

        if env == "test":
            login_url = 'http://' + self.config.loginHost_test
            parm = self.config.loginInfo_test
            print(parm)
            response = requests.post(login_url, data=parm, headers=headers)
            r_data = response.json()
            data = r_data["token"]
            self.log.debug('token: %s'%data)
            res = {"Token":data}
            return res

        elif env == "online":
            login_url = 'http://' + self.config.loginHost_online
            parm = self.config.loginInfo_online

            response = requests.post(login_url, data =parm, headers=headers)
            r_data = response.json()
            data = r_data["token"]
            self.log.debug('token: %s' % data)
            res = {"Token": data}
            return res
        else:
            print("get token error")
            self.log.error('get token error, please checkout!!!')

