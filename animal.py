class Animal:
    """
    Base class representing a generic animal.
    """
    # Class-level attribute
    kingdom = "Animalia"
    # TODO create a class-level attribute that is a list of all the Animal objects

    # TODO create the initializer for Animal with name and species as attributs

    # TODO: Add a method to make a generic sound 
    # Call the method `speak` and make it output a specific message like 
    # "The animal makes a noise.""

    # TODO __str__ method for string representation
    # Example output
    # Kingdom: 'kingdom attribute', Name: 'name attribute' Species: 'species attribute' 

    all_animals = []  # Class-level attribute to store all Animal objects

    def __init__(self, name, species, kingdom='Animalia'):
        """
        Initializes an Animal object.

        Args:
            name (str): The name of the animal.
            species (str): The species of the animal.
            kingdom (str, optional): The kingdom of the animal. Defaults to 'Animalia'.
        """
        self.name = name
        self.species = species
        self.kingdom = kingdom
        Animal.all_animals.append(self)  # Add the current Animal object to the list

    def speak(self):
        """Makes a generic animal sound."""
        print("The animal makes a noise.")

    def __str__(self):
        """Returns a string representation of the Animal object."""
        return f"Kingdom: '{self.kingdom}', Name: '{self.name}', Species: '{self.species}'"

# Example usage:
animal1 = Animal("Buddy", "Canis familiaris", "Chordata")
animal2 = Animal("Mittens", "Felis catus")

animal1.speak()
animal2.speak()

print(animal1)
print(animal2)

print(f"All Animals: {Animal.all_animals}")