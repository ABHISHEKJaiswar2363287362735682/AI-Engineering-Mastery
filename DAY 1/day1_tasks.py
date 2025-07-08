# Task 1: List & Dictionary Practice
import math
nums = [2,4,6,8,10]
squares = []
for i in nums:
    squares.append(i ** 2)
print(squares)

dictionary = {}

for i in nums:
    dictionary[i] = i**2
print(dictionary)

# Task 2: String Manipulation
def count_vowel(s):
    count = 0   
    for char in s:
        if char in "AEIOUaeiou":
            count = count + 1
    return count
print(count_vowel("Artificial Intelligence"))

# Task 3: File I/O Basic
file = open("sample.txt", 'r')
content = file.read()
print(content)
file.close()
    
# Task 4: Array Creation
import numpy as np
a = np.arange(10)
print(a)
print(a.shape)
print(a.dtype)

# Task 5: Reshaping Practice
b = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(b.reshape(3,4))

# Task 6: Array Operations
c = np.random.randint(1,10, size = (3,3))
d = np.random.randint(1,10, size = (3,3))
print(c)
print(d)
print(c+d)
print(c-d)
print(c*d)
