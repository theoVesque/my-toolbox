from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from ...service.mathematics.mathematics import MathematicsTools
from ...model.requestModel.mathematicsRequest import PercentRequest, SumRequest, AverageRequest, MedianRequest, StandardDeviationRequest, MaximumInListRequest, MinimumInListRequest, PowerRequest, FactorialRequest, ExponentialRequest

app = FastAPI()


class MathematicsController:
    mathematics_router = APIRouter(prefix="/api/mathematics")
    
    @mathematics_router.post("/percent")
    async def calculate_percent(request: PercentRequest):
        """
        Calculate the percentage of a given value.
        
        :param request: PercentRequest containing value and percent.
        :return: Calculated percentage.
        """
        calculate_percent = MathematicsTools.calc_percent(request.value, request.percent)
        return {"calculate_percent": calculate_percent}

    @mathematics_router.post("/sum")
    async def calculate_sum(request: SumRequest):
        """
        Calculate the sum of a list of numbers.
        
        :param request: SumRequest containing a list of numbers.
        :return: The sum of the numbers.
        """
        calculate_sum = MathematicsTools.calc_sum(request.value)
        return {"calculate_sum": calculate_sum}

    @mathematics_router.post("/average")
    async def calculate_average(request: AverageRequest):
        """
        Calculate the average of a list of numbers.
        
        :param request: AverageRequest containing a list of numbers.
        :return: The average of the numbers.
        """
        calculate_average = MathematicsTools.average(request.value)
        return {"calculate_average": calculate_average}

    @mathematics_router.post("/median")
    async def calculate_median(request: MedianRequest):
        """
        Calculate the median of a list of numbers.
        
        :param request: MedianRequest containing a list of numbers.
        :return: The median of the numbers.
        """
        calculate_median = MathematicsTools.median(request.value)
        return {"calculate_median": calculate_median}

    @mathematics_router.post("/standard_deviation")
    async def calculate_standard_deviation(request: StandardDeviationRequest):
        """
        Calculate the standard deviation of a list of numbers.
        
        :param request: StandardDeviationRequest containing a list of numbers.
        :return: The standard deviation of the numbers.
        """
        calculate_standard_deviation = MathematicsTools.standard_deviation(request.value)
        return {"calculate_standard_deviation": calculate_standard_deviation}

    @mathematics_router.post("/maximum")
    async def calculate_maximum(request: MaximumInListRequest):
        """
        Find the maximum value in a list of numbers.
        
        :param request: MaximumInListRequest containing a list of numbers.
        :return: The maximum value.
        """
        calculate_maximum = MathematicsTools.maximum(request.value)
        return {"calculate_maximum": calculate_maximum}

    @mathematics_router.post("/minimum")
    async def calculate_minimum(request: MinimumInListRequest):
        """
        Find the minimum value in a list of numbers.
        
        :param request: MinimumInListRequest containing a list of numbers.
        :return: The minimum value.
        """
        calculate_minimum = MathematicsTools.minimum(request.value)
        return {"calculate_minimum": calculate_minimum}

    @mathematics_router.post("/power")
    async def calculate_power(request: PowerRequest):
        """
        Calculate the power of a base number raised to an exponent.
        
        :param request: PowerRequest containing base and exponent.
        :return: The result of the base raised to the exponent.
        """
        calculate_power = MathematicsTools.power(request.base, request.power)
        return {"calculate_power": calculate_power}

    @mathematics_router.post("/factorial")
    async def calculate_factorial(request: FactorialRequest):
        """
        Calculate the factorial of a number.
        
        :param request: FactorialRequest containing a number.
        :return: The factorial of the number.
        """
        calculate_factorial = MathematicsTools.factorial(request.n)
        return {"calculate_factorial": calculate_factorial}

    @mathematics_router.post("/exponential")
    async def calculate_exponential(request: ExponentialRequest):
        """
        Calculate the exponential of a number.
        
        :param request: ExponentialRequest containing a number.
        :return: The exponential of the number.
        """
        calculate_exponential = MathematicsTools.exponential(request.x)
        return {"calculate_exponential": calculate_exponential}
        
   