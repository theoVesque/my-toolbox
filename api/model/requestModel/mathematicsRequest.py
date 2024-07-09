from pydantic import BaseModel
from typing import Union, List

class PercentRequest(BaseModel):
    value: Union[float, int]
    percent: Union[float, int]
    
class SumRequest(BaseModel):
    value: List[Union[float, int]]
    
class AverageRequest(BaseModel):
    value: List[Union[float, int]]

class MedianRequest(BaseModel):
    value: List[Union[float, int]]
    
class StandardDeviationRequest(BaseModel):
    value: List[Union[float, int]]

class MaximumInListRequest(BaseModel):
    value: List[Union[float, int]]
    
class MinimumInListRequest(BaseModel):
    value: List[Union[float, int]]
    
class PowerRequest(BaseModel):
    base: Union[float, int]
    power: int
    
class FactorialRequest(BaseModel):
    n: Union[float, int]
    
class ExponentialRequest(BaseModel):
    x: Union[float, int]
