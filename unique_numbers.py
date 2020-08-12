numbers = [45,4,3,34,3,23,9,4,45,34,34,34,9,23,23,23,23]
numbers.sort()
print(numbers)
temp_set = []

for x in range(len(numbers)-1):
    if numbers[x] != numbers[x+1]:
        temp_set.append(numbers[x])
temp_set.append(numbers[-1])

print(temp_set)

"""
I did not think about this, but mosh does it the following way

numbers = [45,4,3,34,3,23,9,4,45,34,34,34,9,23,23,23,23]
2	unique = []
3	
4	for x in numbers:
5	    if x not in unique:
6	        unique.append(x)
7	        
8	print(unique)
"""

