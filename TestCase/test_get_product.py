#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 16:12
# @Author  : wujiali
# @Site    : 
# @File    : test_get_product.py
# @Software: PyCharm

import allure
from Params.params import Product
from Conf.Config import Config
import requests
from Common import Assert
from Common import Consts
from Common import Token


class TestProPip:

    @allure.feature('panda plus 接口测试')
    @allure.story("请求商品列表")
    @allure.severity('Normal')
    @allure.step("登录->获取商品列表")
    def test_get_pro(self):
        """
           用例描述：获取商品列表
        :return:
        """
        token = Token.Token()
        conf = Config()
        data = Product()
        test = Assert.Assertions()

        host = conf.host_test
        req_url = 'http://' + host
        urls = req_url + data.url[0]
        headers = token.get_token("test")
        shop_id = data.data
        params = urls + "?" + "shop_id=" + str(shop_id[0])

        response = requests.get(params,headers = headers)
        print("------------------我是可爱的分界线----------------------------")
        r_data = response.json()

        # 断言
        allure.attach('实际结果','{}'.format(r_data))
        assert test.assert_code(response.status_code,200)
        assert test.assert_body_key(r_data,'data')
        assert test.assert_body_key(r_data,'page')
        assert test.assert_body_key(r_data,'size')
        assert test.assert_body_key(r_data,'total')

        Consts.RESULT_LIST.append('True')




