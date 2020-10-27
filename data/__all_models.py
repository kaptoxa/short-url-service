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
    pairs = orm.relation("Pair", back_populates='short')
    transitions = orm.relation("Transition", back_populates='short')

    def __repr__(self):
        return f"Short: {self.url}, created: {self.created}"


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
    pairs = orm.relation("Pair", back_populates='long')

    def __repr__(self):
        return f"Long: {self.url}"


class Pair(SqlAlchemyBase):
    __tablename__ = 'pairs'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        autoincrement=True
    )
    short_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("short_urls.id")
    )
    short = orm.relation(Short_url, back_populates='pairs')
    long_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("long_urls.id")
    )
    long = orm.relation(Long_url, back_populates='pairs')

    def __repr__(self):
        return f"Link: {self.short_id} -> {self.long_id}"


class Transition(SqlAlchemyBase):
    __tablename__ = 'transitions'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        autoincrement=True
    )
    short_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("short_urls.id")
    )
    short = orm.relation(Short_url, back_populates='transitions')
    time = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.datetime.now
    )

    def __repr__(self):
        return f"Transition: {self.short_id} at {self.time}"