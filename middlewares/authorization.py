from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

valid_access_keys = ["key1", "key2"]  # TODO: replace with on-startup keys


async def authorization_middleware(request: Request, call_next):
    access_key = request.headers.get("X-ACCESS-KEY")

    if access_key not in valid_access_keys:
        return JSONResponse(status_code=401, content={"detail": "Unauthorized"})
        # raise HTTPException(status_code=401, detail="Unauthorized")

    response = await call_next(request)
    return response
