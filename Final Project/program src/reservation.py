class Reservation:
    def __init__(self, reservation_id, client_name, contact_number, email, pickup_datetime, return_datetime, vehicle, fee):
        self.id = reservation_id
        self.client_name = client_name
        self.contact_number = contact_number
        self.email = email
        self.pickup_datetime = pickup_datetime
        self.return_datetime = return_datetime
        self.vehicle = vehicle
        self.fee = fee

    def cancel(self, db):
        """Cancel the reservation in the database."""
        db.execute("DELETE FROM reservations WHERE id = ?", (self.id,))
        print(f"Reservation {self.id} cancelled.")

    def update(self, db, new_pickup_datetime, new_return_datetime, new_vehicle, total_fee):
        """Update the reservation details in the database."""
        db.execute('''UPDATE reservations
                      SET pickup_datetime = ?, return_datetime = ?, vehicle_id = ?, fee = ?
                      WHERE id = ?''',
                   (new_pickup_datetime, new_return_datetime, new_vehicle.id, total_fee, self.id))
        print(f"Reservation {self.id} updated.")
