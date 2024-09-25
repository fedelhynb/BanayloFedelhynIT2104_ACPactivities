while True:
    tpa=int(input("Enter the total purchase amount: "))
    print("Initial Purchase Amount:", tpa, ".00")

    disc1 = 10
    disc2 = 5

    if tpa >= 5000:
        discount1 = (disc1 / 100) * tpa
        print (f"Discount: {discount1:.2f} ")
        fprice = tpa - discount1
        print (f"Final Price: {fprice:.2f}")
    else :
        discount2 = (disc2 / 100) * tpa
        print (f"Discount:{discount2:.2f}")
        fprice = tpa - discount2
        print (f"Final Price: {fprice:.2f}")

    again= input("Do you want to try again? (yes/no): ").strip().lower()

    if again != 'yes':
        print("Thank you!")
        break 