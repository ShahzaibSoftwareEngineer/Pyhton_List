# Reverse a List
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print("1. Reversed List:", reversed_list)

#  Find Maximum and Minimum in a List
numbers = [10, 50, 20, 70, 30]
print("2. Max:", max(numbers), "Min:", min(numbers))

#  Remove Duplicates from a List
duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(duplicates))
print("3. Unique List:", unique_list)

#  Sort a List
unsorted_list = [5, 1, 8, 3, 2]
sorted_list = sorted(unsorted_list)
print("4. Sorted List:", sorted_list)

#  Merge Two Lists
list1 = [1, 3, 5]
list2 = [2, 4, 6]
merged_list = list1 + list2
print("5. Merged List:", merged_list)

#  Find Even and Odd Numbers in a List
numbers_list = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers_list if num % 2 == 0]
odd_numbers = [num for num in numbers_list if num % 2 != 0]
print("6. Even Numbers:", even_numbers, "Odd Numbers:", odd_numbers)

#  Find the Second Largest Number in a List
nums = [10, 20, 4, 45, 99]
sorted_nums = sorted(set(nums), reverse=True)
second_largest = sorted_nums[1]
print("7. Second Largest Number:", second_largest)

#  Find Common Elements Between Two Lists
list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]
common_elements = list(set(list_a) & set(list_b))
print("8. Common Elements:", common_elements)

#  Rotate List to the Right by 2 Positions
original_list = [1, 2, 3, 4, 5]
rotated_list = original_list[-2:] + original_list[:-2]
print("9. Rotated List:", rotated_list)

#  Flatten a Nested List
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened_list = [item for sublist in nested_list for item in sublist]
print("10. Flattened List:", flattened_list)
