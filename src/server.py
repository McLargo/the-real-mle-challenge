from fastapi import FastAPI
from fastapi.responses import JSONResponse

api = FastAPI()

@api.get("/health", tags=["Health"])
async def healthcheck():
    return JSONResponse(content={"status": "ok"})
