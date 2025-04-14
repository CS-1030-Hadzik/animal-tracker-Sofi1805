
if __name__ == "__main__":
    # TODO: Create an instance of the Animal class
    animalInstanceJonJon = Animal(name='JonJon', species='Black Bear')
        
    # TODO: Print the Animal instance
    print(animalInstanceJonJon)
    # TODO: Call the method to make a generic animal sound
    print(animalInstanceJonJon.speak())
    # TODO: Create an instance of the Dog class
    animalInstanceAddy = Animal(name='Addy', species='dog')
    # TODO: Print the Dog instance
    print(animalInstanceAddy)
    # TODO: Call the method to make the dog-specific sound
    print(animalInstanceAddy.speak())

    # TODO print out all the animals
    for animal in Animal.all_animals:
        print(animal)