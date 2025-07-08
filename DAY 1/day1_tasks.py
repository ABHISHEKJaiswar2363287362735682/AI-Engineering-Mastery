#TASK - 1
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

#TASK - 2(String Manipulation)

def count_vowel(s):
    count = 0   
    for char in s:
        if char in "AEIOUaeiou":
            count = count + 1
    return count
print(count_vowel("Artificial Intelligence"))

#TASK - 3

file = open("sample.txt", 'r')
content = file.read()
print(content)
file.close()
    
# TASK - 4
import numpy as np

a = np.arange(10)
print(a)
print(a.shape)
print(a.dtype)

#TASK - 5
b = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(b.reshape(3,4))

# TASK - 6

c = np.random.randint(1,10, size = (3,3))
d = np.random.randint(1,10, size = (3,3))
print(c)
print(d)
print(c+d)
print(c-d)
print(c*d)