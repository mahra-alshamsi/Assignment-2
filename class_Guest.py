class Guest:
    """Class to represent a guest in the hotel."""
    def __init__(self, name, email, contact, loyalty_status, loyalty_points=0):
        self.__name = name
        self.__email = email
        self.__contact = contact
        self.__loyalty_status = loyalty_status
        self.__loyalty_points = loyalty_points  # Ensure loyalty_points is initialized

    def __str__(self):
        return f"Guest(name={self.__name}, email={self.__email}, contact={self.__contact}, loyalty_status={self.__loyalty_status}, loyalty_points={self.__loyalty_points})"

    #Setter Getter Methods
    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_contact(self):
        return self.__contact

    def get_loyalty_status(self):
        return self.__loyalty_status

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_contact(self, contact):
        self.__contact = contact

    def set_loyalty_status(self, loyalty_status):
        self.__loyalty_status = loyalty_status

    def get_loyalty_points(self):
        return self.__loyalty_points

    def set_loyalty_points(self, points):
        self.__loyalty_points = points
