import asyncio


async def tcp_client():
    reader, writer = await asyncio.open_connection("127.0.0.1", 9000)
    print("Connected to Server!!")

    # Task 1: Listen to Server messages
    async def listen():
        while True:
            data = await reader.read(100)
            if not data:
                print("Server Closed Connection")
                break
            print(f"[SERVER]: {data.decode().strip()}")

    # Task 2: Send Messages typed by user
    async def send():
        while True:
            msg = input("> ")
            writer.write(msg.encode() + b"\n")
            await writer.drain()

    # Run both tasks at same time
    await asyncio.gather(listen(), send())


asyncio.run(tcp_client())
