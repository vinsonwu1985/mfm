# coding:utf-8
"""
description:    define flask config
author: jiangyx3915
date: 2020-03-15
"""
from mfm.env import env, ENV_TYPE


class BaseConfig:
    DEBUG = ENV_TYPE == 'dev'
    SECRET_KEY = env.str('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = env.str('SQLALCHEMY_DATABASE_URI')


class DevConfig(BaseConfig):
    pass


class TestConfig(BaseConfig):
    pass


class ProdConfig(BaseConfig):
    pass


settings_mapper = {
    "dev": DevConfig,
    "test": TestConfig,
    "prod": ProdConfig
}