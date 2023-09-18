
#! Question 7
def isSorted(lst):
    if len(lst) <= 1:
        return True

    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False

    return True


user_list = input("Enter a list of numbers space separated: ").split()
user_list = [int(num) for num in user_list]

sorted_status = isSorted(user_list)
print("Is the list sorted?", sorted_status)

