#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/15 18:23
# @Author  : wujiali
# @Site    : 
# @File    : test_get_product_detail.py
# @Software: PyCharm


import allure
from Params.params import Details
from Conf.Config import Config
import requests
from Common import Assert
from Common import Consts
from Common import Token

class TestProDet:
    @allure.feature('panda plus 接口测试')
    @allure.story("请求商品列表")
    @allure.severity('Normal')
    @allure.step("登录->获取商品详情")
    def test_get_pro_details(self):
      token = Token.Token()
      conf = Config()
      data = Details()
      test = Assert.Assertions()

      host = conf.host_test
      req_url = 'http://' + host
      urls = req_url + data.url[0]
      headers = token.get_token("test")
      product_id = data.data
      params = urls + "/" + str(product_id[0])

      response = requests.get(params, headers=headers)
      print(response)
      print("------------------我是可爱的分界线----------------------------")
      r_data = response.json()

    # 断言
      allure.attach('实际结果', '{}'.format(r_data))
      assert test.assert_code(response.status_code, 200)
      assert test.assert_body_key(r_data, 'data')

      Consts.RESULT_LIST.append('True')