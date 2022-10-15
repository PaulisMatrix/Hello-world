from aiohttp import web
import asyncio

async def handle(request):
    name = request.match_info.get('client_id', 'anon_id')
    text = "Hello, " + name
    data = {"client_data":text}
    # simulate work
    await asyncio.sleep(2)

    # return data
    return web.json_response(data,status=200,content_type='application/json')

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{client_id}', handle)])

if __name__ == '__main__':
    web.run_app(app)