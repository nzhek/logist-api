from aiohttp import web
from logist_api import query
from logist_api.exceptions import RecordNotFound

import json
import datetime

routes = web.RouteTableDef()


def _default(o):
    return o.isoformat() if isinstance(o, (datetime.date, datetime.datetime)) else None


""" Employers """


@routes.get("/employers", name="employers")
async def employers_view(request):
    result = await query.fetch_all_employers(request)

    data = json.dumps([{**r} for r in result]) if result else None

    return web.json_response({"data": json.loads(data) if data else None})


@routes.post("/employers", name="employers_create")
async def employers_create_view(request):
    post = await request.json()
    data = post.get('data')
    if not data:
        return web.json_response({"message": "Error incorrect data"}, status=400)

    result = await query.insert_employer(request, data)

    return web.json_response({
        "message": "Created!",
        "data": json.loads(json.dumps(dict(result)))
    }, status=201)


@routes.get("/employers/{entry_id}", name="employer_detail")
async def employer_view(request):
    try:

        result = await query.fetch_position(request, request.match_info['entry_id'])

    except RecordNotFound as err:
        return web.HTTPNotFound(text=str(err))

    return web.json_response({"data": json.loads(json.dumps(dict(result)))})


@routes.put("/employers/{entry_id}", name="employer_update")
async def employer_update_view(request):
    entry_id = request.match_info['entry_id']
    put = await request.json()
    data = put.get('data')

    try:

        result = await query.update_employer(request, entry_id, data)

    except RecordNotFound as err:
        return web.HTTPNotFound(text=str(err))

    return web.json_response({
        "message": "Update!",
        "data": json.loads(json.dumps(dict(result)))
    }, status=200)


""" Statuses """


@routes.get("/statuses", name="statuses")
async def statuses_view(request):
    result = await query.fetch_all_statuses(request)

    data = json.dumps([{**r} for r in result]) if result else None

    return web.json_response({"data": json.loads(data) if data else None})


@routes.post("/statuses", name="statuses_create")
async def statuses_create_view(request):
    post = await request.json()
    data = post.get('data')
    if not data:
        return web.json_response({"message": "Error incorrect data"}, status=400)

    result = await query.insert_status(request, data)

    return web.json_response({
        "message": "Created!",
        "data": json.dumps(dict(result))
    }, status=201)


@routes.get("/statuses/{entry_id}", name="status_detail")
async def status_view(request):
    try:

        result = await query.fetch_status(request, request.match_info['entry_id'])

    except RecordNotFound as err:
        return web.HTTPNotFound(text=str(err))

    return web.json_response({"data": json.loads(json.dumps(dict(result)))})


@routes.put("/statuses/{entry_id}", name="status_update")
async def status_update_view(request):
    entry_id = request.match_info['entry_id']
    put = await request.json()
    data = put.get('data')

    try:

        result = await query.update_status(request, entry_id, data)

    except RecordNotFound as err:
        return web.HTTPNotFound(text=str(err))

    return web.json_response({
        "message": "Update!",
        "data": json.loads(json.dumps(dict(result)))
    }, status=200)


""" Positions """


@routes.get("/positions", name="positions")
async def positions_view(request):
    result = await query.fetch_all_positions(request)

    data = json.dumps([{**r} for r in result]) if result else None

    return web.json_response({"data": json.loads(data) if data else None})


@routes.post("/positions", name="positions_create")
async def positions_create_view(request):
    post = await request.json()
    data = post.get('data')
    if not data:
        return web.json_response({"message": "Error incorrect data"}, status=400)

    result = await query.insert_position(request, data)

    return web.json_response({
        "message": "Created!",
        "data": json.loads(json.dumps({**result}))
    }, status=201)


@routes.get("/positions/{entry_id}", name="position_detail")
async def position_view(request):
    try:

        result = await query.fetch_position(request, request.match_info['entry_id'])

    except RecordNotFound as err:
        return web.HTTPNotFound(text=str(err))

    return web.json_response({"data": json.loads(json.dumps(dict(result)))})


@routes.put("/positions/{entry_id}", name="position_update")
async def position_update_view(request):
    entry_id = request.match_info['entry_id']
    put = await request.json()
    data = put.get('data')

    try:

        result = await query.update_position(request, entry_id, data)

    except RecordNotFound as err:
        return web.HTTPNotFound(text=str(err))

    return web.json_response({
        "message": "Update!",
        "data": json.loads(json.dumps(dict(result)))
    }, status=200)


@routes.get("/positions/{entry_id}/employers", name="position_employers")
async def position_employers_view(request):
    pos_id = request.match_info['entry_id']

    result = await query.fetch_all_employers_by_position(request, pos_id)

    data = json.dumps([{**r} for r in result]) if result else None

    return web.json_response({"data": json.loads(data) if data else None})


""" Cars """


@routes.get("/cars", name="cars")
async def cars_view(request):
    result = await query.fetch_all_cars(request)

    data = json.loads(json.dumps([{**r} for r in result])) if result else None

    return web.json_response({"data": data})


@routes.post("/cars", name="cars_create")
async def cars_create_view(request):
    post = await request.json()
    data = post.get('data')
    if not data:
        return web.json_response({"message": "Error incorrect data"}, status=400)

    result = await query.insert_car(request, data)

    return web.json_response({
        "message": "Created!",
        "data": json.loads(json.dumps({**result}))
    }, status=201)


@routes.get("/cars/{entry_id}", name="car_detail")
async def car_view(request):
    try:

        result = await query.fetch_car(request, request.match_info['entry_id'])

    except RecordNotFound as err:
        return web.HTTPNotFound(text=str(err))

    return web.json_response({"data": json.loads(json.dumps({**result}))})


@routes.put("/cars/{entry_id}", name="car_update")
async def car_update_view(request):
    entry_id = request.match_info['entry_id']
    put = await request.json()
    data = put.get('data')

    try:

        result = await query.update_car(request, entry_id, data)

    except RecordNotFound as err:
        return web.HTTPNotFound(text=str(err))

    return web.json_response({
        "message": "Update!",
        "data": json.loads(json.dumps(dict(result)))
    }, status=200)


""" Routes """


@routes.get("/routes", name="routes")
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
    return web.json_response({"data": data if data else None})


@routes.get("/routes/{entry_id}", name="route_detail")
async def route_view(request):
    try:

        result = await query.fetch_route(request, request.match_info['entry_id'])

    except RecordNotFound as err:
        return web.HTTPNotFound(text=str(err))

    route = dict(result)
    route['rate_without_percent'] = route['rate_common'] - (route['rate_common'] * (route['percent_org'] / 100))
    route['date_arrival'] = _default(route['date_arrival']) if "date_arrival" in route else None
    route['date_departure'] = _default(route['date_departure']) if "date_departure" in route else None

    return web.json_response({"data": route if route else None})


@routes.post("/routes", name="route_create")
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


@routes.put("/routes/{entry_id}", name="route_update")
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
    # route["rate_without_percent"] = route['rate_common'] - (route['rate_common'] * (route['percent_org'] / 100))

    return web.json_response({
        "message": "Update!",
        "data": route
    }, status=200)


@routes.delete("/routes/{entry_id}")
async def route_delete_view(request):
    return web.json_response({"message": "Delete!"})
