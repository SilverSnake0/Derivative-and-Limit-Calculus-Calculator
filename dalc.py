from sympy import symbols, diff, sympify, limit, lambdify, oo, parse_expr, Pow
import numpy as np
import matplotlib.pyplot as plt
import pyperclip

# Function to calculate the derivative of a given function
def derivative(function, variable='x', n=1):
    x = symbols(variable)
    # Parsing and transforming the input function to a format that sympy can interpret
    # Replacing specific characters to adapt to the sympy library requirements
    if function.startswith('x'):
        expr = parse_expr('x' + function[1:].replace('^', '**').replace('x','*x').replace('√', 'sqrt').replace(variable, 'x'))
    else:
        expr = parse_expr(function.replace('^', '**').replace('x','*x').replace('√', 'sqrt').replace(variable, 'x'))
    derivative = diff(expr, x, n) # Derivative calculation
    solution = f"The #{n} derivative of the function {function} with respect to {variable} is:\n{derivative}" # Format the output string
    pyperclip.copy(solution) # Copy the solution automatically to computer clipboard so user can conveniently paste it
    print(solution) # Display the solution
    print('Solution copied to clipboard.')
    input('Press enter to return to the main menu...')

# Example usage:
#derivative('x^2 + 3x - 2')  # Calculates the first derivative with respect to 'x' (default)
#derivative('sqrt(1x) + sin(1x)')  # Calculates the first derivative with respect to 'x'
#derivative('√(1x) + sin(1x)', n=2)  # Calculates the second derivative with respect to 'x'
#derivative('x^3 + 2*x^2 + 1x', n=2)  # Calculates the second derivative with respect to 'x'
#derivative('x**2 + 3x - pi')  # Calculates the derivative with respect to 'x' for the function x^2 + 3x - pi

# Function to calculate the limit of a given function
def lim(function, variable='x', value=0, direction=None, tolerance=1e-6):
    x = symbols(variable)
    # Parsing and transforming the input function to a format that sympy can interpret
    if function.startswith('x'):
        expr = sympify('x' + function[1:].replace('√', 'sqrt').replace('x','*x').replace(variable, 'x'))
    else:
        expr = sympify(function.replace('√', 'sqrt').replace('x','*x').replace(variable, 'x'))
    expr = expr.replace(Pow, lambda base, exponent: base ** exponent)

    if value == 'oo': # Handling the infinity case
        if direction == 'left':
            limit_minus = limit(expr, x, -oo)
            solution = f'The limit of the function {function} as {variable} approaches ∞ from the left is: {limit_minus}\nlim{variable}->∞-({function})'
        elif direction == 'right':
            limit_plus = limit(expr, x, oo)
            solution = f'The limit of the function {function} as {variable} approaches ∞ from the right is: {limit_plus}\nlim{variable}->∞+({function})'
        else:
            limit_value = limit(expr, x, oo)
            solution = f'The limit of the function {function} as {variable} approaches ∞ is: {limit_value}\nlim{variable}->∞({function})'
    else:
        # Calculate the limit based on the provided direction
        if direction == 'left':
            limit_minus = limit(expr, x, value, dir='-')
            solution = f'The limit of the function {function} as {variable} approaches {value} from the left is: {limit_minus}\nlim{variable}->{value}({function})'
        elif direction == 'right':
            limit_plus = limit(expr, x, value, dir='+')
            solution = f'The limit of the function {function} as {variable} approaches {value} from the right is: {limit_plus}\nlim{variable}->{value}({function})'
        else:
            limit_value = limit(expr, x, value)
            solution = f'The limit of the function {function} as {variable} approaches {value} is: {limit_value}\nlim{variable}->{value}({function})'

    pyperclip.copy(solution)
    print(solution)
    print('Solution copied to clipboard.')
    input('Press enter to return to the main menu...')

# Example usage:
#lim('1/(1x)')  # Calculates the limit of 1/x as x approaches 0 (default)
#lim('sin(x)/1x', 'x', 0)  # Calculates the limit of sin(x)/x as x approaches 0
#lim('(3x**2 + 2x + 1) / (2x**2 - 3x + 4)', 'x', 2)  # Calculates the limit of the function as x approaches 2
#lim('(3x**2 + 2x + 1) / (2x**2 - 3*pi + 4/pi)', 'x', 2)  # Calculates the limit of the function as x approaches 2

def plot_graph(function, variable='x', xmin=-10, xmax=10, num_points=1000):
    x = symbols(variable)
    expr = lambdify(x, function.replace('^', '**').replace('√', 'sqrt').replace('x','*x'), modules=['numpy'])
    x_vals = np.linspace(xmin, xmax, num_points)
    y_vals = expr(x_vals)

    plt.plot(x_vals, y_vals)
    plt.xlabel(variable)
    plt.ylabel(f'f({variable})')
    plt.title(f'Graph of the function y = {function}')
    plt.grid(True)
    plt.show()

# Example usage:
#plot_graph('x**2 + 3x - 2')  # Plots the graph of the function y = x^2 + 3x - 2
#plot_graph('sin(1x)', variable='x', xmin=0, xmax=6.28)  # Plots the graph of the function y = sin(x) from x = 0 to 2*pi
def main_menu():
        print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
        print('▌                                                                                                                                  ▌')
        print('▌                             ███    ███  █████  ██ ███    ██     ███    ███ ███████ ███    ██ ██    ██                            ▌')  
        print('▌                             ████  ████ ██   ██ ██ ████   ██     ████  ████ ██      ████   ██ ██    ██                            ▌') 
        print('▌                             ██ ████ ██ ███████ ██ ██ ██  ██     ██ ████ ██ █████   ██ ██  ██ ██    ██                            ▌') 
        print('▌                             ██  ██  ██ ██   ██ ██ ██  ██ ██     ██  ██  ██ ██      ██  ██ ██ ██    ██                            ▌') 
        print('▌                             ██      ██ ██   ██ ██ ██   ████     ██      ██ ███████ ██   ████  ██████                             ▌')
        print('▌                                                                                                                                  ▌') 
        print('▌                                                        Calculus Functions                                                        ▌')
        print('▌                                    Please select from the following options by their number:                                     ▌')
        print('▌                                                                                                                                  ▌')
        print('▌1. Calculate Derivatives             2. Calculate Limit              3. Plot Graph                                                ▌')
        print('▌10.Exit                                                                                                                           ▌')
        print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
        try:
            menu_answer = int(input('Please enter a number:\n'))
        except:
            print('Please try again.')
            main_menu()
        if menu_answer == 1:
            try:
                function_input = input('Example input:\nx^3 + 2x^2 + 1x \nsqrt(1x) + sin(1x) \nPlease enter the function you would like to calculate the derivative for:')
                num_deriv = input(f"Please enter the derivative # you would like to calculate for the function: '{function_input}':\n")
                derivative(function_input, n=num_deriv)
            except Exception as e:
                input(e)
                print('Returning to main menu...')
            main_menu()
        elif menu_answer == 2:
            try:
                function_input = input('Example input:\n5x+pi\nPlease enter the function you would like to calculate the limit for: ')
                num_lim = input(f"(enter 'oo' for infinity)\nPlease enter the limit # you would like to calculate for the function '{function_input}': ")
                approach = input("Enter 'l' for left approach, 'r' for right approach, or 'none': ")

                if approach.lower() == 'l':
                    direction = 'left'
                elif approach.lower() == 'r':
                    direction = 'right'
                elif approach.lower() == 'none':
                    direction = None
                else:
                    print('Invalid approach. Please try again.')
                    main_menu()
                    return

                lim(function_input, variable='x', value=num_lim, direction=direction)
            except Exception as e:
                input(e)
                print('Returning to main menu...')
            main_menu()
        elif menu_answer == 3:
            try:
                function_input = input('Please enter the function that you would like to plot on the graph: ')
                plot_graph(function_input)
            except Exception as e:
                input(e)
                print('Returning to main menu...')
            main_menu()
        elif menu_answer == 10:
            pass
        else:
            main_menu()
main_menu()