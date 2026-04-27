class BMW:
    def fuel_type(self):
        print("BMW: Uses Petrol or Diesel.")

    def max_speed(self):
        print("BMW: Max speed is 250 km/h.")

class Ferrari:
    def fuel_type(self):
        print("Ferrari: Uses High-Octane Petrol.")

    def max_speed(self):
        print("Ferrari: Max speed is 340 km/h.")

# Demonstrating Polymorphism
def display_car_info(car):
    car.fuel_type()
    car.max_speed()

# Create instances
bmw_car = BMW()
ferrari_car = Ferrari()

# Iterate through different objects using the same interface
for car in (bmw_car, ferrari_car):
    display_car_info(car)
    print("-" * 30)