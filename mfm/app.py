# coding:utf-8
"""
description:   flask app factory
author: jiangyx3915
date: 2020-03-15
"""
from flask import Flask


def register_extensions(app: Flask) -> None:
    """
    register third extensions
    @:param app     flask app instance
    """
    from mfm.extensions import db, api, migrate
    api.init_app(app=app)
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)


def create_app(env: str = 'dev') -> Flask:
    """
    flask app factory to create app instance
    :param env:     config type。dev、test or prod
    :return:        flask app instance
    """
    from mfm.settings import settings_mapper
    app = Flask(__name__)
    conf = settings_mapper.get(env)
    if not conf:
        raise Exception(f'Can not load config type {env}。You must provide it!')
    app.config.from_object(conf)
    return app