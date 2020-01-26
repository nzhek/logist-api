import aiopg.sa


async def init_pg(app):
    conf = app["config"]["postgres"]
    engine = await aiopg.sa.create_engine(**conf)
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()
