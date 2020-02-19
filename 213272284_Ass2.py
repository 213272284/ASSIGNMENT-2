######FUNCTIONS ASSIGNMENT#######

######Problem 1########
nums = [1,0,2,3,1]
check = 0,2,3
x = check[0]
y = check[1]
z = check[2]

def list_check(nums):
    """
        This function returns true if sequence '0,2,3' is in the list
    """
    if x in nums and y in nums and z in nums:
        if nums.index(x) < nums.index(y) < nums.index(z):
            return True
    return False
print(list_check(nums))

###############################
#####Problem 2#########
str = 'Hello'
def string_bits(str):
    """
    This functions returns a new string made of every other character starting with the first
    """
    return (str[::2])
    print(string_bits(str))

###############################
#####Problem 3#########
a = 'abc'
b = 'Hiabc'
def end_other(a,b):
    """
    This function returns true if either of the strings appears at the very end of the other string
    """
    a = a.upper()
    b = b.upper()
    a_length = len(a)
    b_length = len(b)
    if a[-b_length:] == b or b[-a_length:] == a:
        return True
    else:
        return False
    print(end_other(a,b))

###############################
#####Problem 4#########
str = 'abc'
def double_char(str):
    """
    This function returns a string where for every char in the original there are two chars
    """
    new_str = ''
    for a in list(str):
        new_str += a * 2
    return new_str
    print(double_char(str))

###############################
#####Problem 5#########

def no_teen_sum(a,b,c):
    """
    This function returns the sum of the 3 given integers
    """
    sum = a + b + c
    def fix_teen(n):
        """
        This function returns a value fixed for the teen rule
        """
        list = (13,14,17,18,19)
        if n in list:
            n = 0
return(sum)

###############################
#####Problem 6#########
nums = [2,3,6,10,8,5]
def count_evens(nums):
    """
    This function returns the number of even numbers in an array
    """
    total_num = 0
    for x in nums:
        if x % 2 == 0:
            total_num += 1
    return total_num
print(count_evens(nums))

############################################################################
