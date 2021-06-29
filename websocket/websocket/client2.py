
import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    while True:
        try:
            async with websockets.connect(uri) as websocket:
                name = input("What's your name? ")

                # await websocket.send(name)
                # print(f"> {name}")

                greeting = await websocket.recv()
                print(f"< {greeting}")
        except:
            break

asyncio.get_event_loop().run_until_complete(hello())
