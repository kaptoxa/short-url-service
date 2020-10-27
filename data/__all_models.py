import datetime
import sqlalchemy
from sqlalchemy import orm
from .db import SqlAlchemyBase


class Short_url(SqlAlchemyBase):
    __tablename__ = 'short_urls'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        autoincrement=True
    )
    url = sqlalchemy.Column(
        sqlalchemy.String,
        unique=True
    )
    created = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.datetime.now
    )


class Long_url(SqlAlchemyBase):
    __tablename__ = 'long_urls'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        autoincrement=True
    )
    url = sqlalchemy.Column(
        sqlalchemy.Text,
        default='https://ru.wikipedia.org/wiki/NULL'
    )


class Pair(SqlAlchemyBase):
    __tablename__ = 'pairs'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        autoincrement=True
    )
    short = orm.relation(Short_url)
    long = orm.relation(Long_url)


class Transition(SqlAlchemyBase):
    __tablename__ = 'transitions'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        autoincrement=True
    )
    short = orm.relation(Short_url)
    time = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.datetime.now
    )
