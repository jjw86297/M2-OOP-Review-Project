from parking_ticket import ParkingTicket

class PoliceOfficer:
    def __init__(self, name, badge_number):
        self.name = name
        self.badge_number = badge_number

    def inspect_car(self, parked_car, parking_meter):
        #Compares parked minutes to purchased meter time.
        parked = parked_car.minutes_parked
        purchased = parking_meter.minutes_purchased

        if parked > purchased:
            illegal_minutes = parked - purchased
            return ParkingTicket(parked_car, self, illegal_minutes)

        return None



