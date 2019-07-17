# -*- coding: utf-8 -*-
# @Author  : wujiali
# @File    : Shell.py

"""
封装执行shell语句方法

"""

import subprocess
import os


class Shell:
    # """
    # 简单粗暴的方法
    # """
    # @staticmethod
    # def invoke(cmd):
    #   os.system(cmd)

    """
    重点：读取命令行的输出
    """
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o
