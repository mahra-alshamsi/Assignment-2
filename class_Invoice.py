class Invoice:
    """Class to represent an invoice for a booking."""

    def __init__(self, invoice_id, nightly_rate, additional_charges, discounts):
        #Initialize the invoice with charges.

        self.__invoice_id = invoice_id
        self.__nightly_rate = nightly_rate
        self.__additional_charges = additional_charges
        self.__discounts = discounts
        self.__total_amount = self.calculate_total_amount()  #Calculate total

    def calculate_total_amount(self):
        base_amount = self.__nightly_rate + self.__additional_charges
        self.__total_amount = base_amount - self.__discounts  #Ensure discount is applied
        return self.__total_amount

    def apply_discounts(self):
        self.__total_amount *= 0.9 if self.__discounts > 0 else 1  #Apply 10% discount if applicable
        return self.__total_amount

    def __str__(self):
        #Return a string representation of the invoice.
        return f"Invoice ID: {self.__invoice_id}, Total Amount: {self.__total_amount}"
