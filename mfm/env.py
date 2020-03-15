# coding:utf-8
"""
description:  env file，provide base env params
author: jiangyx3915
date: 2020-03-15
"""
from environs import Env


env: Env = Env()
env.read_env()
ENV_TYPE = env.str('ENV_TYPE', 'dev')
