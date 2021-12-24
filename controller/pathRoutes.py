"""

Routes here:

- The Shortest path:
    - Return the shortest path between two geo-coordinates

"""

from fastapi import APIRouter
from model.linearDistance import linearDistance

pathRouter = APIRouter()


@pathRouter.post("/ShPath")
async def getTheShortestPath(distance: linearDistance):
    return {"Message": "Graph here"}
