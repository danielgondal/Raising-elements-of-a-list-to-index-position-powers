numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Create a list containing the power of said number in bases raised 
# to the corresponding number in the index using Python map.

result = list(map(lambda element: element**(numbers.index(element)+1), numbers)) # lambda will use the index method to find the index of each element and raise it to that power.

print(result)
