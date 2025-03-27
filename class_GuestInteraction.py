class GuestInteraction:
    """Class to handle both guest service requests and feedback submissions."""

    def __init__(self, guest, service_type=None, service_description=None, rating=None, review=None):
        self.guest = guest
        self.service_type = service_type
        self.service_description = service_description
        self.rating = rating
        self.review = review
        self.service_status = "Pending"

    #Guest Service Request Methods
    def request_service(self):
        #Send the service request to the relevant hotel staff.
        if self.service_type and self.service_description:
            return f"Service request for {self.service_type} by {self.guest.get_name()} has been sent for action."
        return "No service requested."

    def update_service_status(self, status):
        #Update the status of the service request.
        if self.service_type:
            self.service_status = status
            return f"Service request for {self.service_type} is now {self.service_status}."
        return "No service request to update."

    #Feedback Methods
    def submit_feedback(self):
        #Submit feedback and save the review.
        if 1 <= self.rating <= 5:
            return f"Feedback submitted by {self.guest.get_name()}: Rating: {self.rating}, Review: {self.review}"
        else:
            return "Invalid rating. Please provide a rating between 1 and 5."

    def get_guest_feedback(self):
        #Retrieve guest feedback.
        if self.rating and self.review:
            return f"Guest Feedback: Rating: {self.rating}, Review: {self.review}"
        return "No feedback provided."

    def __str__(self):
        #Return a string representation of the guest interaction.
        service_info = f"Service Request: {self.service_type} - {self.service_description}" if self.service_type else "No service request."
        feedback_info = f"Feedback: {self.rating} stars - {self.review}" if self.rating else "No feedback submitted."
        return f"{service_info}\n{feedback_info}"
