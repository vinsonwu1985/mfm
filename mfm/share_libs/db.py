# coding:utf-8
"""
description: 
author: jiangyx3915
date: 2020-03-15
"""
import time
from mfm.extensions import db

Column = db.Column
String = db.String
Boolean = db.Boolean


def now_timestamp() -> int:
    """
    生成当前时间的时间戳
    :return:
    """
    return int(time.time())


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, default=True, doc='状态')
    create_time = db.Column(db.Integer, nullable=False, default=now_timestamp, doc="创建时间")
    update_time = db.Column(db.Integer, nullable=True, doc="修改时间")

    @classmethod
    def create(cls, **kwargs):
        """
        创建一个新记录并保存于数据库中
        :param kwargs:
        :return:
        """
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """
        更新记录
        :param commit:
        :param kwargs:
        :return:
        """
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        if hasattr(self, 'update_time'):
            setattr(self, 'update_time', now_timestamp())
        return commit and self.save() or self

    def save(self, commit=True):
        """
        保存记录
        :param commit:
        :return:
        """
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True) -> bool:
        """
        从数据库中移除记录
        :param commit:
        :return:
        """
        self.update(commit=commit, id=self.id, active=False)
        return commit and db.session.commit()

    @classmethod
    def get_by_id(cls, record_id):
        """
        根据记录id获取记录
        :param record_id:
        :return:
        """
        if any((
                isinstance(record_id, str) and record_id.isdigit(),
                isinstance(record_id, (int, float))
        )):
            return cls.query.get(int(record_id))
        return None
