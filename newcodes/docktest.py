class Cat:
    def speak(self):
        print("meow!")

class Dog:
    def speak(self):
        print("woof!")

class Bob:
    def bow(self):
        print("thank you, thank you!")
    def speak(self):
        print("hello, welcome to the neighborhood!")
    def drive(self):
        print("beep, beep!")

def command(pet):
    pet.speak()

pets = [ Cat(), Dog(), Bob() ]

for pet in pets:
    command(pet)
