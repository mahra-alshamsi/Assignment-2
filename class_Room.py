class Room:
    """Class to represent a room in the hotel system."""

    def __init__(self, room_number, room_type, amenities, price_per_night, availability_status="available"):
        #Initialize a room with its details.

        self.__room_number = room_number
        self.__room_type = room_type
        self.__amenities = amenities
        self.__price_per_night = price_per_night
        self.__availability_status = availability_status

    def __str__(self):
        #Returns a string representation of the room.
        return f"Room {self.__room_number} ({self.__room_type}) - Price: {self.__price_per_night} - Availability: {self.__availability_status}"

    #Setter Getter Methods
    def get_room_number(self):
        return self.__room_number

    def get_room_type(self):
        return self.__room_type

    def get_amenities(self):
        return self.__amenities

    def get_price_per_night(self):
        return self.__price_per_night

    def check_availability(self, check_in_date, check_out_date):
        #Check if the room is available for the specified dates.
        return self.__availability_status == "available"

    def update_room_status(self, status):
        #Update the availability status of the room.
        self.__availability_status = status
