from fastapi import FastAPI
from routers.cors import CORSMiddleware, middleware_configuration
from routers.login import user

# Create application
app = FastAPI()
# Configure application
app.include_router(user.router)
app.add_middleware(CORSMiddleware, **middleware_configuration)


@app.get('/')
async def root():
    return {'message': 'FastApi project: ChatApp'}
