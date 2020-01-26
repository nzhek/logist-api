from aiohttp import web


async def handle_404(request):
    return web.json_response({"error": "404 page not found"}, status=404)


async def handler_500(request):
    return web.json_response({"error": "500 server fault"}, status=500)


def create_error_middleware(overrides):
    @web.middleware
    async def error_middleware(request, handler):
        try:
            response = await handler(request)

            override = overrides.get(response.status)
            if override:
                return await override(request)

            return response

        except web.HTTPException as ex:
            override = overrides.get(ex.status)
            if override:
                return await override(request)

            raise

    return error_middleware


def setup_middlewares(app):
    error_middlewares = create_error_middleware({
        404: handle_404,
        500: handler_500
    })

    app.middlewares.append(error_middlewares)
