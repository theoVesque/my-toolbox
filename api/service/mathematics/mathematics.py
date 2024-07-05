import math
import random 

class MathematicsTools:
    @staticmethod
    def calc_percent(value, percent):
        """
        Calculate the percentage of a given value.

        :param value: The base value.
        :param percent: The percentage to calculate.
        :return: The calculated percentage of the value.
        """
        return (value * percent) / 100
    
    @staticmethod
    def calc_sum(value):
        """
        Calculate the sum of a list of numbers.

        :param value: A list of numbers.
        :return: The sum of the numbers.
        """
        s = 0
        for i in value:
            s += i
        return s
    
    @staticmethod
    def average(value):
        """
        Calculate the average of a list of numbers.

        :param value: A list of numbers.
        :return: The average of the numbers.
        """
        s = 0
        for i in value:
            s += i
        s = s / len(value)
        return s
    
    @staticmethod
    def median(value):
        """
        Calculate the median of a list of numbers.

        :param value: A list of numbers.
        :return: The median of the numbers.
        """
        sorted_value = sorted(value)
        n = len(sorted_value)
        if n % 2 == 0:
            return (sorted_value[n // 2 - 1] + sorted_value[n // 2]) / 2
        else:
            return sorted_value[n // 2]
    
    @staticmethod
    def variance(value):
        """
        Calculate the variance of a list of numbers.

        :param value: A list of numbers.
        :return: The variance of the numbers.
        """
        mean = MathematicsTools.average(value)
        return sum((x - mean) ** 2 for x in value) / len(value)
    
    @staticmethod
    def standard_deviation(value):
        """
        Calculate the standard deviation of a list of numbers.

        :param value: A list of numbers.
        :return: The standard deviation of the numbers.
        """
        return math.sqrt(MathematicsTools.variance(value))
    
    @staticmethod
    def maximum(value):
        """
        Find the maximum value in a list of numbers.

        :param value: A list of numbers.
        :return: The maximum number.
        """
        return max(value)
    
    @staticmethod
    def minimum(value):
        """
        Find the minimum value in a list of numbers.

        :param value: A list of numbers.
        :return: The minimum number.
        """
        return min(value)
    
    @staticmethod
    def power(base, exponent):
        """
        Calculate the power of a base number raised to an exponent.

        :param base: The base number.
        :param exponent: The exponent to raise the base to.
        :return: The result of the base raised to the exponent.
        """
        return base ** exponent
    
    @staticmethod
    def factorial(n):
        """
        Calculate the factorial of a number.

        :param n: The number to calculate the factorial of.
        :return: The factorial of the number.
        """
        return math.factorial(n)
    
    @staticmethod
    def exponential(x):
        """
        Calculate the exponential of a number.

        :param x: The number to calculate the exponential of.
        :return: The exponential of the number.
        """
        return math.exp(x)

    @staticmethod
    def calc_quiz_level1():
        """
        Generate a basic arithmetic quiz with addition or subtraction.

        :return: A dictionary containing the two numbers, the operator, and the result.
        """
        operator_list = ['+', '-']
        random_operator = random.choice(operator_list)

        number1 = random.randint(0, 100)
        number2 = random.randint(0, 100)

        result = number1 + number2 if random_operator == '+' else number1 - number2

        return {
            'number1': number1,
            'number2': number2,
            'operator': random_operator,
            'result': result
        }

    @staticmethod
    def calc_quiz_level2():
        """
        Generate an arithmetic quiz with addition or subtraction using floating-point numbers.

        :return: A dictionary containing the two numbers, the operator, and the result.
        """
        operator_list = ['+', '-']
        random_operator = random.choice(operator_list)

        number1 = round(random.uniform(0, 100), 2)
        number2 = round(random.uniform(0, 100), 2)

        result = round(number1 + number2, 2) if random_operator == '+' else round(number1 - number2, 2)

        return {
            'number1': number1,
            'number2': number2,
            'operator': random_operator,
            'result': result
        }
        
    @staticmethod
    def calc_quiz_level3():
        """
        Generate an arithmetic quiz with addition, subtraction, multiplication, or division.

        :return: A dictionary containing the two numbers, the operator, and the result.
        """
        operator_list = ['+', '-', '*', '/']
        random_operator = random.choice(operator_list)

        number1 = random.randint(0, 100)
        number2 = random.randint(0, 100)

        if random_operator == '+':
            result = number1 + number2
        elif random_operator == '-':
            result = number1 - number2
        elif random_operator == '*':
            result = number1 * number2
        elif random_operator == '/':
            if number2 == 0:
                result = "Undefined (division by zero)"
            else:
                result = number1 // number2

        return {
            'number1': number1,
            'number2': number2,
            'operator': random_operator,
            'result': result
        }

