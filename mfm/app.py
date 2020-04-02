# coding:utf-8
"""
description:   flask app factory
author: jiangyx3915
date: 2020-03-15
"""
from flask import Flask
from mfm.extensions import db, api, migrate


def register_extensions(app: Flask) -> None:
    """
    register third extensions
    @:param app     flask app instance
    """
    api.init_app(app=app)
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)


def register_shell_context(app):
    """
    注册 shell 上下文
    :param app:
    :return:
    """
    from mfm.user.models import user

    def shell_context():
        return {'db': db, 'User': user.User}
    app.shell_context_processor(shell_context)


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
    register_extensions(app=app)
    register_shell_context(app=app)
    return app