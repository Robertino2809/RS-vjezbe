import asyncio

async def fetch_data():
    await asyncio.sleep(3)
    numbers = [i for i in range(1, 11)]
    print("Data fetched.")
    return numbers

async def main():
    result = await asyncio.gather(fetch_data())
    print("Result:", result)

asyncio.run(main())
