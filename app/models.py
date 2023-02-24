""" Implements a class diagram for an ordering system"""


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.phone = None
        self.email = email
        self.address = None

    def set_phone(self, phone):
        self.phone = phone 
        
    def set_email(self, email):
        self.email = email
        
    def set_address(self, address):
        self.address = address

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    def get_address(self):
        return self.address

class Item:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def set_price(self, price):
        self.price = price

    def set_category(self, category):
        self.category = category

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_category(self):
        return self.category

class Order:
    def __init__(self, customer, items, date):
        self.customer = customer
        self.items = items
        self.date = date

    def total(self):
        return sum(item.get_price() for item in self.items)

    def set_customer(self, customer):
        self.customer = customer

    def set_items(self, items):
        self.items = items

    def set_date(self, date):
        self.date = date

    def get_customer(self):
        return self.customer

    def get_items(self):
        return self.items
        
    def get_date(self):
        return self.date


class Payment:
    def __init__(self, order, amount, date):
        self.order = order
        self.amount = amount
        self.date = date

    def set_order(self, order):
        self.order = order

    def set_amount(self, amount):
        self.amount = amount

    def set_date(self, date):
        self.date = date

    def get_order(self):
        return self.order

    def get_amount(self):
        return self.amount

    def get_date(self):
        return self.date


customer = Customer("John Smith", "johnsmith@gmail.com")
customer.set_phone("555-555-5555")
customer.set_address("123 Main St.")
item1 = Item("Phone", 800, "Electronics")
item2 = Item("Shirt", 20, "Clothing")
item3 = Item("Shoes", 100, "Shoes")
order = Order(customer, [item1, item2, item3], "2022-01-01")
payment = Payment(order, order.total(), "2022-01-02")


# Print information to the command line
print(f"Customer: {customer.get_name()}")
print(f"Email: {customer.get_email()}")
print(f"Phone: {customer.get_phone()}")
print(f"Address: {customer.get_address()}")
print(f"Order Total: ${order.total()}")
print(f"Payment: ${payment.get_amount()} on {payment.get_date()}")