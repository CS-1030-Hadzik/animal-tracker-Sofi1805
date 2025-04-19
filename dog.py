class Dog:
    """
    Derived class representing a dog, which is a type of Animal.
    """
    # TODO: Initialize the Dog class and add the breed attribute.
    # The constructor should accept name, species, and breed as parameters.
    
    # TODO: Override the __str__ method to include the breed.
    # Example output:
    # Kingdom: 'kingdom attribute', Name: 'name attribute', Species: 'species attribute', Breed: 'breed attribute'
    
    # TODO: Add a method for the dog to make a specific sound. 
    # Call the method `speak` and make it output a specific message like 
    # "The dog barks.

    def __init__(self, name, species, breed, kingdom='Animalia'):
        """
        Initializes a Dog object.

        Args:
            name (str): The name of the dog.
            species (str): The species of the dog.
            breed (str): The breed of the dog.
            kingdom (str, optional): The kingdom of the dog. Defaults to 'Animalia'.
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
dog1 = Dog("Max", "Canis familiaris", "Golden Retriever")
dog2 = Dog("Lucy", "Canis familiaris", "Poodle", "Chordata")

dog1.speak()
dog2.speak()

print(dog1)
print(dog2)

print(f"All Animals (including dogs): {Animal.all_animals}")