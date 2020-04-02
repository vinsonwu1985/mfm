# coding:utf-8
"""
description: 
author: jiangyx3915
date: 2020-03-29
"""
from pydantic import BaseModel, validator, ValidationError
from mfm.user.services.user_service import UserService


class UserVO(BaseModel):
    username: str
    email: str
    password: str
    re_password: str

    @validator('username')
    def username_unique(self, v):
        """
        用户名必须唯一
        :param v:
        :return:
        """
        if UserService.is_exists_username(username=v):
            raise ValueError('该用户名已存在')
        return v


    pass
