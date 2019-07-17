#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/15 18:21
# @Author  : wujiali
# @Site    : 
# @File    : test_update_product.py
# @Software: PyCharm

import allure
from Params.params import Update
from Conf.Config import Config
import requests
from Common import Assert
from Common import Consts
from Common import Token
import json

class TestUpPro:
    @allure.feature('panda plus 接口测试')
    @allure.story("更新商品信息")
    @allure.severity('Normal')
    @allure.step("登录->更新商品信息")
    def test_update_product(self):
      token = Token.Token()
      conf = Config()
      data = Update()
      test = Assert.Assertions()

      host = conf.host_test
      req_url = 'http://' + host
      urls = req_url + data.url[0]
      products = data.data
      token = token.get_token("test")
      header = data.header
      header[0].update(token)

      response = requests.post(urls,data=json.dumps(products[0]), headers=header[0])
      print(response)
      print("------------------我是可爱的分界线----------------------------")
      r_data = response.json()

    # 断言
      allure.attach('实际结果', '{}'.format(r_data))
      assert test.assert_code(response.status_code, 200)
      assert test.assert_body(r_data,"message","update product success")

      Consts.RESULT_LIST.append('True')