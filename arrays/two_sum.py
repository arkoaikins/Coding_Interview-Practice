# Now we assume that that array is not sorted so we use the hash map to
# Solve this problem

def two_sum(num, target):
    # so i set my hash table to empty
    hash_table = {}
    # then i use enumerate to iterate over the numbers and their index
    for i, num in enumerate(num):
        # then i find the difference between the target and the numer am on right now and equare it to a value that i think can let me hit the target
        diff = target - num
        # Now i check if my diff is the has table
        if diff in hash_table:
            # then i will return the index of the diff and the i(which is the index of the num am on right now)
            return [hash_table[diff], i]
        # if it is not in the hash table then i will store the current num am on now and its index in the hash table
        hash_table[num] = i
    #if all goes and still the answer cannot be fine i just return an empty 
    return []

# SO the time complexity for this problem is O(n),where n is the number of elements in the array
# Each element is processed once

# The space complexity is also O(n),for the hash table. In the worse case,it stores n key-value pairs(if no pair is found)