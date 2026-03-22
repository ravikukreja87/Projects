
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}


print("Test Dictionary:", test_dict)


k = int(input("Enter the value you want to check the frequency of: "))


result = 0


for i in test_dict:
    if test_dict[i] == k:
        result = result + 1


print(f"The frequency of {k} is: {result}")