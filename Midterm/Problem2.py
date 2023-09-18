

import math

def read_numbers_from_file(file_name):
    with open(file_name, 'r') as file:
    # file = open(file_name, 'r')
        numbers = file.readlines()
        numbers = [int(num.strip()) for num in numbers]
        return numbers

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    # return [((number - mean) ** 2) for num in numbers] / len(numbers) - 1
    return sum([((num - mean) ** 2) for num in numbers]) / len(numbers) - 1

def calculate_standard_deviation(numbers):
    variance = calculate_variance(numbers)
    return math.sqrt(variance)

if __name__ == '__main__':
    file_name = 'Problem 2.txt'
    numbers = read_numbers_from_file(file_name)
    standard_deviation = calculate_standard_deviation(numbers)
    print("The standard deviation is {:.3f}".format(standard_deviation))





# import numpy

# file = open("Problem 2.txt", 'r')
# numbers = [int(line.strip()) for line in file]
# # print(numbers)

# standard_deviation = numpy.std(numbers)
# print(standard_deviation)
