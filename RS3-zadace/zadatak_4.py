import asyncio
import random

async def check_parity(number):
    await asyncio.sleep(2)
    if number % 2 == 0:
        return f"Number {number} is even."
    return f"Number {number} is odd."

async def main():
    numbers = [random.randint(1, 100) for _ in range(10)]
    tasks = [asyncio.create_task(check_parity(n)) for n in numbers]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
