from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost.com",
    "https://localhost.com",
    "http://localhost",
    "http://localhost:80",
    "http://localhost:8080"
]

middleware_configuration = {
    'allow_origins': origins,
    'allow_credentials': True,
    'allow_methods': ["*"],
    'allow_headers': ["*"]
}
