#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 17:46
# @Author  : wujiali
# @Site    :
# @File    : test_user_login.py
# @Software: PyCharm

import allure
from Conf.Config import Config
from Params.params import Basic
import requests
from Common import Assert
import json
from Common import Consts

class TestLogin:

    @allure.feature('panda plus 接口测试')
    @allure.story("用户登录")
    @allure.severity('blocker')
    @allure.step("登录接口")
    def test_user_login(self):
        """
            用例描述：登陆
        """
        conf = Config()
        data = Basic()
        test = Assert.Assertions()

        host = conf.host_test
        req_url = 'http://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[0]
        response = requests.post(api_url,data=json.dumps(params[0]),headers=headers[0])
        r_data = response.json()

        # 断言
        allure.attach("实际结果","{}".format(r_data))
        assert test.assert_code(response.status_code,200)
        Consts.RESULT_LIST.append('True')

