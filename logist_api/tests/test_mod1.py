import pytest
from aiohttp import web


def cli():
    app = web.Application()
    client = await aiohttp_client(app)
    resp = await client.get('/')
    assert resp.status == 200
