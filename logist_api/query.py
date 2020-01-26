from .models import question, choice, route
from .exceptions import RecordNotFound
import sqlalchemy as sa


async def get_question(conn, question_id):
    result = await conn.execute(question.select().where(question.c.id == question_id))
    question_record = await result.first()

    if not question_record:
        msg = f"Question with id: {question_id} does not exists"
        raise RecordNotFound(msg)

    result = await conn.execute(choice.select().where(choice.c.question_id == question_id).order_by(choice.c.id))

    choice_records = await result.fetchall()

    return question_record, choice_records


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
