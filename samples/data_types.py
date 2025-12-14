# Data Types in Python
# ====================

# --------
# Integers
# --------

multiplication_int: int = 5 * 2
result1: int = 10  # integer

division_int: int = 10 // 2  # floor division returns int
result2: int = 5  # integer

sum_int: int = 2 + 3      # results in 5
difference_int: int = 4 - 1  # results in 3

a: int = 10
print("Integer:", a, "Type:", type(a))


# ------
# Floats
# ------

b: float = 10.5
print("Float:", b, "Type:", type(b))

multiplication_float: float = 5.1 * 2.0
result3: float = 10.2  # float

division_float: float = 10.0 / 4.0  # division returns float
result4: float = 2.5  # float

sum_float: float = 2.1 + 3.4        # results in 5.5
difference_float: float = 4.5 - 1.2  # results in 3.3


# --------
# Strings
# --------

c: str = "Hello, Python!"
print("String:", c, "Type:", type(c))


# --------
# Booleans
# --------

d: bool = True
print("Boolean:", d, "Type:", type(d))

e: bool = False
print("Boolean:", e, "Type:", type(e))

bool_sum1: int = True + True     # results in 2
bool_sum2: int = False + True   # results in 1
bool_sum3: int = False + False  # results in 0

# Booleans behave like integers:
# True  == 1
# False == 0
