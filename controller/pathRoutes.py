"""

Routes here:

- The Shortest path:
    - Return the shortest path between two geo-coordinates

"""

from fastapi import APIRouter
from model.linearDistance import linearDistance
from service.shortestPathService import getShortestPath
pathRouter = APIRouter()


@pathRouter.post("/ShPath")
async def getTheShortestPath(distance: linearDistance):
    shortestPathInMeters = getShortestPath(distance)
    return {"Shortest Path": shortestPathInMeters}
