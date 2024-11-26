# script.py

from Capybara import Capybara

def display_capybara_details(capybaras, index):
    try:
        capybara = capybaras[index]
        print(f"Test Case {index + 1}: {capybara}")
    except IndexError:
        print("Invalid test case number. Please choose a valid number.")

def main():
    # Create instances of Capybara
    capybara1 = Capybara("Biscoff", "M", 5)
    capybara2 = Capybara("Capri", "F", 3)
    capybara3 = Capybara("Carlos", "M", 5)

    # Store the instances in a list
    capybaras = [capybara1, capybara2, capybara3]

    # Prompt the user to select a test case
    try:
        test_case_number = int(input("Enter the test case number: ")) - 1
        display_capybara_details(capybaras, test_case_number)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
