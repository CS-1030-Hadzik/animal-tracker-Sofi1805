class Animal:
    """
    Base class representing a generic animal.
    """
     # Class-level attribute
    kingdom = 'Animalia'
    # TODO create a class-level attribute that is a list of all the Animal Objects
    all_animals = [] #boom

    # TODO create the initializer for Animal with name and species as attributes
    def __init__(self, name, species):
        self.name = name
        self.species = species

        Animal.all_animals.append(self)

    # TODO Add a method to make a generic sounds
    # Call the method 'speak' and make it output a specific message like
    # "The animal makes a noise."
    def speak(self):
        print(f'The animal makes a noise')

    # TODO __str__ method for string representation
    # Example output
    # Kingdom: 'kingdom attribute', Name: 'name attribute', Species: 'species attribute'
    def __str__(self):
        return f"Kingdom: '{self.kingdom}', Name: '{self.name}', Species: '{self.species}'"
    
    @classmethod
    def get_all_animals(cls):
        return cls.all_animals