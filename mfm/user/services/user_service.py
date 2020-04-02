# coding:utf-8
"""
description: 
author: jiangyx3915
date: 2020-03-15
"""
from mfm.user.models.user import User


class UserService:

    @classmethod
    def create_user(cls):
        pass

    @classmethod
    def is_exists_username(cls, username):
        return True if User.query.filter_by(username=username).first() else False
