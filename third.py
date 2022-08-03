# string = "this,is my,string"
# search_for = "is"
# total = string.count(search_for)

# print(f"{total} result(s) found")
# print(string.replace(search_for, search_for.upper()))




# print(string.replace(" ", "-"))


# print(string.split(","))


# str_list = ["This", "is", "a", "new", "string"]

# joined = " ".join(str_list)

# print(joined)


                ######## FUNCTIONS ###########

from cmath import pi


def add_numbers(a:int, b:int):
    """This function adds numbers.

    Args:
        a (int): This is the first number to be added
        b (int): This is the second number to be added
        
    Returns:
        a+b (int): This is the addition of a and b
    """
    
    return a+b


# b = add_numbers(53,35)
# print(b)


###### CORRECTION

def simple_interest(principal:int, rate:int, time:int):
    """This is a function that calculates simple interest.

    Args:
        principal (int): Initial capital
        rate (int): Rate of interest e.g 50 for 50%
        time (int): Duration of investment.

    Returns:
        interest: The total returns on investment of principal after the time has elapsed.
    """
    
    rate/=100
    interest = principal*rate*time
    return interest


a = simple_interest(53535, 8, 5)

def poc(r:int):
    """ Ths is a function that calculates perimeter of circle.
    Args:
      r (int): Radius of the circle
       
    Returns: 
      2*pi*r (float): This are the numbers to multiply 
    """
    pi= 3.142
    
    return 2* pi * r



print(poc(4835))
