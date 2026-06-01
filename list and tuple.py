# Program to find the largest and smallest elements in a list

'''numbers = [12, 45, 7, 89, 23, 5, 67]

largest = max(numbers)
smallest = min(numbers)

print("Largest element:", largest)
print("Smallest element:", smallest)'''


# Program to remove duplicate elements from a list

'''numbers = [1, 2, 3, 2, 4, 5, 1, 6]

unique_numbers = list(set(numbers))

print("List after removing duplicates:")
print(unique_numbers)'''

# Program to reverse a list without using reverse()

'''numbers = [10, 20, 30, 40, 50]

reversed_list = []

for i in range(len(numbers)-1, -1, -1):
    reversed_list.append(numbers[i])

print("Original List:", numbers)
print("Reversed List:", reversed_list)'''

#program to count even and odd numbers in a list

'''numbers = [1, 2, 3, 4, 5, 6]

even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers =", even)
print("Odd numbers =", odd)'''

# Program to merge two lists and sort the final list

'''list1 = [5, 2, 8]
list2 = [1, 7, 3]

final_list = list1 + list2
final_list.sort()

print("Sorted List:", final_list)'''

# Program to find the second largest element in a list

'''numbers = [10, 25, 45, 30, 15]

numbers.sort()

print("Second largest element:", numbers[-2])'''

# Program to check whether an element exists in a tuple

'''t = (10, 20, 30, 40, 50)

num = int(input("Enter element to search: "))

if num in t:
    print("Element exists in the tuple")
else:
    print("Element does not exist in the tuple")'''

# Program to count the occurrence of an element in a tuple

'''t = (10, 20, 30, 20, 40, 20, 50)

num = int(input("Enter element: "))

count = t.count(num)

print("Occurrence of", num, "=", count)'''

# Program to sort a list of tuples based on tuple values

'''data = [(3, 4), (1, 2), (5, 1), (2, 3)]

data.sort()

print("Sorted list of tuples:")
print(data)'''

# Program to convert a tuple into a list and a list into a tuple

# Tuple to List
'''t = (10, 20, 30, 40)
lst = list(t)

print("Tuple:", t)
print("Converted List:", lst)

# List to Tuple
l = [1, 2, 3, 4]
tup = tuple(l)

print("List:", l)
print("Converted Tuple:", tup)'''