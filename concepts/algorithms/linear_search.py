# A function that uses the linear_search algorithm to find a value
def linear_search(list, target):
    """
    So it takes in the list that we need to find or valuea
    and the the target(which is the value we looing for)
    and returns the index of that value(target)
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
        else:
            return None
    
    """
    So we use a for loop to iterate over the list from 0 to the end of 
    the list and check if the value of and index(i) is equal to the target
    then we return that index if not we retrun  None indicating that there
    is not value like that
    """