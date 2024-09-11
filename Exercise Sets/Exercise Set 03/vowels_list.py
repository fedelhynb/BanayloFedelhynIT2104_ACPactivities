def print_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = [f"'{char}'" for char in input_string if char in vowels]
    print(f"[{', '.join(result)}]")

user_input = input("Enter a string: ")
print_vowels(user_input)
