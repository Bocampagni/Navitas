from fastapi import FastAPI
from controller.locationRoutes import router
from controller.pathRoutes import pathRouter
from controller.shippingRoutes import shippingRoute
app = FastAPI()


@app.get("/healthcheck")
async def root():
    return {"message": "ok"}


app.include_router(router)
app.include_router(pathRouter)
app.include_router(shippingRoute)