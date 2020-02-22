from sqlalchemy import Table, Column, Integer, String, MetaData, Text, ForeignKey, Date
from migrate import *

meta = MetaData()

employer = Table(
    'employer', meta,
    Column('id', Integer, primary_key=True),
    Column('full_name', String(250), nullable=False),
    Column('position_id', Integer, ForeignKey('position.id', ondelete='SET NULL'))
)

position = Table(
    'position', meta,
    Column('id', Integer, primary_key=True),
    Column('title', String(250), nullable=False),
)

car = Table(
    'car', meta,
    Column('id', Integer, primary_key=True),
    Column('title', String(250), nullable=False),
)

status = Table(
    'status', meta,
    Column('id', Integer, primary_key=True),
    Column('title', String(250), nullable=False),
    Column('code', String(25), nullable=False),
)

route = Table(
    'route', meta,
    Column('id', Integer, primary_key=True),
    Column('title', String(500), nullable=False),
    Column('comment', Text, nullable=True),
    Column('rate_platon', Integer, server_default='0', nullable=False),
    Column('mileage', Integer, server_default='0', nullable=False),
    Column('quantity_trip_day', Integer, server_default='0', nullable=False),
    Column('rate_common', Integer, server_default='0', nullable=False),
    Column('percent_org', Integer, server_default='0', nullable=False),
    Column('percent_mechanic', Integer, server_default='0', nullable=False),
    Column('percent_driver', Integer, server_default='0', nullable=False),
    Column('percent_logist', Integer, server_default='0', nullable=False),

    Column('date_arrival', Date, nullable=False),
    Column('date_departure', Date, nullable=False),

    Column('driver_id', Integer, ForeignKey('employer.id')),
    Column('logist_id', Integer, ForeignKey('employer.id')),
    Column('mechanic_id', Integer, ForeignKey('employer.id')),

    Column('car_id', Integer, ForeignKey('car.id')),
    Column('status_id', Integer, ForeignKey('status.id')),
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    map(lambda x: x.create(), reversed((route, employer, position, status, car)))


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    map(lambda x: x.drop(), (route, employer, position, status, car))
