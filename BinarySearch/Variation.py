# Given, just the range. Eg. 1-100

# Find n, which satifies some condition.

# Instead of comparing mid value with a target, compare mid value with the condition.

# Condition will say, if the given value was too high, or too low.
# Based on that, we will select our next half.
# Carryon with till the condition is meet.


def customFun(value):
    if value > 20:
        # Says value given is high
        return 1
    elif value < 20:
        # Says value given is low
        return -1
    # Match
    else:
        return 0


def binarySearchCustom(low, high, customFun):
    mid = (low + high) // 2

    while low <= high:
        if customFun(mid) > 1:
            low = mid + 1
        elif customFun(mid) < 1:
            high = mid - 1
        else:
            return mid
    return -1
