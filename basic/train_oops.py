class Train:
    def __init__(self, train_number, train_name, total_seats):  # Constructor
        self.train_number = train_number  # Train number
        self.train_name = train_name  # Train name
        self.total_seats = total_seats  # Total seats available
        self.booked_seats = 0  # Initially, no seats are booked

    def show_train_details(self):  # Display train details
        print(f"Train Number: {self.train_number}")
        print(f"Train Name: {self.train_name}")
        print(f"Total Seats: {self.total_seats}")
        print(f"Available Seats: {self.get_available_seats()}")

    def get_available_seats(self):  # Calculate available seats
        return self.total_seats - self.booked_seats

    def book_ticket(self, seats):  # Book tickets
        if seats <= 0:
            print("Invalid number of seats.")
        elif seats > self.get_available_seats():
            print(f"Only {self.get_available_seats()} seats are available.")
        else:
            self.booked_seats += seats
            print(f"{seats} ticket(s) successfully booked. Remaining seats: {self.get_available_seats()}")

    def cancel_ticket(self, seats):  # Cancel tickets
        if seats <= 0:
            print("Invalid number of seats.")
        elif seats > self.booked_seats:
            print(f"Cannot cancel {seats} seats as only {self.booked_seats} seat(s) are booked.")
        else:
            self.booked_seats -= seats
            print(f"{seats} ticket(s) successfully canceled. Remaining seats: {self.get_available_seats()}")

# Example Usage
train = Train(12345, "Rajdhani Express", 100)

print("\n------- Train Details -------")
train.show_train_details()

print("\n------- Booking Tickets -------")
train.book_ticket(59)
train.book_ticket(34)
train.book_ticket(95)  # Attempt to overbook

print("\n------- Canceling Tickets -------")
train.cancel_ticket(21)
train.cancel_ticket(80)  # Attempt to cancel more tickets than booked

print("\n------- Final Train Details -------")
train.show_train_details()