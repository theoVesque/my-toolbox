from pydantic import BaseModel

class LengthConversionRequest(BaseModel):
    value: float
    from_unit: str
    to_unit: str 
    
class TimeConverterRequest(BaseModel):
    value: float
    from_unit: str
    to_unit: str 

class MassConverterRequest(BaseModel): 
    value: float
    from_unit: str
    to_unit: str  
    
class SpeedConverterRequest(BaseModel):
    value: float
    from_unit: str
    to_unit: str 
