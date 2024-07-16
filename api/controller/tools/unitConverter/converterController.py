from fastapi import FastAPI, APIRouter
from ....service.unitConverter.converter import LengthConverter, TimeConverter, MassConverter, SpeedConverter
from ....model.requestModel.unitConverterRequest import LengthConversionRequest, TimeConverterRequest, MassConverterRequest, SpeedConverterRequest

app = FastAPI()


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
    
    @converter_router.post("/time")
    async def convert_time(request: TimeConverterRequest):
        """
        Convert time from one unit to another.
        
        :param request: TimeConverterRequest containing value, from_unit, and to_unit.
        :return: Converted value.
        """
        converted_value = TimeConverter.convert(
            request.value, request.from_unit, request.to_unit)
        return {"converted_value": converted_value}

    @converter_router.post("/mass")
    async def convert_time(request: MassConverterRequest):
        """
        Convert mass from one unit to another.
        
        :param request: MassConverterRequest containing value, from_unit, and to_unit.
        :return: Converted value.
        """
        converted_value = MassConverter.convert(
            request.value, request.from_unit, request.to_unit)
        return {"converted_value": converted_value}
    
    @converter_router.post("/speed")
    async def convert_time(request: SpeedConverterRequest):
        """
        Convert speed from one unit to another.
        
        :param request: SpeedConverterRequest containing value, from_unit, and to_unit.
        :return: Converted value.
        """
        converted_value = SpeedConverter.convert(
            request.value, request.from_unit, request.to_unit)
        return {"converted_value": converted_value}