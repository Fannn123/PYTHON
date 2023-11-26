# MENCARI ANGKA MAX

#MENGGUNAKAN FUNCTION sum()
numbers = [1,2,3,4,5]
number = sum(numbers)
print(number)

#menggunakan function max()
numbers = [2,6,4,8,1]
number = max(numbers)
print(number)

#CARA RUMIT MENCARI MAX NUMBER
numbers = [3,6,8,9,1]
max_number = numbers[0]

for number in numbers :
    if number > max_number :
        max_number = number
print(max_number)