class LoyaltyProgram:
    def __init__(self, program_id, points_required, reward_details):
        self.__program_id = program_id
        self.__points_required = points_required
        self.__reward_details = reward_details

    #Getter methods
    def get_program_id(self):
        return self.__program_id

    def get_points_required(self):
        return self.__points_required

    def get_reward_details(self):
        return self.__reward_details

    def redeem_points(self, points):
        if points >= self.__points_required:
            return f"Redeeming {points} points for {self.__reward_details}."
        else:
            return "Not enough points for redemption."

    def check_eligibility(self, guest):
        #Check if guest has enough loyalty points
        return guest.get_loyalty_points() >= self.__points_required

    def update_points(self, guest):
        #Update guest's loyalty points based on loyalty status or other logic
        if guest.get_loyalty_status() == "Gold":
            guest.set_loyalty_points(200)  #updating points
        elif guest.get_loyalty_status() == "Silver":
            guest.set_loyalty_points(100)
        else:
            guest.set_loyalty_points(50)
        return f"Updated loyalty points for guest {guest.get_name()}."
