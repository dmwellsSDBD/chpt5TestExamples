"""
    Abstraction - removes all but the relevant details needed to perform a task.
    
"""

def summation(lower, upper):
    """Arguments: A lower bound and an upper bound
    Returns: the sum of the numbers from lower through upper
    """
    result = 0
    while lower <= upper:
        result += lower
        lower += 1
    return result

print(summation(1, 50))

print(summation(45, 145))
    