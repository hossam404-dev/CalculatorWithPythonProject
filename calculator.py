import math
from statistics import mean, median, mode
from sympy import Eq, symbols, integrate, sympify, solve
    
class BasicCalculator:
    def __init__(self):
        self.__last_result = 0


    def add(self, a, b):
        self.__last_result = a + b
        return self.__last_result

    def subtract(self, a, b):
        self.__last_result = a - b
        return self.__last_result

    def multiply(self, a, b):
        self.__last_result = a * b
        return self.__last_result

    def divide(self, a, b):
      if b == 0:
        return "Error: Cannot divide by zero"
      self.__last_result = a / b
      return self.__last_result


    def modulus(self, a, b):
        self.__last_result = a % b
        return self.__last_result

    def power(self, a, b):
        self.__last_result = a ** b
        return self.__last_result

    def sqrt(self, a):
      if a < 0:
        return "Error: Cannot take square root of a negative number"
      self.__last_result = math.sqrt(a)
      return self.__last_result


    def get_last_result(self):
        return self.__last_result


class ScientificCalculator:
    def __init__(self):
        self.__last_result = 0

    def sin(self, x, degrees=True):
        x = math.radians(x) if degrees else x
        self.__last_result = math.sin(x)
        return self.__last_result

    def cos(self, x, degrees=True):
        x = math.radians(x) if degrees else x
        self.__last_result = math.cos(x)
        return self.__last_result

    def tan(self, x, degrees=True):
        x = math.radians(x) if degrees else x
        self.__last_result = math.tan(x)
        return self.__last_result

    def asin(self, x, degrees=True):
        self.__last_result = math.asin(x)
        return math.degrees(self.__last_result) if degrees else self.__last_result

    def acos(self, x, degrees=True):
        self.__last_result = math.acos(x)
        return math.degrees(self.__last_result) if degrees else self.__last_result

    def atan(self, x, degrees=True):
        self.__last_result = math.atan(x)
        return math.degrees(self.__last_result) if degrees else self.__last_result

    def sec(self, x, degrees=True):
      x = math.radians(x) if degrees else x
      cos_value = math.cos(x)
      if cos_value == 0:
        return "Error: sec is undefined for this input"
      self.__last_result = 1 / cos_value
      return self.__last_result

    def csc(self, x, degrees=True):
      x = math.radians(x) if degrees else x
      sin_value = math.sin(x)
      if sin_value == 0:
        return "Error: csc is undefined for this input"
      self.__last_result = 1 / sin_value
      return self.__last_result

    def cot(self, x, degrees=True):
      x = math.radians(x) if degrees else x
      tan_value = math.tan(x)
      if tan_value == 0:
        return "Error: cot is undefined for this input"
      self.__last_result = 1 / tan_value
      return self.__last_result

    def log(self, x):
      if x <= 0:
        return "Error: Logarithm is only defined for positive numbers"
      self.__last_result = math.log10(x)
      return self.__last_result


    def ln(self, x):
      if x <= 0:
        return "Error: Natural logarithm is only defined for positive numbers"
      self.__last_result = math.log(x)
      return self.__last_result


    def exp(self, x):
        self.__last_result = math.exp(x)
        return self.__last_result

    def ten_power(self, x):
        self.__last_result = 10 ** x
        return self.__last_result

    def factorial(self, x):
      if type(x) != int or x < 0:
        return "Error: Factorial is only defined for non-negative integers"
      self.__last_result = math.factorial(x)
      return self.__last_result


    def inverse(self, x):
      if x == 0:
        return "Error: Cannot divide by zero"
      self.__last_result = 1 / x
      return self.__last_result


    def absolute(self, x):
        self.__last_result = abs(x)
        return self.__last_result


    def round_value(self, x, digits=0):
        self.__last_result = round(x, digits)
        return self.__last_result


    def get_last_result(self):
        return self.__last_result

      
    def integrate_expression(self, expr_str, variable='x', lower=None, upper=None):
      if not expr_str.strip():
        return "Error: Expression cannot be empty"

      if not variable.isalpha():
        return "Error: Variable must be a valid letter"

      x = symbols(variable)

      invalid_chars = "!@#$&[]{};:?<>\\|"

      for char in expr_str:
        if char in invalid_chars:
          return "Error: Expression contains invalid characters"

      expr = sympify(expr_str)

      if lower is not None and upper is not None:
        result = integrate(expr, (x, lower, upper))
      else:
        result = integrate(expr, x)

      self.__last_result = result
      return result

class GeometryCalculator:
    def area_circle(self, radius):
        if radius < 0:
            return "Error: Radius cannot be negative"
        return math.pi * radius * radius

    def area_rectangle(self, length, width):
        if length < 0 or width < 0:
            return "Error: Length and width must be non-negative"
        return length * width

    def area_triangle(self, base, height):
        if base < 0 or height < 0:
            return "Error: Base and height must be non-negative"
        return 0.5 * base * height

    def area_square(self, side):
        if side < 0:
            return "Error: Side cannot be negative"
        return side * side


class Memory:
    def __init__(self):
        self.__memory = 0

    def memory_add(self, value):
        self.__memory += value

    def memory_subtract(self, value):
        self.__memory -= value

    def memory_recall(self):
        return self.__memory

    def memory_clear(self):
        self.__memory = 0

class Converter:
    def __init__(self):
        pass

    def deg_to_rad(self, deg):
        return math.radians(deg)

    def rad_to_deg(self, rad):
        return math.degrees(rad)

    def deg_to_grad(self, deg):
        return deg * (10 / 9)

    def grad_to_deg(self, grad):
        return grad * (9 / 10)

    def dms_to_decimal(self, degrees, minutes, seconds):
        return degrees + (minutes / 60.0) + (seconds / 3600.0)

    def decimal_to_dms(self, decimal_degrees):
        degrees = int(decimal_degrees)
        minutes_float = (decimal_degrees - degrees) * 60
        minutes = int(minutes_float)
        seconds = (minutes_float - minutes) * 60
        return degrees, minutes, seconds


class History:
    def __init__(self):
        self.__history = []

    def add_record(self, expression, result):
        self.__history.append(f"{expression} = {result}")

    def get_history(self):
        return self.__history[-10:]

    def clear_history(self):
        self.__history = []


class StatisticsCalculator:
    def __init__(self):
        self.__data = []

    def load_data(self, data_list):
        if type(data_list) != list:
          print("Error: Input must be a list of numbers.")
          return False

        for item in data_list:
          if type(item) not in [int, float]:
            print("Error: All elements in the list must be numbers.")
            return False

        self.__data = data_list
        return True

    def __sort(self, data):
      cpy = data[:]
      for i in range(1, len(cpy)):
        key = cpy[i]
        j = i - 1
        while j >= 0 and cpy[j] > key:
            cpy[j + 1] = cpy[j]
            j -= 1
        cpy[j + 1] = key
      return cpy


    def mean(self):
        return sum(self.__data) / len(self.__data)

    def median(self):
        data = self.__sort(self.__data)
        n = len(data)
        mid = n // 2

        if n % 2 == 0:
            return (data[mid - 1] + data[mid]) / 2
        else:
            return data[mid]

    def mode(self):
      frequency = {}

      for item in self.__data:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

      max_count = 0
      for key in frequency:
        if frequency[key] > max_count:
            max_count = frequency[key]

      modes = []
      for key in frequency:
        if frequency[key] == max_count:
            modes.append(key)

      if len(modes) == 1:
        return modes[0]
      else:
        return "No unique mode"

class CalculatorEngine:
    def __init__(self):
        self.basic = BasicCalculator()
        self.sci = ScientificCalculator()
        self.mem = Memory()
        self.hist = History()
        self.conv = Converter()
        self.stats = StatisticsCalculator()
        self.geom = GeometryCalculator()

    def integrate(self, expr, var='x', lower=None, upper=None):
        return self.sci.integrate_expression(expr, var, lower, upper)

    def evaluate_expression(self, expression: str):
        try:
            result = eval(expression, {
                "sqrt": self.basic.sqrt,
                "abs": abs,
                "pow": pow,
                "sin": self.sci.sin,
                "cos": self.sci.cos,
                "tan": self.sci.tan,
                "asin": self.sci.asin,
                "acos": self.sci.acos,
                "atan": self.sci.atan,
                "log": self.sci.log,
                "ln": self.sci.ln,
                "exp": self.sci.exp,
                "fact": self.sci.factorial,
                "inv": self.sci.inverse,
                "pi": math.pi,
                "e": math.e,
                "sec": self.sci.sec,
                "csc": self.sci.csc,
                "cot": self.sci.cot,
  })
            self.hist.add_record(expression, result)
            return result
        except Exception as e:
            return f"Error: {str(e)}"
    
    def solve_equation(self, equation_str, variable='x'):
        try:
          var = symbols(variable)
          if '=' in equation_str:
            left, right = equation_str.split('=')
            eq = Eq(sympify(left), sympify(right))
          else:
            eq = Eq(sympify(equation_str), 0)
            result = solve(eq, var)
            return result
        except Exception as e:
          return f"Error: {str(e)}"

