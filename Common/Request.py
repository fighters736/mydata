# -*- coding: utf-8 -*-
# @Author  : wujiali
# @File    : Request.py

"""
封装request

"""

import requests
import json


class Request:

    def __init__(self):
        """
        :param env:
        """
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json"}

    def get_request_params(self, url, data):
        """
        Get请求：请求格式为"http://xxxx/xx?key1=value1&key2=value2"
        :param url:
        :param data:数据格式为{key1:value1,key2=value2}
        :return:

        """
        response = self.session.get(url,params =data)
        return response

    def get_request_params(self, url, data,header):
        """
        Get请求：请求头变更时
        :param url:
        :param data:
        :return:

        """
        response = self.session.get(url,params =data,headers = header)
        return response

    def get_request(self,url,data):
        """
         Get请求：请求格式为"http://xxxx/xx/value"
         :param url:
         :param data:
         :return:

         """
        urls = url + '/' + data
        response = self.session.get(urls)
        return response

    def get_request(self, url, data,header):
        """
         Get请求：请求头变更时
         :param url:
         :param data:
         :return:

         """
        urls = url + '/' + data
        response = self.session.get(urls,headers = header)
        return response

    def post_request_data(self,url,data):
        """
             Post请求：
             :param url:
             :param data:为python中的字典类型
             :return:

             """
        response = self.session.post(url,data = json.dumps(data))
        return response

    def post_request_data(self,url,data,header):
        """
             Post请求：请求头变更时
             :param url:
             :param data:为python中的字典类型
             :return:

             """
        response = self.session.post(url,data = json.dumps(data),headers = header)
        return response

    def post_request_json(self,url,data):
        """
             Post请求：
             :param url:
             :param data:json格式
             :return:

             """
        response = self.session.post(url,json = data)
        return response

    def post_request_json(self,url,data,header):
        """
             Post请求：请求头变更时
             :param url:
             :param data:json格式
             :return:

             """
        response = self.session.post(url,json = data,header = header)
        return response