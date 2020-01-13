"""my_math.py programm"""

def summ(num_a, num_b):
    """This function sums 2 numbers"""

    return num_a + num_b

def diff(num_a, num_b):
    """This function finds a differnce of the numbers"""

    return num_a - num_b

def mult(num_a, num_b):
    """This function multiplies 2 numbers"""

    return num_a + num_b

def div(num_a, num_b):
    """This function divides 2 numbers"""

    return num_a / num_b

if __name__ == "__main__":
    print(summ(int(input()), int(input())))
    print(diff(int(input()), int(input())))
    print(mult(int(input()), int(input())))
    print(div(int(input()), int(input())))
