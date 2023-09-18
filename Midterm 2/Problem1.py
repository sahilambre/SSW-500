
#! Problem 1

def median_fun(list):
    #TODO: Empty list check 
    if len(list) == 0: 
        return 0
        #TODO: Sort list elements in ascending order
    list.sort() 
    length = len(list)
    #TODO: Logic
    mid = length // 2 
    
    if length % 2 == 0: 
        median = (list[mid - 1] + list[mid]) / 2 
    else:
        median = list[mid] 
    return median

#TODO: User input
list = list(map(int, input("Enter a list of integer numbers (Separate using spaces): ").split()))

result = median_fun(list)

print("The median is: ", result)
