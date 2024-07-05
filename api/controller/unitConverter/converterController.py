from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from ...service.unitConverter.converter import LengthConverter

app = FastAPI()

class LengthConversionRequest(BaseModel):
    value: float
    from_unit: str
    to_unit: str

class ConverterController:
    converter_router = APIRouter(prefix="/api/converter")
    
    @converter_router.post("/length")
    async def convert_length(request: LengthConversionRequest):
        """
        Convert length from one unit to another.
        
        :param request: LengthConversionRequest containing value, from_unit, and to_unit.
        :return: Converted value.
        """
        converted_value = LengthConverter.convert(
            request.value, request.from_unit, request.to_unit)
        return {"converted_value": converted_value}

