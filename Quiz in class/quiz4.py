# def example (n):

#     if n > 0:

#         print (n)

#         example (n-1)



def example (n):
    if n > 0:
        print (n)
        example (n)
    else:
        example (n-1)

print(example(2))

# def displayRange (lower, upper):
#     if lower <= upper:
#         lower = lower + 1
#         print (lower)
#     else:
#         print (upper)

# print(displayRange(5,2))

# data = {"b":20, "a":35, "c":70, "d":15, "f":25}
# print(data.items())
# # print(data ["a"])
# # print(data.get ("g", None))
# # print(len(data))
# # print(data.keys())
# # print(data.pop("b"))

# info = {"name": "Sandy", "age": 17}
# # print(info.keys())
# # print(info.get ("hobbies", None))

# test = {"Apple": 29, "Orange": 15, "Banana": 30} 
# print(sorted(test.items(), key=lambda i: i[1]))
# # print(sorted(test.items(), key=lambda x: items[1]))
# print(sorted(test.items(), key=lambda item: item[0]))