import asyncio

user_database = [
    {'username': 'mirkol23', 'email': 'mirkol23@gmail.com'},
    {'username': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'username': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'username': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

password_database = [
    {'username': 'mirkol23', 'password': 'password123'},
    {'username': 'ana_anic', 'password': 'super_strong_password'},
    {'username': 'maja_0x', 'password': 's3A2DFFdsj234'},
    {'username': 'zdeslav032', 'password': 'deso123'}
]

async def authorize(user, password):
    await asyncio.sleep(2)
    for record in password_database:
        if record['username'] == user['username']:
            if record['password'] == password:
                return f"User ({user['username']}): Authorization successful."
            return f"User ({user['username']}): Authorization failed."
    return "Error: No password record found."

async def authenticate(username, email, password):
    await asyncio.sleep(3)

    user = None
    for record in user_database:
        if record['username'] == username and record['email'] == email:
            user = record
            break

    if user is None:
        return f"User ({username}) not found."

    return await authorize(user, password)

async def main():
    result = await authenticate("mirkol23", "mirkol23@gmail.com", "password123")
    print(result)

asyncio.run(main())
