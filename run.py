# coding:utf-8
"""
description:  flask run start
author: jiangyx3915
date: 2020-03-15
"""
from mfm.env import ENV_TYPE
from mfm.app import create_app


app = create_app(env=ENV_TYPE)
