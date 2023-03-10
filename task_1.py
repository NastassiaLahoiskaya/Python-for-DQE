import random

# generate 100 random numbers between 0 and 1000
randomlist = random.sample(range(0, 1000), 100)
print(randomlist)  # console output

# sort list from min to max (without using sort())
unsorted_list = randomlist
sorted_list = []
while unsorted_list:
    minimum = unsorted_list[0]
    for x in unsorted_list:  # iterating each number in list
        if x < minimum:
            minimum = x
    sorted_list.append(minimum)  # adds an element to the end of the list
    unsorted_list.remove(minimum)  # removes the first element in the list
print(sorted_list)  # console output

# calculate average for even and odd numbers and print both average result in console

sum_even = 0
count_even = 0
sum_odd = 0
count_odd = 0
for num in sorted_list:  # iterating each number in list
    if num % 2 == 0:  # checking condition if number is even
        sum_even = sum_even + num  # calculate sum for even numbers
        count_even += 1  # counting for even numbers
    elif num % 2 != 0:  # checking condition if number is odd
        sum_odd = sum_odd + num  # calculate sum for odd numbers
        count_odd += 1  # counting for odd numbers
average_even = sum_even / count_even
average_odd = sum_odd / count_odd
print("average for even numbers:", average_even)  # console output
print("average for odd numbers:", average_odd)  # console output
