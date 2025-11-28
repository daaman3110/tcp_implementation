import asyncio


async def handle_client(reader, writer):
    print("Client Connected")

    # Waiting for message from Client
    data = await reader.read(100)
    print("Client Said:", data.decode())

    # Sending Reply
    writer.write(b"Hello from server!\n")
    await writer.drain()

    # Closing Connection
    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_client, "0.0.0.0", 9000)

    print("Server is running on port 9000")

    async with server:
        await server.serve_forever()


asyncio.run(main())
