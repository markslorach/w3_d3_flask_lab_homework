class Order():
    def __init__(self, customer_name, order_date, book_name, quantity, description):
        self.customer_name = customer_name
        self.order_date = order_date
        self.book_name = book_name
        self.quantity = quantity
        self.description = description