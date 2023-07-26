print(3 <= 3 < 9)
# True
# 3 <= 3 < 9 checks if 3 is greater than or equal to 3 (True) and also less than 9 (True). 
# Since both conditions are True, the entire expression evaluates to True.

print(3 == 3 == 3)
# True
# 3 == 3 == 3 is checking if 3 is equal to 3 (True) and if True is equal to 3 (False).
# Since both sides of the == operator are True, the entire expression evaluates to True.

print(bool(0))
# False
# The bool() function converts the argument to a boolean value. In this case, 
# bool(0) converts the integer 0 to a boolean, which is False.

print(bool(5 == "5"))
# False
# The expression 5 == "5" compares an integer (5) to a string ("5"). Since they have different types, the result is False.

print(bool(4 == 4) == bool("4" == "4"))
# True
# The first bool(4 == 4) evaluates to True, and the second bool("4" == "4") also evaluates to True. 
# Since both sides of the == operator are equal (both True), the entire expression evaluates to True.

print(bool(bool(None)))
# False
# The expression bool(None) converts the value None to a boolean, which is False. 
# So, the outer bool() function will return False.

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)
