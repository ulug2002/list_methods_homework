def main(fruits,x,i):
    """
    You will be given a list of fruits. Add the x fruit to the i index and return it.
    Args:
        fruits(list): parameter 
        x(str): parameter
        i(int): parameter
    Returns:
        list: return answer
    """
    fruits = ['kiwi','bannana']
    x = 'apple'
    i = 1
  
    fruits.insert(i,x)
    return fruits
print(main(1,1,1))