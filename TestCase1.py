#Importing necessary classes
from class_Room import Room
from class_Guest import Guest
from class_Booking import Booking
from class_Invoice import Invoice
from class_Payment import Payment
from class_LoyaltyProgram import LoyaltyProgram
from class_GuestInteraction import GuestInteraction


def test_booking_system():
    #Test for Guest class
    guest = Guest(name="Mahra Alshamsi", email="202312983@zu.ac.ae", contact="1234567890", loyalty_status="Gold",
                  loyalty_points=150)

    #Test the getter methods
    assert guest.get_name() == "Mahra Alshamsi"
    assert guest.get_email() == "202312983@zu.ac.ae"
    assert guest.get_contact() == "1234567890"
    assert guest.get_loyalty_status() == "Gold"
    assert guest.get_loyalty_points() == 150  # Test that loyalty points are set properly

    #Test the getter methods
    print(f"Testing Guest Class (initial state):")
    print(f"Name: {guest.get_name()}")
    print(f"Email: {guest.get_email()}")
    print(f"Contact: {guest.get_contact()}")
    print(f"Loyalty Status: {guest.get_loyalty_status()}")
    print(f"Loyalty Points: {guest.get_loyalty_points()}")
    print()

    #Test the setter methods
    guest.set_name("Sara Saif")
    guest.set_email("SaraSaif@gmail.com")
    guest.set_contact("0987654321")
    guest.set_loyalty_status("Silver")
    guest.set_loyalty_points(120)

    assert guest.get_name() == "Sara Saif"
    assert guest.get_email() == "SaraSaif@gmail.com"
    assert guest.get_contact() == "0987654321"
    assert guest.get_loyalty_status() == "Silver"
    assert guest.get_loyalty_points() == 120  # Test updated loyalty points

    print(f"Testing Guest Class (after updates):")
    print(f"Updated Name: {guest.get_name()}")
    print(f"Updated Email: {guest.get_email()}")
    print(f"Updated Contact: {guest.get_contact()}")
    print(f"Updated Loyalty Status: {guest.get_loyalty_status()}")
    print(f"Updated Loyalty Points: {guest.get_loyalty_points()}")
    print()

    #Test for Room class
    room = Room(room_number="101", room_type="Single", amenities=["TV", "Wi-Fi"], price_per_night=100)

    print(f"Testing Room Class:")
    print(str(room))

    #Test getter methods
    print(f"Room Number: {room.get_room_number()}")
    print(f"Room Type: {room.get_room_type()}")
    print(f"Amenities: {room.get_amenities()}")
    print(f"Price per Night: {room.get_price_per_night()}")

    #Test check_availability
    print(f"Availability (check_availability): {room.check_availability('2025-04-01', '2025-04-07')}")
    print()

    #Test string representation
    assert str(room) == "Room 101 (Single) - Price: 100 - Availability: available"

    #Test getter methods
    assert room.get_room_number() == "101"
    assert room.get_room_type() == "Single"
    assert room.get_amenities() == ["TV", "Wi-Fi"]
    assert room.get_price_per_night() == 100

    #Test check_availability
    assert room.check_availability("2025-04-01", "2025-04-07") == True

    #Test for Booking class
    booking = Booking(booking_id=1, guest=guest, room=room, check_in_date="2025-04-01", check_out_date="2025-04-07")

    #Test string representation
    print(f"Testing Booking Class:")
    print(str(booking))

    #Test methods for generating invoice and sending booking confirmation
    print(f"Invoice Generation: {booking.generate_invoice()}")
    print(f"Booking Confirmation: {booking.send_booking_confirmation()}")
    print()

    #Test string representation
    assert str(booking) == "Booking ID: 1, Guest: Sara Saif, Room: 101"

    #Test methods for generating invoice and sending booking confirmation
    assert booking.generate_invoice() == "Invoice generated for booking ID: 1"
    assert booking.send_booking_confirmation() == "Booking confirmed for Sara Saif in Room 101."

    #Test for Invoice class
    invoice = Invoice(invoice_id=101, nightly_rate=100, additional_charges=50, discounts=20)

    #Test calculate_total_amount
    print(f"Testing Invoice Class:")
    print(f"Total Amount (without discounts): {invoice.calculate_total_amount()}")

    #Test apply_discounts
    print(f"Total Amount (after discounts): {invoice.apply_discounts()}")

    #Test string representation of Invoice
    print(f"Invoice String Representation: {str(invoice)}")
    print()

    #Test calculate_total_amount
    assert invoice.calculate_total_amount() == 130

    #Test apply_discounts
    assert invoice.apply_discounts() == 117

    #Test string representation of Invoice
    assert str(invoice) == "Invoice ID: 101, Total Amount: 117.0"

    #Test for Payment class
    payment = Payment(payment_id=202, payment_method="Credit Card", payment_amount=117)

    #Test processing payment and generating receipt
    print(f"Testing Payment Class:")
    print(f"Payment Processed: {payment.process_payment()}")
    print(f"Payment Receipt: {payment.generate_receipt()}")
    print()

    #Test processing payment and generating receipt
    assert payment.process_payment() == "Payment of 117 via Credit Card processed."
    assert payment.generate_receipt() == "Payment receipt: ID: 202, Amount: 117"

    #Test for LoyaltyProgram class
    loyalty_program = LoyaltyProgram(program_id=301, points_required=100, reward_details="Free Night Stay")

    #Test redeem_points method
    print(f"Testing LoyaltyProgram Class:")
    print(f"Redeem Points (150): {loyalty_program.redeem_points(150)}")
    print(f"Redeem Points (50): {loyalty_program.redeem_points(50)}")

    #Test check_eligibility method
    print(f"Eligibility for Guest: {loyalty_program.check_eligibility(guest)}")  # Will pass as points >= 100

    #Test update_points method
    print(f"Update Loyalty Points for Guest: {loyalty_program.update_points(guest)}")
    print()

    #Test redeem_points method
    assert loyalty_program.redeem_points(150) == "Redeeming 150 points for Free Night Stay."
    assert loyalty_program.redeem_points(50) == "Not enough points for redemption."

    #Test check_eligibility method
    assert loyalty_program.check_eligibility(guest) == True  # This will now pass because points >= 100

    #Test update_points method
    assert loyalty_program.update_points(guest) == "Updated loyalty points for guest Sara Saif."

    #Test for GuestInteraction class
    guest_interaction = GuestInteraction(guest, service_type="Room Service", service_description="Dinner", rating=5,
                                         review=" Best service!")

    #Test service request and feedback methods
    assert guest_interaction.request_service() == "Service request for Room Service by Sara Saif has been sent for action."
    assert guest_interaction.update_service_status("Completed") == "Service request for Room Service is now Completed."
    assert guest_interaction.submit_feedback() == "Feedback submitted by Sara Saif: Rating: 5, Review:  Best service!"
    assert guest_interaction.get_guest_feedback() == "Guest Feedback: Rating: 5, Review:  Best service!"

    #Test service request and feedback methods
    print(f"Testing GuestInteraction Class:")
    print(f"Service Request: {guest_interaction.request_service()}")
    print(f"Service Status Update: {guest_interaction.update_service_status('Completed')}")
    print(f"Feedback Submission: {guest_interaction.submit_feedback()}")
    print(f"Guest Feedback: {guest_interaction.get_guest_feedback()}")
    print()
    print("All tests passed successfully!")


#Run the test
test_booking_system()
