INBUILT FUNCTIONS

str_items = ['ABC', 'aaa', 'ED', 'bda', 'JM']
str_items.sort()
print(str_items) # No proper sorting

# key=str.lower performs case insensitive sorting
str_items.sort(key = str.lower)
print(str_items) # properly sorted

str_items.sort(key = str.lower, reverse=True)
print(str_items) # Sorted in reverse

str_items = ['ABC', 'aaa', 'ED', 'bda', 'JM']
new_items = sorted(str_items, key=str.lower) # Make a new sorted list
print(str_items)
print(new_items)

int_items = [132, 13, 9, 1456, 24, 7]
new_items = sorted(int_items)
print(new_items)

sum_items = sum(int_items)
print(sum_items)
print(len(new_items))

average = sum_items/len(new_items)
print(average)
