from .models import route, status, position, car, employer
from .exceptions import RecordNotFound

""" Employers """


async def fetch_all_employers(request):
    async with request.app['db'].acquire() as conn:
        result = await (await conn.execute(employer.select().order_by(employer.c.id))).fetchall()
        return result


async def fetch_all_employers_by_position(request, entry_id):
    async with request.app['db'].acquire() as conn:
        result = await (
            await conn.execute(employer.select().where(employer.c.id == entry_id).order_by(employer.c.id))).fetchall()
        return result


async def fetch_employer(request, entry_id):
    async with request.app['db'].acquire() as conn:
        result = await conn.execute(employer.select().where(employer.c.id == entry_id))
        row = await result.first()

        if not row:
            msg = f"Employer with id: {entry_id} does not exists"
            raise RecordNotFound(msg)

        return row


async def insert_employer(request, data):
    async with request.app['db'].acquire() as conn:
        row_id = await conn.scalar(employer.insert().values(**data))

        q = await conn.execute(employer.select().where(employer.c.id == row_id))
        result = await q.first()

        return result


async def update_employer(request, entry_id, data):
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


""" Routes """


async def fetch_all_routes(request):
    async with request.app['db'].acquire() as conn:
        result = await (await conn.execute(route.select().order_by(route.c.id))).fetchall()
        return result


async def fetch_route(request, entry_id):
    async with request.app['db'].acquire() as conn:
        result = await conn.execute(route.select().where(route.c.id == entry_id))
        row = await result.first()

        if not row:
            msg = f"Route with id: {entry_id} does not exists"
            raise RecordNotFound(msg)

        return row


async def insert_route(request, data):
    async with request.app['db'].acquire() as conn:
        row_id = await conn.scalar(route.insert().values(**data))

        q = await conn.execute(route.select().where(route.c.id == row_id))
        result = await q.first()

        return result


async def update_route(request, entry_id, data):
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


""" Status """


async def fetch_all_statuses(request):
    async with request.app['db'].acquire() as conn:
        result = await (await conn.execute(status.select().order_by(status.c.id))).fetchall()
        return result


async def insert_status(request, data):
    async with request.app['db'].acquire() as conn:
        row_id = await conn.scalar(status.insert().values(**data))

        q = await conn.execute(status.select().where(status.c.id == row_id))
        result = await q.first()

        return result


async def fetch_status(request, entry_id):
    async with request.app['db'].acquire() as conn:
        result = await conn.execute(status.select().where(status.c.id == entry_id))
        row = await result.first()

        if not row:
            msg = f"Status with id: {entry_id} does not exists"
            raise RecordNotFound(msg)

        return row


async def update_status(request, entry_id, data):
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


""" Positions """


async def fetch_all_positions(request):
    async with request.app['db'].acquire() as conn:
        result = await (await conn.execute(position.select().order_by(position.c.id))).fetchall()
        return result


async def insert_position(request, data):
    async with request.app['db'].acquire() as conn:
        row_id = await conn.scalar(position.insert().values(**data))

        q = await conn.execute(position.select().where(position.c.id == row_id))
        result = await q.first()

        return result


async def fetch_position(request, entry_id):
    async with request.app['db'].acquire() as conn:
        result = await conn.execute(position.select().where(position.c.id == entry_id))
        row = await result.first()

        if not row:
            msg = f"Position with id: {entry_id} does not exists"
            raise RecordNotFound(msg)

        return row


async def update_position(request, entry_id, data):
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


""" Cars """


async def fetch_all_cars(request):
    async with request.app['db'].acquire() as conn:
        result = await (await conn.execute(car.select().order_by(car.c.id))).fetchall()
        return result


async def insert_car(request, data):
    async with request.app['db'].acquire() as conn:
        row_id = await conn.scalar(car.insert().values(**data))

        q = await conn.execute(car.select().where(car.c.id == row_id))
        result = await q.first()

        return result


async def fetch_car(request, entry_id):
    async with request.app['db'].acquire() as conn:
        result = await conn.execute(car.select().where(car.c.id == entry_id))
        row = await result.first()

        if not row:
            msg = f"Position with id: {entry_id} does not exists"
            raise RecordNotFound(msg)

        return row


async def update_car(request, entry_id, data):
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
