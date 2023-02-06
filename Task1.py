import random
# generate 100 random numbers between 0 and 1000
randomlist = random.sample(range(0, 1000), 100)
print(randomlist)                   # console output

# sort list from min to max (without using sort())
unsorted_list = randomlist
sorted_list = []
while unsorted_list:
    minimum = unsorted_list[0]
    for x in unsorted_list:             # iterating each number in list
        if x < minimum:
            minimum = x
    sorted_list.append(minimum)         # adds an element to the end of the list
    unsorted_list.remove(minimum)       # removes the first element in the list
print(sorted_list)  # console output

# calculate average for even and odd numbers and print both average result in console
numbers = sorted_list
summ = 0
count = 0
for num in numbers:        # iterating each number in list
    if num % 2 == 0:       # checking condition if number is even
        summ = summ + num  # calculate sum for even numbers
        count += 1         # counting for even numbers
average = summ / count     # counting average for even numbers
print("average for even numbers:", average)  # console output

numbers = sorted_list
summ = 0
count = 0
for num in numbers:        # iterating each number in list
    if num % 2 != 0:       # checking condition if number is odd
        summ = summ + num  # calculate sum for odd numbers
        count += 1         # counting for odd numbers
average = summ / count     # counting average for odd numbers
print("average for odd numbers:", average)  # console output

