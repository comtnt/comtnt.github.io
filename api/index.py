from sanic import Sanic
from sanic.response import json

app = Sanic("api")

@app.get('/')
async def test(request):
    return json({'hello': 'world'})