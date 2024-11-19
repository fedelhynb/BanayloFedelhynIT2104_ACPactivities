def roman_to_integer(roman):
    #dictionary; roman numerals = integer values
    roman_values = {
        'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000,
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    
    # Initialize total to 0
    total = 0
    # processess numerals from right to left
    previous_value = 0
    for char in reversed(roman):
        if char not in roman_values:
            raise ValueError(f"Invalid Roman numeral character: {char}")
        current_value = roman_values[char]
        
        #subtract it subtracting if curr. value is less than prev. value
        if current_value < previous_value:
            total -= current_value
        else:
            # Otherwise, add curr. val
            total += current_value
        
        previous_value = current_value
    
    return total


if __name__ == "__main__":
     while True: 
        roman_numeral = input("Enter a Roman numeral: ").strip()

        if roman_numeral.lower() == 'exit':
            print("Exiting the program.")
            break
        try:
            result = roman_to_integer(roman_numeral)
            print(f"The integer value of '{roman_numeral.upper()}' is: {result}")
        except ValueError as e:
            print(f"Error: {e}")
