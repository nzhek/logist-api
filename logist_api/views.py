from aiohttp import web
from logist_api import query
from logist_api import exceptions
from logist_api.exceptions import RecordNotFound

import json
import datetime

routes = web.RouteTableDef()


def _default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()


@routes.get('/', name='index')
async def index(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(query.question.select())
        records = await cursor.fetchall()
        questions = [dict(q) for q in records]

        return web.json_response(
            json.loads(
                json.dumps(
                    {'questions': questions},
                    default=lambda o: o.isoformat() if isinstance(o, (datetime.date, datetime.datetime)) else None
                )))


@routes.get('/poll/{question_id}/', name='poll')
async def poll(request):
    async with request.app['db'].acquire() as conn:
        question_id = request.match_info['question_id']
        try:
            question, choices = await query.get_question(conn, question_id)
        except exceptions.RecordNotFound as e:
            raise web.HTTPNotFound(text=str(e))

        return web.json_response(json.loads(json.dumps({
            "question": {**question},
            "choices": [dict(q) for q in choices]
        }, default=_default)))


@routes.get("/employers/", name="employers")
async def employers_view(request):
    return web.json_response([
        {"id": 1, "full_name": "Чижик Пыжик Чижик", "position_id": 1},
        {"id": 2, "full_name": "Василенко Василий Васильевич", "position_id": 2},
        {"id": 3, "full_name": "Иванов Иван Иваныч", "position_id": 3},
    ])


@routes.get("/employers/{entry_id}/", name="employer_detail")
async def employer_view(request):
    return web.json_response({"id": 1, "full_name": "Чижик Пыжик Чижик", "position_id": 1})


@routes.get("/statuses/", name="statuses")
async def statuses_view(request):
    return web.json_response([
        {
            "id": 1,
            "name": "В пути",
            "code": "in_progress"
        },
        {
            "id": 2,
            "name": "Завершен",
            "code": "end"
        },
        {
            "id": 3,
            "name": "На ремонте",
            "code": "repair"
        },
        {
            "id": 4,
            "name": "В ожидании",
            "code": "wait"
        },
        {
            "id": 5,
            "name": "Оплачено",
            "code": "paid"
        },
        {
            "id": 6,
            "name": "Не оплачено",
            "code": "no_paid"
        }
    ])


@routes.get("/statuses/{entry_id}/", name="status_detail")
async def status_view(request):
    return web.json_response({
        "id": 1,
        "name": "В пути",
        "code": "in_progress"
    })


@routes.get("/positions/", name="positions")
async def positions_view(request):
    return web.json_response([
        {
            "id": 1,
            "title": "Логист"
        },
        {
            "id": 2,
            "title": "Водитель"
        },
        {
            "id": 3,
            "title": "Механик"
        },
        {
            "id": 4,
            "title": "Другое"
        }
    ])


@routes.get("/positions/{entry_id}/", name="position_detail")
async def position_view(request):
    return web.json_response({
        "id": 1,
        "title": "Логист"
    })


@routes.get("/cars/", name="cars")
async def cars_view(request):
    return web.json_response([
        {
            "id": 1,
            "title": "Камаз"
        },
        {
            "id": 2,
            "title": "Маз"
        },
        {
            "id": 3,
            "title": "Ивеко"
        }
    ])


@routes.get("/cars/{entry_id}/", name="car_detail")
async def car_view(request):
    return web.json_response({
        "id": 1,
        "title": "Камаз"
    })


@routes.get("/routes/", name="routes")
async def routes_view(request):
    result = await query.fetch_all_routes(request)

    data = [dict(r) for r in result]

    async def replace_all():
        for d in data:
            d["car"] = ''
            d["rate_without_percent"] = d['rate_common'] - (d['rate_common'] * (d['percent_org'] / 100))
            d["date_arrival"] = _default(d["date_arrival"]) if "date_arrival" in d else None
            d["date_departure"] = _default(d["date_departure"]) if "date_departure" in d else None

    await replace_all()
    return web.json_response({"data": data})


@routes.get("/routes/{entry_id}/", name="route_detail")
async def route_view(request):
    try:

        result = await query.fetch_route(request, request.match_info['entry_id'])

    except RecordNotFound as err:
        return web.HTTPNotFound(text=str(err))

    route = dict(result)
    route['car'] = ''
    route['rate_without_percent'] = route['rate_common'] - (route['rate_common'] * (route['percent_org'] / 100))
    route['date_arrival'] = _default(route['date_arrival']) if "date_arrival" in route else None
    route['date_departure'] = _default(route['date_departure']) if "date_departure" in route else None

    return web.json_response({"data": route})


@routes.post("/routes/", name="route_create")
async def route_create_view(request):
    post = await request.json()
    data = post.get('data')

    result = await query.insert_route(request, data)

    return web.json_response({
        "message": "Created!",
        "data": json.loads(
            json.dumps(
                {**result},
                default=lambda o: o.isoformat() if isinstance(o, (datetime.date, datetime.datetime)) else None
            ))
    }, status=201)


@routes.put("/routes/{entry_id}/", name="route_update")
async def route_update_view(request):
    entry_id = request.match_info['entry_id']
    put = await request.json()
    data = put.get('data')

    try:

        res = await query.update_route(request, entry_id, data)

    except RecordNotFound as err:
        return web.HTTPNotFound(text=str(err))

    route = dict(res)
    route["date_arrival"] = _default(route["date_arrival"])
    route["date_departure"] = _default(route["date_departure"])
    route["car"] = ''
    route["rate_without_percent"] = route['rate_common'] - (route['rate_common'] * (route['percent_org'] / 100))

    return web.json_response({
        "message": "Update!",
        "data": route
    }, status=200)


@routes.delete("/routes/{entry_id}/")
async def route_delete_view(request):
    return web.json_response({"message": "Delete!"})
