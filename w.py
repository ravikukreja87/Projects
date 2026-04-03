
user_input = int(input("Enter a number: "))


odd_numbers = [num for num in range(user_input) if num % 2 != 0]

print(f"Odd numbers under {user_input}:")
print(odd_numbers)

fruits = ["apple", "banana", "mango", "cherry", "kiwi"]


updated_fruits = [fruit.capitalize() for fruit in fruits]

print("Original list:", fruits)
print("Updated list: ", updated_fruits)