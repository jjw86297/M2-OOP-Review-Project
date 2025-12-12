from parked_car import ParkedCar
from parking_meter import ParkingMeter
from police_officer import PoliceOfficer

def run_scenario(title):
    print("\n")
    print(title)

#Scenario: Car Parked Legally
run_scenario("Scenario: Car Parked Legally")

car1= ParkedCar("Toyota", "Camry", "Red", "XYZ123", 30)
meter1= ParkingMeter(40)
officer1 = PoliceOfficer("John Doe", "5678")

ticket = officer1.inspect_car(car1, meter1)
if ticket is None:
    print("Car is parked legally.")
else:
    print(ticket)

#Scenario: Less Than 1 Hour Over Time
run_scenario("Scenario: Car Illegally Parked Less Than 1 Hour Over")

car2 = ParkedCar("Honda", "Accord", "Blue", "ABC987", 70)
meter2 = ParkingMeter(60)
officer2 = PoliceOfficer("Jane Smith", "1234")

ticket = officer2.inspect_car(car2, meter2)
if ticket:
    print(ticket)

#Scenario: Multiple Hours Over Time
run_scenario("Scenario: Car Illegally Parked Multiple Hours Over")

car3 = ParkedCar("Ford", "Mustang", "Black", "LMN456", 190)
meter3 = ParkingMeter(60)
officer3 = PoliceOfficer("James Brown", "4321")

ticket = officer3.inspect_car(car3, meter3)
if ticket:
    print(ticket)

#Scenario: Multiple Cars in a Parking Lot
run_scenario("Scenario: Multiple Cars in a Parking Lot")

officer4= PoliceOfficer("Sarah Green", "9999")

cars = [
(ParkedCar("Nissan", "Altima", "White", "JKL321", 60), ParkingMeter(60)),
(ParkedCar("Chevy", "Malibu", "Silver", "QWE789", 80), ParkingMeter(60)),
(ParkedCar("BMW", "X5", "Black", "BMW999", 500), ParkingMeter(60)),
(ParkedCar("Mazda", "3", "Blue", "MAZ321", 45), ParkingMeter(60)),
]

for car, meter in cars:
    ticket = officer4.inspect_car(car, meter)
    if ticket:
        print(ticket)
    else:
        print(f"No ticket for {car.license_number}: Car is parked legally.")
