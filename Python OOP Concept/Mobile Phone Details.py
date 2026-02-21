class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def apply_discount(self, discount_amount):
        if discount_amount > 0:
            if discount_amount <= self.price:
                self.price -= discount_amount
                print(f"Discount of ${discount_amount} applied successfully.")
            else:
                print("Discount amount cannot be greater than the price.")
        else:
            print("Discount amount must be positive.")

    def display_mobile(self):
        print("Mobile Details:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price}")


# Create an object and call methods
mobile1 = Mobile("Apple", "iPhone 15", 1200)

mobile1.display_mobile()
mobile1.apply_discount(200)
mobile1.display_mobile()