from aiohttp import web
from logist_api import query
from logist_api.exceptions import RecordNotFound

import json
import datetime

routes = web.RouteTableDef()


def _default(o):
    return o.isoformat() if isinstance(o, (datetime.date, datetime.datetime)) else None


@routes.view("/employers")
class EmployerView(web.View):
    """ Employers
    """

    async def get(self):
        result = await query.EmployerQuery.fetch_all_employers(self.request)

        data = json.dumps([{**r} for r in result]) if result else None

        return web.json_response({"data": json.loads(data) if data else None})

    async def post(self):
        post = await self.request.json()
        data = post.get('data')
        if not data:
            return web.json_response({"message": "Error incorrect data"}, status=400)

        result = await query.EmployerQuery.insert_employer(self.request, data)

        return web.json_response({
            "message": "Created!",
            "data": json.loads(json.dumps(dict(result)))
        }, status=201)


@routes.view("/employers/{entry_id}")
class EmployerEntryView(web.View):
    """ Employers
    """

    async def get(self):
        try:
            result = await query.Position.fetch_position(self.request, self.request.match_info['entry_id'])
        except RecordNotFound as err:
            return web.HTTPNotFound(text=str(err))

        return web.json_response({"data": json.loads(json.dumps(dict(result)))})

    async def put(self):
        entry_id = self.request.match_info['entry_id']
        put = await self.request.json()
        data = put.get('data')

        try:
            result = await query.EmployerQuery.update_employer(self.request, entry_id, data)
        except RecordNotFound as err:
            return web.HTTPNotFound(text=str(err))

        return web.json_response({
            "message": "Update!",
            "data": json.loads(json.dumps(dict(result)))
        }, status=200)


@routes.view("/statuses")
class StatusView(web.View):
    """ Statuses
    """

    async def get(self):
        result = await query.Status.fetch_all_statuses(self.request)

        data = json.dumps([{**r} for r in result]) if result else None

        return web.json_response({"data": json.loads(data) if data else None})

    async def post(self):
        post = await self.request.json()
        data = post.get('data')
        if not data:
            return web.json_response({"message": "Error incorrect data"}, status=400)

        result = await query.Status.insert_status(self.request, data)

        return web.json_response({
            "message": "Created!",
            "data": json.dumps(dict(result))
        }, status=201)


@routes.view("/statuses/{entry_id}")
class StatusEntryView(web.View):
    """ Status entry
    """

    async def get(self):
        try:
            result = await query.Status.fetch_status(self.request, self.request.match_info['entry_id'])
        except RecordNotFound as err:
            return web.HTTPNotFound(text=str(err))

        return web.json_response({"data": json.loads(json.dumps(dict(result)))})

    async def put(self):
        entry_id = self.request.match_info['entry_id']
        put = await self.request.json()
        data = put.get('data')

        try:
            result = await query.Status.update_status(self.request, entry_id, data)
        except RecordNotFound as err:
            return web.HTTPNotFound(text=str(err))

        return web.json_response({
            "message": "Update!",
            "data": json.loads(json.dumps(dict(result)))
        }, status=200)


@routes.view("/positions")
class PositionView(web.View):
    """ Positions
    """

    async def get(self):
        result = await query.Position.fetch_all_positions(self.request)

        data = json.dumps([{**r} for r in result]) if result else None

        return web.json_response({"data": json.loads(data) if data else None})

    async def post(self):
        post = await self.request.json()
        data = post.get('data')
        if not data:
            return web.json_response({"message": "Error incorrect data"}, status=400)

        result = await query.Position.insert_position(self.request, data)

        return web.json_response({
            "message": "Created!",
            "data": json.loads(json.dumps({**result}))
        }, status=201)


@routes.view("/positions/{entry_id}")
class PositionEntryView(web.View):
    """ Positions entry
    """

    async def get(self):
        try:
            result = await query.Position.fetch_position(self.request, self.request.match_info['entry_id'])
        except RecordNotFound as err:
            return web.HTTPNotFound(text=str(err))

        return web.json_response({"data": json.loads(json.dumps(dict(result)))})

    async def put(self):
        entry_id = self.request.match_info['entry_id']
        put = await self.request.json()
        data = put.get('data')

        try:
            result = await query.Position.update_position(self.request, entry_id, data)
        except RecordNotFound as err:
            return web.HTTPNotFound(text=str(err))

        return web.json_response({
            "message": "Update!",
            "data": json.loads(json.dumps(dict(result)))
        }, status=200)


@routes.get("/positions/{entry_id}/employers", name="position_employers")
async def position_employers_view(request):
    pos_id = request.match_info['entry_id']

    result = await query.EmployerQuery.fetch_all_employers_by_position(request, pos_id)

    data = json.dumps([{**r} for r in result]) if result else None

    return web.json_response({"data": json.loads(data) if data else None})


@routes.view("/cars")
class CarsView(web.View):
    """ Cars
    """

    async def get(self):
        result = await query.Car.fetch_all_cars(self.request)

        data = json.loads(json.dumps([{**r} for r in result])) if result else None

        return web.json_response({"data": data})

    async def post(self):
        post = await self.request.json()
        data = post.get('data')
        if not data:
            return web.json_response({"message": "Error incorrect data"}, status=400)

        result = await query.Car.insert_car(self.request, data)

        return web.json_response({
            "message": "Created!",
            "data": json.loads(json.dumps({**result}))
        }, status=201)


@routes.view("/cars/{entry_id}")
class CarEntryView(web.View):
    """ Cars entry
    """

    async def get(self):
        try:
            result = await query.Car.fetch_car(self.request, self.request.match_info['entry_id'])
        except RecordNotFound as err:
            return web.HTTPNotFound(text=str(err))

        return web.json_response({"data": json.loads(json.dumps({**result}))})

    async def put(self):
        entry_id = self.request.match_info['entry_id']
        put = await self.request.json()
        data = put.get('data')

        try:
            result = await query.Car.update_car(self.request, entry_id, data)
        except RecordNotFound as err:
            return web.HTTPNotFound(text=str(err))

        return web.json_response({
            "message": "Update!",
            "data": json.loads(json.dumps(dict(result)))
        }, status=200)


@routes.view("/routes")
class RouteView(web.View):
    """ Routes
    """

    async def get(self):
        if self.request.query:
            # machineList=&driverList=&logistList=&mechanicList=&date_departure=&date_arrival=&statusRoute=
            filter_data = {
                'car_id': self.request.query.get("machineList", None),
                'driver_id': self.request.query.get("driverList", None),
                'logist_id': self.request.query.get("logistList", None),
                'mechanic_id': self.request.query.get("mechanicList", None),
                'date_departure': self.request.query.get("date_departure", None),
                'date_arrival': self.request.query.get("date_arrival", None),
                'status_id': self.request.query.get("statusRoute", None),
            }
            result = await query.Route.fetch_with_filter(self.request, filter_data)
        else:
            result = await query.Route.fetch_all_routes(self.request)

        data = [dict(r) for r in result]

        for d in data:
            d["car"] = ''
            d["rate_without_percent"] = d['rate_common'] - (d['rate_common'] * (d['percent_org'] / 100))
            d["date_arrival"] = _default(d["date_arrival"]) if "date_arrival" in d else None
            d["date_departure"] = _default(d["date_departure"]) if "date_departure" in d else None

        return web.json_response({"data": data if data else None})

    async def post(self):
        post = await self.request.json()
        result = await query.Route.insert_route(self.request, post.get('data'))

        return web.json_response({
            "message": "Created!",
            "data": json.loads(
                json.dumps(
                    {**result},
                    default=lambda o: o.isoformat() if isinstance(o, (datetime.date, datetime.datetime)) else None
                ))
        }, status=201)


@routes.view("/routes/{entry_id}")
class RouteEntryView(web.View):
    """ Route entry
    """

    async def get(self):
        try:

            result = await query.Route.fetch_route(self.request, self.request.match_info['entry_id'])

        except RecordNotFound as err:
            return web.HTTPNotFound(text=str(err))

        route = dict(result)
        route['rate_without_percent'] = route['rate_common'] - (route['rate_common'] * (route['percent_org'] / 100))
        route['date_arrival'] = _default(route['date_arrival']) if "date_arrival" in route else None
        route['date_departure'] = _default(route['date_departure']) if "date_departure" in route else None

        return web.json_response({"data": route if route else None})

    async def put(self):
        entry_id = self.request.match_info['entry_id']
        put = await self.request.json()
        data = put.get('data')

        try:
            res = await query.Route.update_route(self.request, entry_id, data)
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

    async def delete(self):
        return web.json_response({"message": "Delete!"})


@routes.get("/filter")
async def filter_route(request):
    return web.json_response({"data": None})
