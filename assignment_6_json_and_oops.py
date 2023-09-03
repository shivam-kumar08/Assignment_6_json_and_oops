class Dog:

    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")


class Chihuahua(Dog):
    def __init__(self, name, age, coat_color, size):
        super().__init__(name, age, coat_color)
        self.size = size

    def bark(self):
        print(f"{self.name} the Chihuahua says: Woof, woof!")

    def play_fetch(self):
        print(f"{self.name} loves to play fetch with tiny toys.")


class Terrier(Dog):
    def __init__(self, name, age, coat_color, energy_level):
        super().__init__(name, age, coat_color)
        self.energy_level = energy_level

    def dig_holes(self):
        print(f"{self.name} the Terrier is digging a hole in the yard.")

    def agility_training(self):
        print(f"{self.name} enjoys agility training to burn off energy.")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, drool_level):
        super().__init__(name, age, coat_color)
        self.drool_level = drool_level

    def snore(self):
        print(f"{self.name} the Bulldog is snoring loudly.")

    def eat_snacks(self):
        print(f"{self.name} loves to eat tasty snacks.")

chihuahua = Chihuahua("Leo", 2, "Brown", "Small")
terrier = Terrier("Max", 3, "White", "High")
bulldog = Bulldog("Rocky", 4, "Brindle", "Moderate")

chihuahua.description()
chihuahua.get_info()
chihuahua.bark()
chihuahua.play_fetch()

terrier.description()
terrier.get_info()
terrier.dig_holes()
terrier.agility_training()

bulldog.description()
bulldog.get_info()
bulldog.snore()
bulldog.eat_snacks()
