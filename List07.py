def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace zero with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    i=0
    while i<5:
        if list1[i]==[0]:
            list1[i]=[False]
        i+=1
    return list1
print(main((1,0,1,1,0)))