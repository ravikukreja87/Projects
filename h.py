class RomanConverter:
    def int_to_roman(self, num: int) -> str:
        # Define the mapping of values to Roman symbols in descending order
        # This includes the subtractive cases (e.g., 4, 9, 40, etc.)
        val_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        roman_num = ""
        
        for value, symbol in val_map:

            count = num // value

            roman_num += symbol * count
            
            num %= value
            
        return roman_num


if __name__ == "__main__":
    try:
        user_input = int(input("Enter an integer to convert to Roman: "))
        
        if user_input <= 0:
            print("Please enter a positive integer greater than 0.")
        else:
            converter = RomanConverter()
            result = converter.int_to_roman(user_input)
            print(f"The Roman numeral for {user_input} is: {result}")
            
    except ValueError:
        print("Invalid input. Please enter a valid integer.")