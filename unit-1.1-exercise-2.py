#Author: Spohia
#Created Date: August, 21, 2021
#Description: This program has two functions to find the maximum
#value of three numbers
#Example usage: print(max_of_three(20, 30, -10))
#Result: function returns 30
#Function: max_of_two
#Purpose: This function accepts two numbers, compares them
#and returns the value that is larger.
def max_of_two( firstNumber, secondNumber ):
    if firstNumber > secondNumber:
        return firstNumber
    return secondNumber
#Function: max_of_three
#Purpose: This function accepts three numbers and sends the second and third 
#numbers to max_of_two. It then takes the result of that comparison to
#send the first number and the result to get the larger value
#of all three.
def max_of_three( firstNumber, secondNumber, thirdNumber ):
    return max_of_two( firstNumber, max_of_two( secondNumber, thirdNumber))
#Testing the function max_of_three
print(max_of_three(20, 30, -10))