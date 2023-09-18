class Fraction:
    """ Support addition, subtraction, multiplication, and division of fractions
        with a simple algorithm
    """

    def __init__(self, num: float, denom: float) -> None:
        """ store num and denom
            Raises a ZeroDivisionError on 0 denominator
        """
        
        self.num = num
        self.denom = denom

        if self.denom == 0:
            raise ZeroDivisionError

    def __str__(self) -> str:
        """ return a String to display fractions """
        
        return f"{self.num}/{self.denom}"


    def plus(self, other: "Fraction") -> "Fraction":
        """ Adds two fractions using simplest approach.
            Calculate snew numerator and denominator and return new Fraction
        """
        
        if self.equal(other):
            newNum = self.num + other.num
            newDenom = self.denom + other.denom
        else:
            newNum = self.num * other.denom + self.denom * other.num
            newDenom = self.denom * other.denom
        return Fraction(newNum, newDenom)

    def minus(self, other: "Fraction") -> "Fraction":
        """ subtracts two fractions using simplest approach
            Calculates new numerator and denominator and return new Fraction
        """
        
        if self.equal(other):
            return 0
        else:
            newNum = self.num * other.denom - self.denom * other.num
            newDenom = self.denom * other.denom
        return Fraction(newNum, newDenom)

    def times(self, other: "Fraction") -> "Fraction":
        """ Multiply two fractions using simplest approach
            Calculate new numerator and denominator and return new Fraction
        """
        
        newNum = self.num * other.num
        newDenom = self.denom * other.denom
        return Fraction(newNum, newDenom)

    def divide(self, other: "Fraction") -> "Fraction":
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        
        newNum = self.num * other.denom
        newDenom = self.denom * other.num
        return Fraction(newNum, newDenom)

    def equal(self, other: "Fraction") -> bool:
        """ returns True/False if the two fractions are equivalent """
        
        if self.num == other.num and self.denom == other.denom:
            return True
        else:
            return False

def test_suite() -> None:
    
    f12: Fraction = Fraction(1, 2)
    f34: Fraction = Fraction(3, 4)
    f68: Fraction = Fraction(6, 8)
    f128: Fraction = Fraction(12, 8)
    f32: Fraction = Fraction(3, 2)
    f912: Fraction = Fraction(9, 12)
    f44: Fraction = Fraction(4, 4)
    print(f"{f12} + {f34} = {f12.plus(f12)} [10/8]")

    # include a test with three operands
    print(f"{f12} + {f34} + {f44} = {f12.plus(f34).plus(f44)} [72/32]")

    
    print(f"{f12} + {f12} = {f12.plus(f12)} [4/4]")
    print(f"{f44} - {f12} = {f44.minus(f12)} [4/8]")
    print(f"{f12} + {f44} = {f12.plus(f44)} [12/8]")
    print(f"{f128} == {f32} is {f128.equal(f32)} [True]")


def get_number(prompt: str) -> float:
    """ read and return a number from the user.
        Loop until the user provides a valid number.
    """
    while True:
        inp: str = input(prompt)
        try:
            return float(inp)
        except ValueError:
            print(f"Error: '{inp}' is not a number. Please try again...")


def get_fraction() -> Fraction:
    """ Asks the user for a numerator and denominator and return a valid Fraction
"""
    while True:
        num = get_number("Enter the numerator value:")
        denom = get_number("Enter the denominator value:")
        return Fraction(num, denom)


#

def compute(f1: Fraction, operator: str, f2: Fraction) -> None:
    """ Givestwo fractions and an operator, returns the result
        of applying the operator to the two fractions
    """
    okay = True
    result: Fraction  
    if operator == '+':
        result = f1.plus(f2)
    
    elif operator == '-':
        result = f1.minus(f2)
    elif operator == '*':
        result = f1.times(f2)
    elif operator == '/':
        result = f1.divide(f2)
    else:
        print(f"Error: '{operator}' is an unrecognized operator")
        okay = False
    if okay:
        print(f"{f1} {operator} {f2} = {result}")


def main() -> None:
    """ Fraction calculations """
    print('Welcome to the fraction calculator!')
    f1: Fraction = get_fraction()
    operator: str = input("Operation (+, -, *, /): ")
    f2: Fraction = get_fraction()

    try:
        compute(f1, operator, f2)
    except ZeroDivisionError as e:
        print(e)


if __name__ == '__main__':
    test_suite()
    main()

