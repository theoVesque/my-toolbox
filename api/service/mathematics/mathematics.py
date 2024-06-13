import math

class MathematicsTools:
    
    @staticmethod
    def calc_percent(value, percent):
        return (value * percent) / 100
    
    @staticmethod
    def calc_sum(value):
        s = 0
        for i in value:
            s += i
        return s
    
    @staticmethod
    def average(value):
        s = 0
        for i in value:
            s += i
        s = s / len(value)
        return s
    
    @staticmethod
    def median(value):
        sorted_value = sorted(value)
        n = len(sorted_value)
        if n % 2 == 0:
            return (sorted_value[n//2 - 1] + sorted_value[n//2]) / 2
        else:
            return sorted_value[n//2]
    
    @staticmethod
    def variance(value):
        mean = MathematicsTools.average(value)
        return sum((x - mean) ** 2 for x in value) / len(value)
    
    @staticmethod
    def standard_deviation(value):
        return math.sqrt(MathematicsTools.variance(value))
    
    @staticmethod
    def maximum(value):
        return max(value)
    
    @staticmethod
    def minimum(value):
        return min(value)
    
    @staticmethod
    def power(base, exponent):
        return base ** exponent
    
    @staticmethod
    def factorial(n):
        return math.factorial(n)
    
    @staticmethod
    def exponential(x):
        return math.exp(x)

values = [50, 25, 75, 100, 125]

print("Moyenne:", MathematicsTools.average(values))
print("Médiane:", MathematicsTools.median(values))
print("Variance:", MathematicsTools.variance(values))
print("Écart type:", MathematicsTools.standard_deviation(values))
print("Maximum:", MathematicsTools.maximum(values))
print("Minimum:", MathematicsTools.minimum(values))
print("Puissance:", MathematicsTools.power(2, 3))
print("Factoriel:", MathematicsTools.factorial(5))
print("Exponentielle:", MathematicsTools.exponential(2))
