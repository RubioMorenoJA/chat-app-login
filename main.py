from fastapi import FastApi


app = FastApi()


@app.get('/')
async def root():
    return {'message': 'FastApi project: ChatApp'}

