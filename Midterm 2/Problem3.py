
#!Problem 3

def high_element(my_dict):
    values = list(my_dict.values())
 
    # values.sorted()
    values.sort(reverse=True)
    
    top3_values = values[:3]
    
    top3_dict = {}
    for key, value in my_dict.items():
        if value in top3_values:
            top3_dict[key] = value
    
    return top3_dict

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
new_dict = high_element(my_dict)
print(new_dict)
