# coding:utf-8
"""
description: User(用户) 模块
author: jiangyx3915
date: 2020-03-15
"""


def register(api):
    from .apis import user
    api.register(user.UserResource)
