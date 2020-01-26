from aiohttp import web
from logist_api.db import init_pg, close_pg
from logist_api.settings import config
from logist_api.middlewares import setup_middlewares

import aiohttp_debugtoolbar
from aiohttp_debugtoolbar import toolbar_middleware_factory

if __name__ == '__main__':

    app = web.Application()
    app['config'] = config

    if app['config']['app']['debug']:
        app.middlewares.append(toolbar_middleware_factory)
        aiohttp_debugtoolbar.setup(app)

    from logist_api.views import routes

    app.router.add_routes([*routes])

    setup_middlewares(app)

    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)

    web.run_app(app, host=app['config']['app']['host'], port=app['config']['app']['port'])
