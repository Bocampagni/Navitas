from fastapi import FastAPI
from controller.locationRoutes import router
app = FastAPI()


@app.get("/healthcheck")
async def root():
    return {"message": "ok"}

app.include_router(router)