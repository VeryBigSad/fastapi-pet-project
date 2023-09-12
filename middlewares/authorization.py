from fastapi import Request
from fastapi.responses import JSONResponse
from config import ACCESS_KEY


async def authorization_middleware(request: Request, call_next):
    access_key = request.headers.get("X-ACCESS-KEY")

    if access_key != ACCESS_KEY:
        return JSONResponse(status_code=401, content={"detail": "Unauthorized"})

    response = await call_next(request)
    return response
