import os
import sqlite3
from datetime import datetime

# Database connection setup
class Database:
    def __init__(self, db_file='vehicle_rental.db'):
        self.db_name = db_file
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def connect(self):
        """Connect to the SQLite database, creating tables if not already present"""
        self.create_tables()  # Ensure tables are created each time
        if not self._is_sample_data_inserted():
            self.insert_sample_vehicles()

    def create_tables(self):
        """Create tables for vehicles and reservations"""
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS vehicles (
                                    id INTEGER PRIMARY KEY,
                                    type TEXT,
                                    model TEXT,
                                    plate_number TEXT,
                                    available BOOLEAN,
                                    daily_rate INTEGER
                                )''')

            self.cursor.execute('''CREATE TABLE IF NOT EXISTS reservations (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    client_name TEXT,
                                    contact_number INTEGER,
                                    email TEXT,
                                    pickup_datetime TEXT,
                                    return_datetime TEXT,
                                    vehicle_id INTEGER,
                                    fee REAL,
                                    FOREIGN KEY(vehicle_id) REFERENCES vehicles(id)
                                )''')

            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def insert_sample_vehicles(self):
        """Insert sample vehicles into the database"""
        vehicles = [
            ('Car', 'Toyota Camry', 'ABC1234', True, 3800),
            ('Car', 'Honda Civic', 'HND5678', True, 3800),
            ('Car', 'Ford Mustang', 'FDM2345', True, 3800),
            ('Car', 'Chevrolet Malibu', 'CHV6789', True, 3800),
            ('Car', 'Mazda 3', 'MZD0123', True, 3800),
            ('Van', 'Toyota Hiace', 'XYZ5678', True, 5500),
            ('Van', 'Nissan NV350', 'NSN6789', True, 5500),
            ('Van', 'Hyundai H-1', 'HYD1234', True, 5500),
            ('Van', 'Kia Carnival', 'KIA9876', True, 5500),
            ('Van', 'Mitsubishi L300', 'MIT5678', True, 5500),
            ('Motorcycle', 'Yamaha R15', 'R15AB123', True, 2800),
            ('Motorcycle', 'Kawasaki Ninja', 'KAW1234', True, 2800),
            ('Motorcycle', 'Honda CBR150R', 'CBR4567', True, 2800),
            ('Motorcycle', 'Suzuki GSX-R150', 'GSX1234', True, 2800),
            ('Motorcycle', 'Yamaha YZF-R3', 'YZF5678', True, 2800),
        ]
    
        for vehicle in vehicles:
            self.cursor.execute('''INSERT INTO vehicles (type, model, plate_number, available, daily_rate)
                                   VALUES (?, ?, ?, ?, ?)''', vehicle)
            print(f"Inserted vehicle: {vehicle}")
    
        self.conn.commit()

    def _is_sample_data_inserted(self):
        """Check if sample data is already present in the vehicles table"""
        self.cursor.execute("SELECT COUNT(*) FROM vehicles")
        count = self.cursor.fetchone()[0]
        return count > 0

    def fetch_all(self, query, params=None):
        """Fetch all rows from a query"""
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def execute_query(self, query, params=()):
        """Execute a query"""
        self.cursor.execute(query, params)
        self.conn.commit()


# Vehicle Class
class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, model, plate_number, available, daily_rate):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.model = model
        self.plate_number = plate_number
        self.available = available
        self.daily_rate = daily_rate

    def mark_as_unavailable(self, db):
        """Mark vehicle as unavailable in the database"""
        db.execute_query("UPDATE vehicles SET available = 0 WHERE id = ?", (self.vehicle_id,))

    def mark_as_available(self, db):
        """Mark vehicle as available in the database"""
        db.execute_query("UPDATE vehicles SET available = 1 WHERE id = ?", (self.vehicle_id,))


# Reservation Class
class Reservation:
    def __init__(self, reservation_id, client_name, contact_number, email, pickup_datetime, return_datetime, vehicle, fee):
        self.reservation_id = reservation_id
        self.client_name = client_name
        self.contact_number = contact_number
        self.email = email
        self.pickup_datetime = pickup_datetime
        self.return_datetime = return_datetime
        self.vehicle = vehicle
        self.fee = fee

    def cancel(self, db):
        """Cancel the reservation and make vehicle available"""
        db.execute_query("DELETE FROM reservations WHERE id = ?", (self.reservation_id,))
        self.vehicle.mark_as_available(db)

    def update(self, db, new_pickup_datetime, new_return_datetime, new_vehicle, additional_fee):
        """Update reservation details"""
        db.execute_query('''UPDATE reservations
                             SET pickup_datetime = ?, return_datetime = ?, vehicle_id = ?, fee = fee + ?
                             WHERE id = ?''', 
                         (new_pickup_datetime, new_return_datetime, new_vehicle.vehicle_id, additional_fee, self.reservation_id))
        self.vehicle.mark_as_available(db)
        self.vehicle = new_vehicle
        self.vehicle.mark_as_unavailable(db)


# Vehicle Rental System
class VehicleRental:
    def __init__(self, db):
        self.db = db

    def show_dashboard(self):
        """Display the main menu/dashboard for the vehicle rental service"""
        print("=" * 80)
        print("----------------- WELCOME TO SWIFTRENT: VEHICLE RENTAL SERVICES! ---------------")
        print("=" * 80)
        print("1. See Company Information")
        print("2. Make your Rent")
        print("3. Cancel your Rent")
        print("4. Update your Rent")
        print("5. View Available Vehicles")
        print("6. See all Reservations")
        print("7. Exit")
        print("=" * 80)


    def see_company_information(self):
        print("\n" + "=" * 95)
        print("                       Welcome to SwiftRent: Vehicle Rental Services!                            ")
        print("   We offer various types of vehicles for rent including Cars, Vans, and Motorcycles.")
        print(" Our goal is to provide you with a reliable, affordable, and enjoyable rental experience.")
        print("         We hope to swiftly accommodate your needs. Thank you and Safe Travels!\n")
        print("For more information, you may contact: ")
        print("SwiftRent CEO: Ms. Fedelhyn Banaylo | +63 9632549800 | ms.fedelhynb@gmail.com")
        print("=" * 95 + "\n")


    def see_all_vehicles(self):
        """Display all vehicles with their availability status"""
        print("\n=========================================== ALL VEHICLES ===========================================")
        vehicles_data = self.db.fetch_all("SELECT id, type, model, plate_number, available, daily_rate FROM vehicles")

        if not vehicles_data:
            print("No vehicles available.")
            return

        # Print vehicle table headers
        print(f"{'ID':<5} {'Model':<23} {'Plate Number':<20} {'Type':<15} {'Availability':<15} {'Daily Rate':<15}")
        print("-" * 100)

        for vehicle in vehicles_data:
            vehicle_id, model, plate_number, vehicle_type, available, daily_rate = vehicle
            availability = "Available" if available else "Reserved"
            print(f"{vehicle_id:<5} {model:<23} {plate_number:<20} {vehicle_type:<15} {availability:<15} ₱{daily_rate:,.2f}")
        print("\n")


    def print_vehicle_table(self, vehicles):
        """Print vehicle details in a table format"""
        print(f"{'ID':<5} {'Type':<15} {'Model':<20} {'Plate Number':<15} {'Availability':<20} {'Rate/Day':<10}")
        print("-" * 100)

        for vehicle in vehicles:
            availability = "Available" if vehicle.available else "Reserved"
            formatted_rate = f"₱{vehicle.daily_rate:,.2f}"
            print(f"{vehicle.vehicle_id:<5} {vehicle.vehicle_type:<15} {vehicle.model:<20} {vehicle.plate_number:<15} {availability:<20} {formatted_rate:<30}")
    

    def create_reservation(self, client_name, contact_number, email, pickup_datetime, return_datetime, vehicle, fee):
        """Create a new reservation in the database"""
        # Prepare the query to insert reservation data
        query = '''INSERT INTO reservations (client_name, contact_number, email, pickup_datetime, return_datetime, vehicle_id, fee)
                    VALUES (?, ?, ?, ?, ?, ?, ?)'''
    
        # Execute the query with the provided data
        self.db.execute_query(query, (client_name, contact_number, email, pickup_datetime, return_datetime, vehicle.vehicle_id, fee))

        # After inserting, return the last inserted reservation ID
        reservation_id = self.db.cursor.lastrowid
        return reservation_id


    def make_rent(self):
        """Handle the reservation process"""
        print("\n")
        print("**************************************************\n\t     FILLING UP RENTAL FORM\n**************************************************\n")
    
        # Collecting client details
        client_name = input("Enter client name: ")
        contact_number = int(input("Enter contact number: "))
        email = input("Enter email: ")
        print("-" * 50)
        pickup_datetime = input("Enter pick-up date and time (YYYY-MM-DD HH:MM AM/PM): ")
        return_datetime = input("Enter return date and time (YYYY-MM-DD HH:MM AM/PM): ")

        # Fetch all vehicles (whether available or not)
        vehicles_data = self.db.fetch_all("SELECT id, type, model, plate_number, available, daily_rate FROM vehicles")
        vehicles = [Vehicle(*vehicle_data) for vehicle_data in vehicles_data]

        if not vehicles:
            print("No vehicles found.")
            return

        # Show all vehicles to the user
        print("-" * 100)
        print(f"\n======================================== AVAILABLE VEHICLES ========================================")
        self.print_vehicle_table(vehicles)

        # Choose vehicle to rent
        vehicle_id = int(input("\nSelect a vehicle by ID: "))
        selected_vehicle = next((v for v in vehicles if v.vehicle_id == vehicle_id), None)

        if not selected_vehicle:
            print("Invalid vehicle ID.")
            return

        if not selected_vehicle.available:
            print("This vehicle is currently reserved and cannot be rented.")
            return

        # Calculate rental duration
        days, hours = self.calculate_rental_duration(pickup_datetime, return_datetime)
        print(f"\nRental Duration: {days} days and {hours} hours")

        # Calculate rental fee
        rental_fee = self.calculate_rental_fee(selected_vehicle.daily_rate, days, hours)
        print(f"Rental Fee: ₱{rental_fee:,.2f}")

        # Collect payment and confirm reservation
        payment = float(input("Enter payment amount: "))
        change = payment - rental_fee
        print(f"Change: ₱{change:,.2f}")

        print("-" * 50)
        confirm = input("Do you want to proceed with the reservation? (yes/no): ").lower()
        if confirm == "yes":
            # Create reservation
            reservation_id = self.create_reservation(client_name, contact_number, email, pickup_datetime, return_datetime, selected_vehicle, rental_fee)
            print(f"Reservation confirmed. Your reservation ID is {reservation_id}.")
            selected_vehicle.mark_as_unavailable(self.db)
        print("\n")

        #DISPLAY OF RECEIPT
        self.display_rental_receipt(reservation_id, client_name, selected_vehicle, pickup_datetime, return_datetime, rental_fee, payment, change)

    def display_rental_receipt(self, reservation_id, client_name, vehicle, pickup_datetime, return_datetime, rental_fee, payment, change):
        """Display rental receipt after confirming the reservation"""
        print("\n" + "="*50)
        print(f"           SWIFtrent RENTAL RECEIPT")
        print("="*50)
        print(f"Reservation ID: {reservation_id}")
        print(f"Client Name: {client_name}")
        print("-" * 50)
        print(f"Vehicle: {vehicle.model} ({vehicle.plate_number})")
        print(f"Pick-up Date: {pickup_datetime}")
        print(f"Return Date: {return_datetime}")
        print("-" * 50)
        print(f"Rental Fee: ₱{rental_fee:,.2f}")
        print(f"Payment: ₱{payment:,.2f}")
        print(f"Change: ₱{change:,.2f}")
        print("="*50)
        print("Thank you for choosing SwiftRent. Safe Travels!")
        print("="*50 + "\n")


    def calculate_rental_duration(self, pickup_datetime, return_datetime):
        """Calculate rental duration in days and hours"""
        format_str = "%Y-%m-%d %I:%M %p"
        pickup_time = datetime.strptime(pickup_datetime, format_str)
        return_time = datetime.strptime(return_datetime, format_str)

        diff = return_time - pickup_time
        days = diff.days
        hours = diff.seconds // 3600
        return days, hours

    def calculate_rental_fee(self, daily_rate, days, hours):
        """Calculate rental fee based on duration"""
        rental_fee = daily_rate * days
        if hours > 0:
            rental_fee += daily_rate * (hours / 24)
        return rental_fee


    def cancel_rent(self):
        """Handle the cancellation of an existing reservation"""
        print("\n")
        print("**************************************************\n\t     CANCELLING RESERVATION\n**************************************************\n")
    
        # Ask for the reservation ID to cancel
        reservation_id = int(input("Enter the reservation ID to cancel: "))

        # Fetch the reservation details along with vehicle details
        reservation_data = self.db.fetch_all('''SELECT r.id, r.client_name, v.id AS vehicle_id, v.model, v.plate_number, r.fee
                                                FROM reservations r 
                                                JOIN vehicles v ON r.vehicle_id = v.id
                                                WHERE r.id = ?''', (reservation_id,))

        if not reservation_data:
            print("Reservation not found.")
            
            return

        # Extract reservation and vehicle details
        reservation = reservation_data[0]
        reservation_id, client_name, vehicle_id, vehicle_model, plate_number, fee = reservation

        # Show reservation details
        print(f"\nReservation Details:")
        print(f"ID: {reservation_id}")
        print(f"Client Name: {client_name}")
        print(f"Vehicle: {vehicle_model} ({plate_number})")
        print(f"Total Fee: ₱{fee:,.2f}")

        # Ask user for confirmation to cancel
        confirm = input(f"Are you sure you want to cancel this reservation (ID: {reservation_id})? (yes/no): ").lower()
        if confirm != 'yes':
            print("Cancellation aborted.")
            return

        # Cancel the reservation (delete from the database and mark vehicle as available)
    # Reset vehicle availability
        self.db.cursor.execute('''UPDATE vehicles SET available = ? WHERE id = ?''', (True, vehicle_id))  # Mark the vehicle as available again

    # Now, delete the reservation from the database
        self.db.cursor.execute('''DELETE FROM reservations WHERE id = ?''', (reservation_id,))

        # Fetch the vehicle object
        vehicle = Vehicle(vehicle_id, vehicle_model, plate_number, '', True, 0)  # Temporarily marking as available

        # Cancel the reservation (delete from the database and mark vehicle as available)
        reservation_obj = Reservation(reservation_id, client_name, '', '', '', '', vehicle, fee)
        reservation_obj.cancel(self.db)

        print(f"\nReservation {reservation_id} has been successfully cancelled.")
        print(f"The vehicle ({vehicle_model} - {plate_number}) is now available for rent.")
        print("\n")
    
    def see_all_reservations(self):
        """Display all reservations with their details"""
        print("\n================================================================= ALL RESERVATIONS ==================================================================")
        reservations_data = self.db.fetch_all('''SELECT r.id, r.client_name, v.model, v.plate_number, r.pickup_datetime, r.return_datetime, r.fee
                                                FROM reservations r
                                                JOIN vehicles v ON r.vehicle_id = v.id''')

        if not reservations_data:
            print("No reservations found.\n")
            return
        
        # Print reservation table headers
        print(f"{'ID':<5} {'Client Name':<20} {'Vehicle Model':<25} {'Plate Number':<20} {'Pickup':<25} {'Return':<25} {'Total Fee':<15}")
        print("-" * 150)

        for reservation in reservations_data:
            reservation_id, client_name, vehicle_model, plate_number, pickup, return_datetime, fee = reservation
            formatted_fee = f"₱{fee:,.2f}"
            print(f"{reservation_id:<5} {client_name:<20} {vehicle_model:<25} {plate_number:<20} {pickup:<25} {return_datetime:<25} {formatted_fee:<15}")
        print("\n")

    def update_reservation(self):
        """Update an existing reservation"""
        print("\n**************************************************\n\t  FILLING UP UPDATION RENTAL FORM\n**************************************************\n")

        # Ask for reservation ID to update
        reservation_id = int(input("Enter reservation ID to update: "))

        # Fetch reservation details
        reservation_data = self.db.fetch_all('''SELECT r.id, r.client_name, r.contact_number, r.email, r.pickup_datetime, r.return_datetime, v.model, v.plate_number, v.type, r.fee, v.id 
                                                FROM reservations r 
                                                JOIN vehicles v ON r.vehicle_id = v.id
                                                WHERE r.id = ?''', (reservation_id,))

        if not reservation_data:
            print("Reservation not found!")
            return

        # Extract reservation and vehicle details
        reservation = reservation_data[0]
        original_pickup = datetime.strptime(reservation[4], "%Y-%m-%d %I:%M %p")
        original_return = datetime.strptime(reservation[5], "%Y-%m-%d %I:%M %p")
        original_duration = (original_return - original_pickup).days, (original_return - original_pickup).seconds // 3600

        print(f"\nOriginal Pickup: {original_pickup} | Original Return: {original_return}")
        print(f"Original Duration: {original_duration[0]} days | {original_duration[1]} hours")

        # Ask if the user wants to retain the original pick-up and return dates
        print("-" * 80)
        retain_dates = input("Do you want to retain the original pick-up and return dates? (yes/no): ").lower()

        if retain_dates == "no":
            # Get new pick-up and return dates
            print("\n" + "-" * 80)
            new_pickup = input("Enter new pickup date and time (YYYY-MM-DD HH:MM AM/PM): ")
            new_return = input("Enter new return date and time (YYYY-MM-DD HH:MM AM/PM): ")

            # Convert to datetime objects
            new_pickup_datetime = datetime.strptime(new_pickup, "%Y-%m-%d %I:%M %p")
            new_return_datetime = datetime.strptime(new_return, "%Y-%m-%d %I:%M %p")

            # Calculate new rental duration
            new_duration = (new_return_datetime - new_pickup_datetime).days, (new_return_datetime - new_pickup_datetime).seconds // 3600

            # Extension fee calculation
            extension_fee = 0
            if new_duration[0] > original_duration[0]:
                extension_fee += (new_duration[0] - original_duration[0]) * 500  # ₱500 per extra day
            if new_duration[1] > original_duration[1]:
                extension_fee += (new_duration[1] - original_duration[1]) * 200  # ₱200 per extra hour

            print(f"\nNew Duration: {new_duration[0]} days, {new_duration[1]} hours")
            print(f"Extension Fee: ₱{extension_fee:,.2f}")
        else:
            # No change in dates, use original dates
            new_pickup_datetime = original_pickup
            new_return_datetime = original_return
            extension_fee = 0  # No extension fee if dates are unchanged

        # Ask if the user wants to keep the same vehicle
        print("-" * 80)
        keep_vehicle = input("Do you want to keep the same vehicle? (yes/no): ").lower()

        if keep_vehicle == "no":
            # Display available vehicles
            print("\n")
            self.see_all_vehicles()  # This should display all vehicles with availability
            new_vehicle_id = int(input("\nEnter the new vehicle ID: "))

            # Fetch the new vehicle details
            new_vehicle_data = self.db.fetch_all("SELECT id, type, model, plate_number, available, daily_rate FROM vehicles WHERE id = ?", (new_vehicle_id,))

            if not new_vehicle_data:
                print("Invalid vehicle ID.")
                return

            # Instantiate the new vehicle object
            new_vehicle = Vehicle(*new_vehicle_data[0])

            # Calculate vehicle change fee
            change_vehicle_fee = 200
            print(f"Vehicle Change Fee: ₱{change_vehicle_fee:,.2f}")

            # Calculate total fee (only additional fees: extension fee + vehicle change fee)
            total_fee = extension_fee + change_vehicle_fee

            # Mark the old vehicle as available again
            self.db.execute('''UPDATE vehicles SET available = 1 WHERE id = ?''', (reservation[10],))  # Make the old vehicle available

            # Mark the new vehicle as reserved
            self.db.execute('''UPDATE vehicles SET available = 0 WHERE id = ?''', (new_vehicle_id,))  # Mark the new vehicle as reserved
        else:
            #If keeping the same vehicle, no change fee
            new_vehicle = Vehicle(reservation[10], reservation[7], reservation[8], 0, reservation[9])  # Keep the original vehicle

            # Calculate total fee (only extension fee, no change fee)
            total_fee = extension_fee  # No additional change fee for keeping the same vehicle

        # Display only the total fee
        print(f"\nTotal Fee to Pay: ₱{total_fee:,.2f}")

        # Payment and change handling
        payment = float(input("Enter payment amount: "))

        if payment < total_fee:
            print("Insufficient payment. Please pay the full amount.")
            return

        change = payment - total_fee
        print(f"Change: ₱{change:,.2f}")

        # Update the reservation details in the database
        reservation_obj = Reservation(reservation[0], reservation[1], reservation[2], reservation[3], original_pickup, original_return, new_vehicle, total_fee)
        reservation_obj.update(self.db, new_pickup_datetime.strftime("%Y-%m-%d %I:%M %p"), new_return_datetime.strftime("%Y-%m-%d %I:%M %p"), new_vehicle, total_fee)

        # Display updated receipt
        self.display_updated_receipt(reservation_id, reservation, new_vehicle, new_pickup_datetime, new_return_datetime, total_fee)


    def display_updated_receipt(self, reservation_id, reservation, new_vehicle, new_pickup_datetime, new_return_datetime, total_fee):
        """Display rental receipt after confirming the reservation"""
        print("\n" + "="*50)
        print(f"           SwiftRent RENTAL RECEIPT")
        print("="*50)
        print(f"Reservation ID: {reservation_id}")
        print(f"Client Name: {reservation[1]}")
        print("-" * 50)
        print(f"Vehicle: {new_vehicle.model} ({new_vehicle.plate_number})")
        print(f"Pick-up Date: {new_pickup_datetime.strftime('%Y-%m-%d %I:%M %p')}")
        print(f"Return Date: {new_return_datetime.strftime('%Y-%m-%d %I:%M %p')}")
        print(f"Total Fee: ₱{total_fee:,.2f}")
        print("-" * 50)
        print("Thank you for choosing SwiftRent. Safe Travels!")
        print("="*50 + "\n")


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
            rental_system.update_reservation()  # Call the method to update reservation
        elif choice == '5':
            rental_system.see_all_vehicles()  # View all vehicles, available or not
        elif choice == '6':
            rental_system.see_all_reservations()  # This method will display all reservations (already implemented)
        elif choice == '7':
            print("\n===== Thank you for being with SwiftRent: Vehicle Rental Services. Safe Travels! =====")
            break  # Exit the application
        else:
            print("Invalid choice. Please try again.")

