from fastapi import FastAPI
from src.controller.locationRoutes import router
from src.controller.pathRoutes import pathRouter
from src.controller.shippingRoutes import shippingRoute
app = FastAPI()


@app.get("/healthcheck")
async def root():
    return {"message": "ok"}


app.include_router(router)
app.include_router(pathRouter)
app.include_router(shippingRoute)