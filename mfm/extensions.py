# coding:utf-8
"""
description: 
author: jiangyx3915
date: 2020-03-15
"""
from flask_api_resource import FlaskApiResource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


api = FlaskApiResource()
db = SQLAlchemy()
migrate = Migrate()
