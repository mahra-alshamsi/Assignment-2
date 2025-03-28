from class_Guest import Guest
from class_Room import Room
from class_Booking import Booking
from class_Invoice import Invoice
from class_Payment import Payment
from class_LoyaltyProgram import LoyaltyProgram
from class_GuestInteraction import GuestInteraction


def get_input(prompt, cast_type=str, required=True, numeric_only=False):
    """Handles user input with error checking, ensuring non-empty values and numeric validation when needed."""
    while True:
        value = input(prompt).strip()

        if required and not value:
            print("Input cannot be empty. Please provide a value.")
            continue

        if numeric_only and not value.isdigit():
            print("Invalid input. Please enter only numbers.")
            continue

        try:
            return cast_type(value)
        except ValueError:
            print(f"Invalid input. Please enter a valid {cast_type.__name__} value.")


def create_guest_account():
    """Create a guest account."""
    try:
        guest = Guest(
            name=get_input("Enter guest name: "),
            email=get_input("Enter guest email: "),
            contact=get_input("Enter guest contact number: ", str, numeric_only=True),
            loyalty_status=get_input("Enter loyalty status (e.g., Silver, Gold, None): ")
        )
        print(f"Guest account created successfully: {guest.__dict__}")
    except Exception as e:
        print(f"Error creating guest account: {e}")


def search_for_available_rooms():
    """Search for available rooms."""
    try:
        room = Room(
            "101",
            get_input("Enter room type (e.g., Single, Double, Suite): "),
            get_input("Enter amenities (comma-separated): ").split(","),
            get_input("Enter price per night: ", float)
        )
        check_in = get_input("Enter check-in date (YYYY-MM-DD): ")
        check_out = get_input("Enter check-out date (YYYY-MM-DD): ")
        print(
            f"Room {room.get_room_number()} is {'available' if room.check_availability(check_in, check_out) else 'not available'}."
        )
    except Exception as e:
        print(f"Error during room search: {e}")


def make_room_reservation():
    """Make a room reservation."""
    try:
        booking = Booking(
            booking_id=get_input("Enter booking ID: "),
            guest=Guest(get_input("Enter guest name: "), "email@example.com",
                        get_input("Enter guest contact number: ", str, numeric_only=True), "Gold"),
            room=Room(get_input("Enter room number: "), "Single", ["WiFi", "AC"], 100),
            check_in_date=get_input("Enter check-in date (YYYY-MM-DD): "),
            check_out_date=get_input("Enter check-out date (YYYY-MM-DD): ")
        )
        print(f"Booking successful: {booking}")
    except Exception as e:
        print(f"Error making reservation: {e}")


def generate_invoice():
    """Generate an invoice."""
    try:
        invoice_id = get_input("Enter invoice ID: ")
        nightly_rate = get_input("Enter nightly rate: ", float)
        additional_charges = get_input("Enter additional charges: ", float)
        discounts = get_input("Enter discounts: ", float)

        invoice = Invoice(
            invoice_id=invoice_id,
            nightly_rate=nightly_rate,
            additional_charges=additional_charges,
            discounts=discounts
        )
        total_amount = invoice.calculate_total_amount()
        print(f"Invoice ID: {invoice_id}, Total Amount: {total_amount:.2f}")
    except Exception as e:
        print(f"Error generating invoice: {e}")


def process_payment():
    """Process a payment."""
    try:
        payment = Payment(
            payment_id=get_input("Enter payment ID: "),
            payment_method=get_input("Enter payment method (Credit Card, PayPal, etc.): "),
            payment_amount=get_input("Enter payment amount: ", float)
        )
        print(payment.process_payment())
        print(payment.generate_receipt())
    except Exception as e:
        print(f"Error processing payment: {e}")


def cancel_reservation():
    """Cancel a reservation."""
    try:
        booking_id = get_input("Enter booking ID to cancel: ")
        room = Room(get_input("Enter room number: "), "Single", ["WiFi", "AC"], 100)
        room.update_room_status("available")
        print(f"Booking {booking_id} canceled. Room {room.get_room_number()} is now available.")
    except Exception as e:
        print(f"Error canceling reservation: {e}")


def main():
    options = {
        "1": create_guest_account,
        "2": search_for_available_rooms,
        "3": make_room_reservation,
        "4": generate_invoice,
        "5": process_payment,
        "6": cancel_reservation,
        "0": exit
    }

    while True:
        print("\nHotel Management System")
        print("1. Create Guest Account")
        print("2. Search for Available Rooms")
        print("3. Make Room Reservation")
        print("4. Generate Invoice")
        print("5. Process Payment")
        print("6. Cancel Reservation")
        print("0. Exit")

        choice = input("Enter your choice: ")
        action = options.get(choice, lambda: print("Invalid choice, please try again."))
        action()


if __name__ == "__main__":
    main()
