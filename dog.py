class Dog:
    
    animal = "Canine"

    def __init__(self, breed, colour):
        
        self.breed = breed
        self.colour = colour

    def display_details(self):
        print(f"Type: {Dog.animal}")
        print(f"Breed: {self.breed}")
        print(f"Colour: {self.colour}")
        print("-" * 20)

# Creating two different objects for different breeds
dog1 = Dog("German Shepherd", "Black and Tan")
dog2 = Dog("Labrador", "Golden")

# Displaying the details
print("Details of Dog 1:")
dog1.display_details()

print("Details of Dog 2:")
dog2.display_details()