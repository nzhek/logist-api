from .models import route, status, position, car, employer
from .exceptions import RecordNotFound


class EmployerQuery:
    """ EmployerQuery
    """

    @classmethod
    async def fetch_all_employers(cls, request):
        async with request.app['db'].acquire() as conn:
            result = await (await conn.execute(employer.select().order_by(employer.c.id))).fetchall()
            return result

    @classmethod
    async def fetch_all_employers_by_position(cls, request, entry_id):
        async with request.app['db'].acquire() as conn:
            result = await (
                await conn.execute(
                    employer.select().where(employer.c.id == entry_id).order_by(employer.c.id))).fetchall()
            return result

    @classmethod
    async def fetch_employer(cls, request, entry_id):
        async with request.app['db'].acquire() as conn:
            result = await conn.execute(employer.select().where(employer.c.id == entry_id))
            row = await result.first()

            if not row:
                msg = f"Employer with id: {entry_id} does not exists"
                raise RecordNotFound(msg)

            return row

    @classmethod
    async def insert_employer(cls, request, data):
        async with request.app['db'].acquire() as conn:
            row_id = await conn.scalar(employer.insert().values(**data))

            q = await conn.execute(employer.select().where(employer.c.id == row_id))
            result = await q.first()

            return result

    @classmethod
    async def update_employer(cls, request, entry_id, data):
        async with request.app['db'].acquire() as conn:
            t1 = employer.select().where(employer.c.id == entry_id)
            row = await (await conn.execute(t1)).first()
            if not row:
                msg = f"Route with id: {entry_id} does not exists"
                raise RecordNotFound(msg)

            await conn.execute(employer.update().values(**data).where(employer.c.id == entry_id))

            q_q = await conn.execute(employer.select().where(employer.c.id == entry_id))
            q = await q_q.first()

            return q


class Route:
    """ Route
    """

    @classmethod
    async def fetch_with_filter(cls, request, filter_data):
        d = {k: v for (k, v) in filter_data.items() if v != ''}
        query = route.select()
        for k, v in d.items():
            if k in ('car_id', 'driver_id', 'logist_id', 'mechanic_id', 'status_id'):
                query = query.where(route.c[k].in_(v.split(',')))
            else:
                query = query.where(route.c[k] == v)

        async with request.app['db'].acquire() as conn:
            result = await (await conn.execute(query.order_by(route.c.id))).fetchall()
            return result

    @classmethod
    async def fetch_all_routes(cls, request):
        async with request.app['db'].acquire() as conn:
            result = await (await conn.execute(route.select().order_by(route.c.id))).fetchall()
            return result

    @classmethod
    async def fetch_route(cls, request, entry_id):
        async with request.app['db'].acquire() as conn:
            result = await conn.execute(route.select().where(route.c.id == entry_id))
            row = await result.first()

            if not row:
                msg = f"Route with id: {entry_id} does not exists"
                raise RecordNotFound(msg)

            return row

    @classmethod
    async def insert_route(cls, request, data):
        async with request.app['db'].acquire() as conn:
            row_id = await conn.scalar(route.insert().values(**data))

            q = await conn.execute(route.select().where(route.c.id == row_id))
            result = await q.first()

            return result

    @classmethod
    async def update_route(cls, request, entry_id, data):
        async with request.app['db'].acquire() as conn:
            t1 = route.select().where(route.c.id == entry_id)
            row = await (await conn.execute(t1)).first()
            if not row:
                msg = f"Route with id: {entry_id} does not exists"
                raise RecordNotFound(msg)

            await conn.execute(route.update().values(**data).where(route.c.id == entry_id))

            q_q = await conn.execute(route.select().where(route.c.id == entry_id))
            q = await q_q.first()

            return q


class Status:
    """ Status
    """

    @classmethod
    async def fetch_all_statuses(cls, request):
        async with request.app['db'].acquire() as conn:
            result = await (await conn.execute(status.select().order_by(status.c.id))).fetchall()
            return result

    @classmethod
    async def insert_status(cls, request, data):
        async with request.app['db'].acquire() as conn:
            row_id = await conn.scalar(status.insert().values(**data))

            q = await conn.execute(status.select().where(status.c.id == row_id))
            result = await q.first()

            return result

    @classmethod
    async def fetch_status(cls, request, entry_id):
        async with request.app['db'].acquire() as conn:
            result = await conn.execute(status.select().where(status.c.id == entry_id))
            row = await result.first()

            if not row:
                msg = f"Status with id: {entry_id} does not exists"
                raise RecordNotFound(msg)

            return row

    @classmethod
    async def update_status(cls, request, entry_id, data):
        async with request.app['db'].acquire() as conn:
            t1 = status.select().where(status.c.id == entry_id)
            row = await (await conn.execute(t1)).first()
            if not row:
                msg = f"Status with id: {entry_id} does not exists"
                raise RecordNotFound(msg)

            await conn.execute(status.update().values(**data).where(status.c.id == entry_id))

            q_q = await conn.execute(status.select().where(status.c.id == entry_id))
            q = await q_q.first()

            return q


class Position:
    """ Position
    """

    @classmethod
    async def fetch_all_positions(cls, request):
        async with request.app['db'].acquire() as conn:
            result = await (await conn.execute(position.select().order_by(position.c.id))).fetchall()
            return result

    @classmethod
    async def insert_position(cls, request, data):
        async with request.app['db'].acquire() as conn:
            row_id = await conn.scalar(position.insert().values(**data))

            q = await conn.execute(position.select().where(position.c.id == row_id))
            result = await q.first()

            return result

    @classmethod
    async def fetch_position(cls, request, entry_id):
        async with request.app['db'].acquire() as conn:
            result = await conn.execute(position.select().where(position.c.id == entry_id))
            row = await result.first()

            if not row:
                msg = f"Position with id: {entry_id} does not exists"
                raise RecordNotFound(msg)

            return row

    @classmethod
    async def update_position(cls, request, entry_id, data):
        async with request.app['db'].acquire() as conn:
            t1 = position.select().where(position.c.id == entry_id)
            row = await (await conn.execute(t1)).first()
            if not row:
                msg = f"Position with id: {entry_id} does not exists"
                raise RecordNotFound(msg)

            await conn.execute(position.update().values(**data).where(position.c.id == entry_id))

            q_q = await conn.execute(position.select().where(position.c.id == entry_id))
            q = await q_q.first()

            return q


class Car:
    """ Car
    """

    @classmethod
    async def fetch_all_cars(cls, request):
        async with request.app['db'].acquire() as conn:
            result = await (await conn.execute(car.select().order_by(car.c.id))).fetchall()
            return result

    @classmethod
    async def insert_car(cls, request, data):
        async with request.app['db'].acquire() as conn:
            row_id = await conn.scalar(car.insert().values(**data))

            q = await conn.execute(car.select().where(car.c.id == row_id))
            result = await q.first()

            return result

    @classmethod
    async def fetch_car(cls, request, entry_id):
        async with request.app['db'].acquire() as conn:
            result = await conn.execute(car.select().where(car.c.id == entry_id))
            row = await result.first()

            if not row:
                msg = f"Position with id: {entry_id} does not exists"
                raise RecordNotFound(msg)

            return row

    @classmethod
    async def update_car(cls, request, entry_id, data):
        async with request.app['db'].acquire() as conn:
            t1 = car.select().where(car.c.id == entry_id)
            row = await (await conn.execute(t1)).first()
            if not row:
                msg = f"Car with id: {entry_id} does not exists"
                raise RecordNotFound(msg)

            await conn.execute(car.update().values(**data).where(car.c.id == entry_id))

            q_q = await conn.execute(car.select().where(car.c.id == entry_id))
            q = await q_q.first()

            return q
