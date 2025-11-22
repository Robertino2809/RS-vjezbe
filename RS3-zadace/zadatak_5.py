import asyncio
import hashlib

async def secure_data(data):
    await asyncio.sleep(3)
    return {
        'lastname': data['lastname'],
        'card_number': data['card_number'],
        'CVV': hashlib.sha256(data['CVV'].encode()).hexdigest()
    }

async def main():
    dataset = [
        {'lastname': 'Smith', 'card_number': '1111-2222-3333-4444', 'CVV': '123'},
        {'lastname': 'Brown', 'card_number': '5555-6666-7777-8888', 'CVV': '555'},
        {'lastname': 'Jones', 'card_number': '9999-0000-1111-2222', 'CVV': '777'}
    ]

    tasks = [asyncio.create_task(secure_data(entry)) for entry in dataset]
    results = await asyncio.gather(*tasks)

    print(results)

asyncio.run(main())
