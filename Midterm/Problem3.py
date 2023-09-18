
#TODO: revecrse elements of the list
def reverse_list(list):
    num = len(list)
    for element in range(num // 2):
        list[element], list[num-element-1] = list[num-element-1], list[element]
    return list

#TODO: take input from the user
def get_list_from_user():
    # list = float(input("Enter elements seperated by spaces: ")).split()
    list = input("Enter elements seperated by spaces: ").split()
    return list

#TODO: main function
if __name__ == '__main__':
    list = get_list_from_user()
    reversed_lst = reverse_list(list.copy())
    # reversed_lst = reverse_list(list.copy())

    print("Original list", list)
    print("Reversed list:", reversed_lst)
