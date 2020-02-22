from sqlalchemy import create_engine, MetaData

from logist_api.settings import config
from logist_api.models import employer, position, car, status, route

DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"


def create_table(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[employer, position, car, status, route])


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)

    create_table(engine)
