class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting hunger level
        self.happiness = 5  # Starting happiness level
        self.health = 10  # Starting health level

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 1
            print(f"{self.name} has been fed. Hunger level is now {self.hunger}.")
        else:
            print(f"{self.name} is not hungry!")

    def play(self):
        if self.happiness < 10:
            self.happiness += 1
            print(f"{self.name} played! Happiness level is now {self.happiness}.")
        else:
            print(f"{self.name} is already very happy!")

    def check_status(self):
        print(f"{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Happiness: {self.happiness}/10")
        print(f"Health: {self.health}/10")

    def pass_time(self):
        """Simulate the passing of time, affecting the pet's attributes."""
        self.hunger += 1
        self.happiness -= 1
        if self.hunger > 10:
            self.hunger = 10
            self.health -= 1
            print(f"{self.name} is very hungry! Health decreases.")
        if self.happiness < 0:
            self.happiness = 0
            self.health -= 1
            print(f"{self.name} is sad! Health decreases.")

    def get_health_status(self):
        if self.health <= 0:
            print(f"{self.name} has passed away. :(")
        else:
            print(f"{self.name} is alive and well!")

# Example usage:
if __name__ == "__main__":
    pet_name = input("What would you like to name your pet? ")
    my_pet = VirtualPet(pet_name)

    # Simulate some interactions
    my_pet.check_status()
    my_pet.feed()
    my_pet.play()
    my_pet.pass_time()
    my_pet.check_status()
    my_pet.get_health_status()
