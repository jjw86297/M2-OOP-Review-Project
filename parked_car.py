class ParkedCar:
    def __init__(self, make, model, color, license_number, minutes_parked=60):
        #Public
        self.make = make
        self.model = model
        self.color = color
        self.license_number = license_number
        #Private
        self._minutes_parked = 0
        self.minutes_parked = minutes_parked

    @property
    def minutes_parked(self):
        #Getter
        return self._minutes_parked

    @minutes_parked.setter
    def minutes_parked(self, minutes):
        #Setter
        if minutes <= 0:
            raise ValueError("Minutes parked has to be positive.")
        self._minutes_parked = minutes

    def __str__(self):
        return (f"{self.make} {self.model}, Color: {self.color}, "
                f"License: {self.license_number}, Minutes Parked: {self.minutes_parked}")