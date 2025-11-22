import asyncio

async def fetch_users():
    await asyncio.sleep(3)
    return [{"name": "Mark"}, {"name": "Anna"}, {"name": "Peter"}]

async def fetch_products():
    await asyncio.sleep(5)
    return [{"product": "Laptop"}, {"product": "Mouse"}]

async def main():
    users, products = await asyncio.gather(
        fetch_users(),
        fetch_products()
    )
    print("Users:", users)
    print("Products:", products)

asyncio.run(main())
