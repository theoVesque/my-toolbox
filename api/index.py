from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .controller.tools.unitConverter.converterController import ConverterController
from .controller.tools.mathematics.mathematicsController import MathematicsController 
from .controller.tools.qrCodeGenerator import QrCodeController

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
    allow_origins=origins,  # Autoriser ces origines
    allow_credentials=True,
    allow_methods=["*"],  # Autoriser toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],  # Autoriser tous les headers
)

app.include_router(ConverterController.converter_router)
app.include_router(MathematicsController.mathematics_router)
app.include_router(QrCodeController.qr_code_router) 