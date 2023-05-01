def main(numbers,i):
    """
    You are given a list of numbers. i Delete and return the number in the index.
    Args:
        numbers(list): parameter
        i(int): parameter
    Returns: 
        list: return answer
    """
    numbers = [4, 7, 3, 2, 8]
    i = 2
    numbers.pop(i)
    return numbers
print(main(1,1))