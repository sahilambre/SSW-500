def raise_exception():
    raise ValueError
    print("leaving raise_exception()")

def inner():
    raise_exception()
    print("leaving inner()")

def outer():
    inner()
    print("leaving outer()")

def way_out():
    try:
        outer()
    except ValueError:
        print("way_out(): caught a ValueError")
    print("leaving way_out()")

way_out()

# class Quiz:
#     def init(self, score: int):
#         self.grade: int = score

# # Now you can create an instance of the Quiz class:
# q = Quiz(10)
# print(q)

def check(x):
    if x < 0:
        raise ValueError("ValueError: {} is not greater than 0".format(x))


try:
    check(-1)
except ValueError as error:
    print(error)
