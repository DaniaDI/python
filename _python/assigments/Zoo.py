class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Happiness: {self.happiness}")
        print("-" * 20)
        return self

    def feed(self):
        self.health += 10
        self.happiness += 10
        return self
                    
 

        