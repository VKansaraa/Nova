import sympy as sp
import numpy as np
from scipy import stats
import math

def poly_eq(equation):
    x = sp.Symbol('x')
    equation = equation.replace('^', '**').replace(' ', '')
    parts = equation.split('=')
    left_side = sp.sympify(parts[0])
    right_side = sp.sympify(parts[1])
    solutions = sp.solve(left_side - right_side, x)
    simplified_solutions = [sp.simplify(sol) for sol in solutions]
    latex_solutions = [sp.latex(sol) for sol in simplified_solutions]
    decimal_solutions = [sol.evalf() for sol in simplified_solutions]

    return latex_solutions, decimal_solutions

def stats_solve(data):
    data = np.array(data)
    mean = np.mean(data)
    median = np.median(data)
    mode = stats.mode(data)
    std_dev = np.std(data)
    variance = np.var(data)
    return mean, median, mode, std_dev, variance

def solve_probability(expression):
    expression = expression.replace(' ', '')
    numerator = sp.sympify(expression)
    num_terms = sp.count_ops(numerator)
    return numerator / num_terms

def trig_calculations(select, angle):
    angle_rad = math.radians(angle)
    if select == 1:
        return math.sin(angle_rad)
    elif select == 2:
        return math.cos(angle_rad)
    elif select == 3:
        return math.tan(angle_rad)
    else:
        return None

def geo_calculations(shape, calc_type, *dimensions):
    if shape == 1:  # Circle
        radius = dimensions[0]
        if calc_type == 1:
            return math.pi * radius ** 2
        elif calc_type == 2:
            return 2 * math.pi * radius
    elif shape == 2:  # Triangle
        if calc_type == 1:
            base, height = dimensions
            return 0.5 * base * height
        elif calc_type == 2:
            return sum(dimensions)
    elif shape == 3:  # Rectangle
        length, breadth = dimensions
        if calc_type == 1:
            return length * breadth
        elif calc_type == 2:
            return 2 * (length + breadth)
    return None
def cal():
 while True :
    print('Hello! choose a type of calculation')
    print('1.multiplication')
    print('2.addition')
    print('3.substration')
    print('4.division')
    print('5.logarithm')
    print('6.exponential')
    print('7.quit')
    choice=int(input('enter your choice:'))
    if choice==1:
      numbers_str = input('enter the numbers separated by spaces:')
      numbers = [float(x) for x in numbers_str.split()]
      result = numbers[0]
      for i in range(1, len(numbers)):
        result = np.multiply(numbers[i], result)
      try:
       print("Result:", result)
      except( UnboundLocalError,OverflowError):
        print("this is too much for my little brain, try splitting it into smaller chunks")
    elif choice==2:
      numbers_str = input('enter the numbers separated by spaces:')
      numbers = [float(x) for x in numbers_str.split()]
      result = numbers[0]
      for i in range(1, len(numbers)):
        result = np.add(numbers[i],result)
      try:
       print("Result:", result)
      except( UnboundLocalError,OverflowError):
        print('this is too much for my little brain, try splitting it into smaller chunks')
    elif choice==3:
      numbers_str = input('enter the numbers separated by spaces:')
      numbers = [float(x) for x in numbers_str.split()]
      result = numbers[0]
      for i in range(1, len(numbers)):
        result = np.subtract(numbers,result)
      try:    
       print("Result:", result)
      except( UnboundLocalError,OverflowError):
          print('this is too much for my little brain, try splitting it into smaller chunks')
    elif choice==4:
      numbers_str = input('enter the numbers separated by spaces:')
      numbers = [float(x) for x in numbers_str.split()]
      result = numbers[0]
      for i in range(1, len(numbers)):
        result = np.divide(numbers,result)
      try:
       print("Result:", result)
      except( UnboundLocalError,OverflowError):
          print('this is too much for my little brain, try splitting it into smaller chunks')
    elif choice==5:
      e=float(input('enter the base'))
      g=float(input('enter the answer'))
      try:
        print(math.log(g)/math.log(e))
      except(UnboundLocalError,OverflowError):
         print('this is too much for my little brain, try splitting it into smaller chunks')
    elif choice==6:
      f=float(input('enter the base'))
      h=float(input('enter the power'))
      try:
       print(f**h)
      except(UnboundLocalError,OverflowError):
          print('this is too much for my little brain, try splitting it into smaller chunks')
    elif choice==7:
      print('you quitted')
      break
    else:
        print('invalid choice')

def main_menu():
    while True:
        print("Main Menu:")
        print("1. Polynomial Equation Solver")
        print("2. Statistics Calculator")
        print("3. Probability Solver")
        print("4. Trigonometry Calculator")
        print("5. Geometry Calculator")
        print("6. calculator")
        print("7. Quit")

        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            poly()
        elif choice == '2':
            statistic()
        elif choice == '3':
            prob()
        elif choice == '4':
            trig()
        elif choice == '5':
            geo()
        elif choice == '6':
            cal()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def poly():
    while True:
        equation = input("Enter the polynomial equation (or type 'quit' to exit): ")
        if equation.lower() == "quit":
            print("Quitted from polynomial equation")
            break
        latex_solutions, decimal_solutions = poly_eq(equation)
        print("Simplified solutions (LaTeX format):", latex_solutions)
        print("Decimal approximations:", decimal_solutions)

def statistic():
    while True:
        data = input("Enter the data for statistics (comma-separated) or 'quit' to exit: ")
        if data.lower() == 'quit':
            print("Quitted from statistics")
            break
        data = [float(x) for x in data.split(',')]
        mean, median, mode, std_dev, variance = stats_solve(data)
        print("Mean:", mean)
        print("Median:", median)
        print("Mode:", mode)
        print("Standard Deviation:", std_dev)
        print("Variance:", variance)

def prob():
    while True:
        expression = input("Enter the probability expression (or type 'quit' to exit): ")
        if expression.lower() == 'quit':
            print("Quitted from probability")
            break
        probability = solve_probability(expression)
        print("The probability is:", probability)

def trig():
    while True:
        print("1. Sin")
        print("2. Cos")
        print("3. Tan")
        print("4. Quit")

        select = int(input("Enter the type of trigonometric function to solve: "))
        if select == 4:
            print("You are quitting from trigonometry")
            break
        angle = float(input("Enter the angle in degrees: "))
        result = trig_calculations(select, angle)
        if result is not None:
            print(f"The value is: {result}")
        else:
            print("Invalid choice. Please try again.")

def geo():
    while True:
        print("1. Circle")
        print("2. Triangle")
        print("3. Rectangle")
        print("4. Quit")

        shape = int(input("Choose a type of shape: "))
        if shape == 4:
            print("You are quitting from geometry")
            break

        print("1. Area")
        print("2. Perimeter/Circumference")
        calc_type = int(input("Choose a type of calculation: "))

        if shape == 1:
            radius = float(input("Enter the radius: "))
            result = geo_calculations(shape, calc_type, radius)
        elif shape == 2:
            if calc_type == 1:
                base = float(input("Enter the base: "))
                height = float(input("Enter the height: "))
                result = geo_calculations(shape, calc_type, base, height)
            else:
                side_1 = float(input("Enter side 1: "))
                side_2 = float(input("Enter side 2: "))
                side_3 = float(input("Enter side 3: "))
                result = geo_calculations(shape, calc_type, side_1, side_2, side_3)
        elif shape == 3:
            length = float(input("Enter the length: "))
            breadth = float(input("Enter the breadth: "))
            result = geo_calculations(shape, calc_type, length, breadth)
        else:
            print("Invalid shape. Please try again.")
            continue

        if result is not None:
            print(f"The result is: {result}")
        else:
            print("Invalid calculation type. Please try again.")

if __name__ == "__main__":
    main_menu()
