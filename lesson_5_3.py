def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
print(is_even(4))

def is_odd(n):
    return n%2 != 0
print(is_odd(4))

def is_odd_2(n):
    return not (n%2 == 0)
print(is_odd_2(4))