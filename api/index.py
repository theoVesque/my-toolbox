from fastapi import FastAPI
from .controller.test import TestController

app = FastAPI()

app.include_router(TestController.testRouter)
