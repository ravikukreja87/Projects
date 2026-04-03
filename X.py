# A. Colors Set
set1_a = {'blue', 'green'}
set2_a = {'blue', 'yellow'}

# Method 1: Using the symmetric_difference() method
result_a = set1_a.symmetric_difference(set2_a)
print(f"Symmetric Difference A: {result_a}")


# B. Numbers Set
set1_b = {1, 2, 3, 4, 5}
set2_b = {1, 5, 6, 7, 8, 9}

# Method 2: Using the ^ operator (shorthand for symmetric difference)
result_b = set1_b ^ set2_b
print(f"Symmetric Difference B: {result_b}")