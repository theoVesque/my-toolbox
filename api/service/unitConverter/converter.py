import math
import random 

class LengthConverter:
    conversion_factors = {
        'm': 1,           # base unit 
        'km': 1000,       # 1 km = 1000 m
        'cm': 0.01,       # 1 cm = 0.01 m
        'mm': 0.001,      # 1 mm = 0.001 m
        'mile': 1609.34,  # 1 mile = 1609.34 m
        'yard': 0.9144,   # 1 yard = 0.9144 m
        'foot': 0.3048,   # 1 foot = 0.3048 m
        'inch': 0.0254    # 1 inch = 0.0254 m
    }
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        """
        Convert a length from one unit to another.

        :param value: The length value to convert.
        :param from_unit: The unit to convert from.
        :param to_unit: The unit to convert to.
        :return: The converted length value.
        :raises ValueError: If the from_unit or to_unit is not recognized.
        """
        if from_unit not in LengthConverter.conversion_factors:
            raise ValueError(f"Unknown from unit: {from_unit}")
        if to_unit not in LengthConverter.conversion_factors:
            raise ValueError(f"Unknown destination unit: {to_unit}")
    
        # Convert to meters
        value_in_meters = value * LengthConverter.conversion_factors[from_unit]
        
        # Convert to destination unit
        converted_value = value_in_meters / LengthConverter.conversion_factors[to_unit]
        return converted_value

    
class TimeConverter:
    conversion_factors_time = {
        'second': 1,          # second is the reference unit
        'minute': 60,         # 1 minute = 60 seconds
        'hour': 3600,         # 1 hour = 3600 seconds
        'day': 86400,         # 1 day = 86400 seconds
        'week': 604800,       # 1 week = 604800 seconds
        'month': 2628000,     # approximation: 1 month = 2628000 seconds (30.42 days)
        'year': 31536000      # approximation: 1 year = 31536000 seconds (365 days)
    }
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        """
        Convert a time duration from one unit to another.

        :param value: The time value to convert.
        :param from_unit: The unit to convert from.
        :param to_unit: The unit to convert to.
        :return: The converted time value.
        :raises ValueError: If the from_unit or to_unit is not recognized.
        """
        if from_unit not in TimeConverter.conversion_factors_time:
            raise ValueError(f"Unknown from unit: {from_unit}")
        if to_unit not in TimeConverter.conversion_factors_time:
            raise ValueError(f"Unknown destination unit: {to_unit}")
        
        # Convert to seconds
        value_in_seconds = value * TimeConverter.conversion_factors_time[from_unit]

        # Convert to destination unit
        converted_value = value_in_seconds / TimeConverter.conversion_factors_time[to_unit]
        return converted_value

class MassConverter:
    conversion_factors_mass = {
        'gram': 1,           # gram is the reference unit
        'kilogram': 1000,    # 1 kilogram = 1000 grams
        'milligram': 0.001,  # 1 milligram = 0.001 grams
        'tonne': 1000000,    # 1 tonne = 1000000 grams
        'ounce': 28.3495,    # 1 ounce = 28.3495 grams
        'pound': 453.592     # 1 pound = 453.592 grams
    }
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        """
        Convert a mass from one unit to another.

        :param value: The mass value to convert.
        :param from_unit: The unit to convert from.
        :param to_unit: The unit to convert to.
        :return: The converted mass value.
        :raises ValueError: If the from_unit or to_unit is not recognized.
        """
        if from_unit not in MassConverter.conversion_factors_mass:
            raise ValueError(f"Unknown from unit: {from_unit}")
        if to_unit not in MassConverter.conversion_factors_mass:
            raise ValueError(f"Unknown destination unit: {to_unit}")
        
        # Convert to grams
        value_in_grams = value * MassConverter.conversion_factors_mass[from_unit]

        # Convert to destination unit
        converted_value = value_in_grams / MassConverter.conversion_factors_mass[to_unit]
        return converted_value
    

class SpeedConverter:
    conversion_factors_speed = {
        'm/s': 1,          # meter per second is the reference unit
        'km/h': 0.277778,  # 1 kilometer per hour = 0.277778 meters per second
        'mph': 0.44704,    # 1 mile per hour = 0.44704 meters per second
        'knot': 0.514444   # 1 knot = 0.514444 meters per second
    }
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        """
        Convert a speed from one unit to another.

        :param value: The speed value to convert.
        :param from_unit: The unit to convert from.
        :param to_unit: The unit to convert to.
        :return: The converted speed value.
        :raises ValueError: If the from_unit or to_unit is not recognized.
        """
        if from_unit not in SpeedConverter.conversion_factors_speed:
            raise ValueError(f"Unknown from unit: {from_unit}")
        if to_unit not in SpeedConverter.conversion_factors_speed:
            raise ValueError(f"Unknown destination unit: {to_unit}")
        
        # Convert to meters per second
        value_in_meters_per_second = value * SpeedConverter.conversion_factors_speed[from_unit]

        # Convert to destination unit
        converted_value = value_in_meters_per_second / SpeedConverter.conversion_factors_speed[to_unit]
        return converted_value


