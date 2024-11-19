def is_perfect_number(n):
    divisors_sum = 0 #initializing varible to store sum of divisors
    
    #find divisors
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    
    #check if sum of divisors are equal to the number
    if divisors_sum == n:
        return True
    else:
        return False

def main():
    while True:
        user_input = input("Enter a number: ") 
        
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break   
        try:
            num = int(user_input)

            if is_perfect_number(num):
                print(f"{num} is a perfect number.")
            else:
                print(f"{num} is not a perfect number.")

        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
