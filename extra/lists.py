# vals = [expression
#         for value in collection
#         if condition]
# # This is equivalent to:

# vals = []

# for value in collection:
#     if condition:
#         vals.append(expression)

# Example:

even_squares = [x * x for x in range(10) if not x % 2]

print(even_squares)