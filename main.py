
if __name__ == "__main__":
    # TODO: Create an instance of the Animal class
    # TODO: Print the Animal instance
    # TODO: Call the method to make a generic animal sound

    # TODO: Create an instance of the Dog class
    # TODO: Print the Dog instance
    # TODO: Call the method to make the dog-specific sound

    # TODO print out all the animals

 class Animal:
    """A generic animal class."""

    all_animals = []  # Class-level attribute to store all Animal objects
    kingdom = 'Animalia'  # Class-level attribute for kingdom

    def __init__(self, name, species, kingdom='Animalia'):
        """
        Initializes an Animal object.

        Args:
            name (str): The name of the animal.
            species (str): The species of the animal.
            kingdom (str, optional): The kingdom of the animal. Defaults to the class-level kingdom.
        """
        self.name = name
        self.species = species
        self.kingdom = kingdom if kingdom is not None else Animal.kingdom
        Animal.all_animals.append(self)  # Add the current Animal object to the list

    def speak(self):
        """Makes a generic animal sound."""
        print("The animal makes a noise.")

    def __str__(self):
        """Returns a string representation of the Animal object."""
        return f"Kingdom: '{self.kingdom}', Name: '{self.name}', Species: '{self.species}'"

class Dog(Animal):
    """A class representing a dog, inheriting from Animal."""

    def __init__(self, name, species, breed, kingdom='Animalia'):
        """
        Initializes a Dog object.

        Args:
            name (str): The name of the dog.
            species (str): The species of the dog.
            breed (str): The breed of the dog.
            kingdom (str, optional): The kingdom of the dog. Defaults to the class-level kingdom.
        """
        super().__init__(name, species, kingdom)  # Call the parent class's initializer
        self.breed = breed

    def __str__(self):
        """Overrides the __str__ method to include the breed."""
        parent_str = super().__str__()  # Get the string representation from the parent class
        return f"{parent_str}, Breed: '{self.breed}'"

    def speak(self):
        """Makes the dog bark."""
        print("The dog barks.")

# Example usage:
# TODO: Create an instance of the Animal class
my_animal = Animal("Simba", "Panthera leo")  # Corrected instantiation

# TODO: Print the Animal instance
print(my_animal)

# TODO: Call the method to make a generic animal sound
my_animal.speak()

# TODO: Create an instance of the Dog class
my_dog = Dog("Buddy", "Canis familiaris", "Golden Retriever")

# TODO: Print the Dog instance
print(my_dog)

# TODO: Call the method to make the dog-specific sound
my_dog.speak()

# TODO: print out all the animals
print("\nAll animals:")
for animal in Animal.all_animals:
    print(animal)