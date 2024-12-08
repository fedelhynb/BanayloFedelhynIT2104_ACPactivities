from database import Database
from rental_system import VehicleRental

if __name__ == "__main__":
    db = Database()
    db.connect()
    rental_system = VehicleRental(db)

    while True:
        rental_system.show_dashboard()

        choice = input("Enter choice: ")
        if choice == '1':
            rental_system.see_company_information()
        elif choice == '2':
            rental_system.make_rent()
        elif choice == '3':
            rental_system.cancel_rent()
        elif choice == '4':
            rental_system.update_reservation()
        elif choice == '5':
            rental_system.see_all_vehicles()
        elif choice == '6':
            rental_system.see_all_reservations()
        elif choice == '7':
            print("\n===== Thank you for being with SwiftRent: Vehicle Rental Services. Safe Travels! =====")
            break
        else:
            print("Invalid choice. Please try again.")
