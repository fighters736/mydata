# -*- coding: utf-8 -*-
# @Author  : wujiali
# @File    : Session.py

"""
封装获取cookie方法

"""

import requests

from Common import Log
from Conf import Config


class Session:
    def __init__(self):
        self.config = Config.Config()
        self.log = Log.MyLog()

    def get_session(self, env):
        """
        获取session
        :param env: 环境变量
        :return:
        """
        headers = {
            "Content-Type": "application/json"
        }

        if env == "test":
            login_url = 'http://' + self.config.loginHost_test
            parm = self.config.loginInfo_test

            session_debug = requests.session()
            response = session_debug.post(login_url, parm, headers=headers)
            print(response.cookies)
            self.log.debug('cookies: %s' % response.cookies.get_dict())
            return response.cookies.get_dict()

        elif env == "online":
            login_url = 'http://' + self.config.loginHost_online
            parm = self.config.loginInfo_online

            session_release = requests.session()
            response = session_release.post(login_url, parm, headers=headers)
            print(response.cookies)
            self.log.debug('cookies: %s' % response.cookies.get_dict())
            return response.cookies.get_dict()

        else:
            print("get cookies error")
            self.log.error('get cookies error, please checkout!!!')


if __name__ == '__main__':
    ss = Session()
    ss.get_session('test')