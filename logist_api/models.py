from sqlalchemy import (MetaData, Table, Column, ForeignKey, Integer, String, Date, Text)

__all__ = ['question', 'choice', 'employer', 'position', 'car', 'status', 'route']

meta = MetaData()

question = Table(
    'question', meta,
    Column('id', Integer, primary_key=True),
    Column('question_text', String(200), nullable=False),
    Column('pub_date', Date, nullable=False)
)

choice = Table(
    'choice', meta,
    Column('id', Integer, primary_key=True),
    Column('choice_text', String(200), nullable=False),
    Column('votes', Integer, server_default='0', nullable=False),
    Column('question_id', Integer, ForeignKey('question.id', ondelete='CASCADE'))
)

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

    Column('employer_id', Integer, ForeignKey('employer.id')),
    Column('car_id', Integer, ForeignKey('car.id')),
    Column('status_id', Integer, ForeignKey('status.id')),
)
