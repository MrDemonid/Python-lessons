import sqlalchemy as sa
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as dec
from sqlalchemy.orm import Session


SqlAlchemyBase = dec.declarative_base()

__factory = None

'''
    Подключение к базе данных
'''
def global_init(db_file):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception('Необходимо указать файл базы данных.')

    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'

    print(f'Подключение к базе данных по адресу {conn_str}')

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    from . import __all_models

    SqlAlchemyBase.metadata.create_all(engine)


'''
    Сессия
'''
def create_session() -> Session:
    global __factory
    return __factory()
