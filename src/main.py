from fastapi import FastAPI
from src.controller.locationRoutes import router
from src.controller.pathRoutes import pathRouter
from src.controller.shippingRoutes import shippingRoute
from src.utils.fuelPriceSyncer import getFuelPrice

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    try:
        getFuelPrice()
    except Exception:
        print("Could not get fuel prices")


@app.get("/healthcheck")
async def root():
    return {"message": "ok"}


app.include_router(router)
app.include_router(pathRouter)
app.include_router(shippingRoute)
