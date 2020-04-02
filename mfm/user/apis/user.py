# coding:utf-8
"""
description: 
author: jiangyx3915
date: 2020-03-15
"""
import json
from flask import request, jsonify
from flask_api_resource.api import BaseResource
from flask_api_resource.decorator import post


class UserResource(BaseResource):
    def get_urls(self):
        return [
            ('/register', self.register)
        ]

    @post
    def register(self):
        data = self.get_data()
        return jsonify({'status': True, 'data': data})


