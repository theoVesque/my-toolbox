from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .controller.tools.unitConverter.converterController import ConverterController
from .controller.tools.mathematics.mathematicsController import MathematicsController 
from .controller.tools.qrCodeGenerator import qr_code_router

app = FastAPI()

# Configuration des origines autorisées
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://my-toolbox.vercel.app",
    "http://my-toolbox.vercel.app",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ConverterController.converter_router)
app.include_router(MathematicsController.mathematics_router)
app.include_router(qr_code_router)

# Pour vérifier les routes enregistrées
@app.get("/routes")
async def get_routes():
    return [{"path": route.path, "name": route.name} for route in app.routes]
