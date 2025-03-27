class Payment:
    """Class to represent a payment for a booking."""

    def __init__(self, payment_id, payment_method, payment_amount):
        #Initialize a payment with details.
        self.__payment_id = payment_id
        self.__payment_method = payment_method
        self.__payment_amount = payment_amount

    def process_payment(self):
        #Process the payment and return a success message.
        return f"Payment of {self.__payment_amount} via {self.__payment_method} processed."

    def generate_receipt(self):
        #Generate a receipt for the payment.
        return f"Payment receipt: ID: {self.__payment_id}, Amount: {self.__payment_amount}"
