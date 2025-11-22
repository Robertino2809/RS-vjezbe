import asyncio
import time

async def fetch_data(param):
    print(f"Working with param {param}...")
    await asyncio.sleep(2)
    print(f"Finished param {param}.")
    return f"Result for {param}"

async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))

    result1 = await task1
    print("Task 1 is done.")

    return [result1]

t1 = time.perf_counter()
result = asyncio.run(main())
t2 = time.perf_counter()

print("Result:", result)
print(f"Execution time: {t2 - t1:.2f} seconds")
