class Animal:
    def __init__(self, name, age, health_level, happiness_level):
        self.name = name
        self.age = age
        self.health = health_level
        self.happiness = happiness_level

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Happiness: {self.happiness}")
        
    def feed(self):
        self.health += 10
        self.happiness += 10
        
class Lion(Animal):
    def __init__(self, name):
        super().__init__(name,5,80,80)

    def feed(self):
        self.health += 15
        self.happiness += 5
            
class Tiger(Animal):
    def __init__(self, name):
        super().__init__(name,6,60,90)

    def feed(self):
        self.health += 10
        self.happiness += 15



class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
### in general############################
    def add_animal(self, animal):
        self.animals.append(animal)
############################################
    def add_lion(self, name):
        self.animals.append(Lion(name))
    def add_tiger(self, name):
        self.animals.append(Tiger(name))
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
            print("-"*60)
        

zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.add_animal(Lion("Simba"))
zoo1.add_animal(Tiger("Shere Khan"))
zoo1.print_all_info()


zoo2 = Animal('tiger',6,60,90)
zoo2.display_info()


        