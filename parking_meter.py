class ParkingMeter:
    def __init__(self, minutes_purchased=60):
        #Private
        self._minutes_purchased = 0
        self.minutes_purchased = minutes_purchased

    @property
    def minutes_purchased(self):
        #Getter
        return self._minutes_purchased

    @minutes_purchased.setter
    def minutes_purchased(self, minutes):
        #Setter
        if minutes <= 0:
            raise ValueError("Minutes purchased has to be positive.")
        self._minutes_purchased = minutes

    def __str__(self):
        return f"Minutes Purchased: {self._minutes_purchased}"



