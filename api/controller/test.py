from fastapi import APIRouter

class TestController:

    testRouter  = APIRouter()

    @testRouter.get("/api/python")
    def hello_world():
        return {"message": "Hello World"}