# Import necessary modules and functions
import math
import pytest
from unittest.mock import patch
from a_v_calc_starter3 import (
    first_calculation,
    second_calculation,
    third_calculation,
    fourth_calculation,
    fifth_calculation,
)

# Define a test for the first calculation function
def test_first_calculation():
    # Use the 'patch' context manager to mock user input (side_effect provides input values)
    with patch("builtins.input", side_effect=["5", "10"]):
        result = first_calculation()
    # Check if the result of the function is as expected
    assert result == (50, 5, 10)

# Define a test for the second calculation function
def test_second_calculation():
    # Use the 'patch' context manager to mock user input (side_effect provides input values)
    with patch("builtins.input", side_effect=["5"]):
        result = second_calculation()
    # Check if the result is a tuple and has a length of 2
    assert isinstance(result, tuple)
    assert len(result) == 2

# Define a test for the third calculation function
def test_third_calculation():
    # Use the 'patch' context manager to mock user input (side_effect provides input values)
    with patch("builtins.input", side_effect=["10", "5"]):
        result = third_calculation()
    # Check if the result of the function is as expected
    assert result == (25, 10, 5)

# Define the fourth calculation function (it's not a test)
def fourth_calculation(input_function=input):
    # Prompt the user for input
    print("You selected prism volume calculation.")
    base = int(input_function("Input Base: "))
    length = int(input_function("Input length: "))
    height = int(input_function("Input height: "))

    # Calculate the volume of the prism
    volume = (base * length * height) / 2

    # Return the input values and the calculated volume
    return base, length, height, volume

# Define a test for the fifth calculation function
def test_fifth_calculation():
    # Use the 'patch' context manager to mock user input (side_effect provides input values)
    with patch("builtins.input", side_effect=["10"]):
        result = fifth_calculation()
    # Check if the result is a tuple and has a length of 2
    assert isinstance(result, tuple)
    assert len(result) == 2

# Run the pytest framework to execute the defined tests
if __name__ == '__main__':
    pytest.main()
