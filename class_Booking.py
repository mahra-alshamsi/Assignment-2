from class_Room import Room
from class_Guest import Guest

class Booking:
    """Class to represent a booking made by a guest for a room. """

    def __init__(self, booking_id, guest, room, check_in_date, check_out_date):
        #Initialize a booking with guest, room, and dates.
        self.__booking_id = booking_id
        self.__guest = guest
        self.__room = room
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date

    def get_guest(self):
        return self.__guest

    def __str__(self):
        #Returns a string representation of the booking.
        return f"Booking ID: {self.__booking_id}, Guest: {self.__guest.get_name()}, Room: {self.__room.get_room_number()}"

    def generate_invoice(self):
        #Generate an invoice for the booking.
        return f"Invoice generated for booking ID: {self.__booking_id}"

    def send_booking_confirmation(self):
        #Send a confirmation email or notification to the guest.
        return f"Booking confirmed for {self.__guest.get_name()} in Room {self.__room.get_room_number()}."
