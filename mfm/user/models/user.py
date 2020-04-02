# coding:utf-8
"""
description: 
author: jiangyx3915
date: 2020-03-15
"""
from mfm.share_libs.db import Column, BaseModel, String, Boolean


class User(BaseModel):
    username = Column(String(length=32), doc="用户名")
    password = Column(String(length=32), doc="用户密码")
    email = Column(String(length=50), doc="邮箱")
    is_email_valid = Column(Boolean, doc="是否激活邮箱")