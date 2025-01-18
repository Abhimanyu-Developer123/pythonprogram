class Mobile:
    def __init__(self, brand, model, price):  # Constructor
        self.brand = brand  # Brand of the mobile
        self.model = model  # Model of the mobile
        self.price = price  # Price of the mobile

    def show_details(self):  # Show details of the mobile
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ₹{self.price}")

    def apply_discount(self, percentage):  # Apply discount
        if 0 < percentage < 100:
            discount_amount = self.price * (percentage / 100)
            self.price -= discount_amount
            print(f"Discount of {percentage}% applied. New price: ₹{self.price}")
        else:
            print("Invalid discount percentage. It should be between 0 and 100.")

# Example Usage
mobile1 = Mobile("Samsung", "Galaxy S23", 80000)  # Create a mobile object
mobile2 = Mobile("Apple", "iPhone 14", 120000)

print("\n------------- Mobile 1 Details -------------")
mobile1.show_details()
mobile1.apply_discount(10)  # Apply 10% discount
mobile1.show_details()

print("\n-------------- Mobile 2 Details -------------")
mobile2.show_details()
mobile2.apply_discount(5)  # Apply 5% discount
mobile2.show_details()