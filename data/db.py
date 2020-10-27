import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec

SqlAlchemyBase = dec.declarative_base()

__factory = None


def global_init(db_name):
    global __factory

    if __factory:
        return

    if not db_name or not db_name.strip():
        raise Exception("Необходимо имя базы данных Postgre.")

    conn_str = f'postgresql+psycopg2://postgres:back1nblack@127.0.0.1:5432/{db_name.strip()}'
    print(f"Подключение к базе данных по адресу {conn_str}")

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    from . import __all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()
