from datetime import datetime
from vehicle import Vehicle
from reservation import Reservation

class VehicleRental:
    def __init__(self, db):
        self.db = db

    def show_dashboard(self):
        print("\n==================== Vehicle Rental System ====================")
        print("1. View Company Information")
        print("2. Make Reservation")
        print("3. Cancel Reservation")
        print("4. Update Reservation")
        print("5. View All Vehicles")
        print("6. View All Reservations")
        print("7. Exit")
        print("===============================================================")

    def see_company_information(self):
        print("Company Name: SwiftRent\nContact: info@swiftrent.com")

    def make_rent(self):
        print("Reservation Form")

    def cancel_rent(self):
        """Handle the cancellation of an existing reservation"""
        print("\nCANCELLING RESERVATION")
        reservation_id = int(input("Enter the reservation ID to cancel: "))
        reservation_data = self.db.fetch_all('''SELECT r.id, r.client_name, v.id AS vehicle_id, v.model, v.plate_number, r.fee
                                                FROM reservations r 
                                                JOIN vehicles v ON r.vehicle_id = v.id
                                                WHERE r.id = ?''', (reservation_id,))
        if not reservation_data:
            print("Reservation not found.")
            return
        reservation = reservation_data[0]
        reservation_id, client_name, vehicle_id, vehicle_model, plate_number, fee = reservation

        # Ask for confirmation to cancel
        confirm = input(f"Are you sure you want to cancel this reservation (ID: {reservation_id})? (yes/no): ").lower()
        if confirm != 'yes':
            print("Cancellation aborted.")
            return

        self.db.execute('''UPDATE vehicles SET available = ? WHERE id = ?''', (True, vehicle_id))
        self.db.execute('''DELETE FROM reservations WHERE id = ?''', (reservation_id,))

        # Create a vehicle object for the cancelled reservation
        vehicle = Vehicle(vehicle_id, vehicle_model, plate_number, '', True, 0)  # Temporarily mark as available
        reservation_obj = Reservation(reservation_id, client_name, '', '', '', '', vehicle, fee)
        reservation_obj.cancel(self.db)

        print(f"\nReservation {reservation_id} has been successfully cancelled.")

    def see_all_reservations(self):
        """Display all reservations with their details"""
        reservations_data = self.db.fetch_all('''SELECT r.id, r.client_name, v.model, v.plate_number, r.pickup_datetime, r.return_datetime, r.fee
                                                FROM reservations r
                                                JOIN vehicles v ON r.vehicle_id = v.id''')
        if not reservations_data:
            print("No reservations found.\n")
            return
        print(f"{'ID':<5} {'Client Name':<20} {'Vehicle Model':<25} {'Plate Number':<20} {'Pickup':<25} {'Return':<25} {'Total Fee':<15}")
        print("-" * 150)
        for reservation in reservations_data:
            reservation_id, client_name, vehicle_model, plate_number, pickup, return_datetime, fee = reservation
            formatted_fee = f"₱{fee:,.2f}"
            print(f"{reservation_id:<5} {client_name:<20} {vehicle_model:<25} {plate_number:<20} {pickup:<25} {return_datetime:<25} {formatted_fee:<15}")
        print("\n")
    
    def update_reservation(self):
        """Update an existing reservation"""
        print("\nFILLING UP UPDATION RENTAL FORM")
        reservation_id = int(input("Enter reservation ID to update: "))
        reservation_data = self.db.fetch_all('''SELECT r.id, r.client_name, r.contact_number, r.email, r.pickup_datetime, r.return_datetime, v.model, v.plate_number, v.type, r.fee, v.id 
                                                FROM reservations r 
                                                JOIN vehicles v ON r.vehicle_id = v.id
                                                WHERE r.id = ?''', (reservation_id,))
        if not reservation_data:
            print("Reservation not found!")
            return

        reservation = reservation_data[0]
        original_pickup = datetime.strptime(reservation[4], "%Y-%m-%d %I:%M %p")
        original_return = datetime.strptime(reservation[5], "%Y-%m-%d %I:%M %p")
        original_duration = (original_return - original_pickup).days, (original_return - original_pickup).seconds // 3600

        print(f"Original Pickup: {original_pickup} | Original Return: {original_return}")
        print(f"Original Duration: {original_duration[0]} days | {original_duration[1]} hours")
        # Continue updating reservation logic here...

