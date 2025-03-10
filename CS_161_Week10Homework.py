#Parker Palubeski
#Week 10
#CS 161

class SolarObject:
    """
    Represents a solar object

    Attributes
    ----------
    name : str
        name of the solar object
    distance : float
        distance of the object from the sun, in au
    orbit : int
        orbital period of the object, in days

    Methods
    -------
    colonization():
        returns the population an object can support if colonized
    spin():
        a virtual function to be overwritten by the child objects
    """
    def __init__(self, name, distance, orbit):
        """
        Initalizes a new object of class SolarObject

        Uses the attributes of SolarObject as parameters
        """
        self.name = name
        self.distance = distance
        self.orbit = orbit
    def colonization(self):
        """
        Calculates the population an object can support if colonized

        Parameters
        ----------
            distance : float
                distance of the object from the sun, in au

        Returns
        -------
            float
                The population the object can support
        """
        #6 billion was the default value provided
        return 6000000000 / self.distance
    def set_spin(self):
        #Virtual function to be overwritten by child classes
        pass

class Planet(SolarObject):
    """
    Subclass of SolarObject, representing a planet
    Methods:
    --------
    set_spin():
        returns spin of the planet
    printObject():
        prints planet information to the console
    """
    def set_spin(self):
        """
        Returns string describing the spin of the planet
        """
        return "slightly elliptical"
    def printObject(self):
        print(f"{self.name} is {self.distance} au from the sun, spins {self.set_spin()}, and has an orbit taking {self.orbit} days to complete. In total, {self.name} can support a population of approximately: {self.colonization()/1000000000:.0f} billion.")

class Comet(SolarObject):
    """
    Subclass of SolarObject, representing a comet
    Methods:
    --------
    set_spin():
        returns spin of the comet
    printObject():
        prints comet information to the console
    """
    def set_spin(self):
        """
        Returns string describing the spin of the planet
        """
        return "like crazy"
    def printObject(self):
        print(f"{self.name} is {self.distance} au from the sun, spins {self.set_spin()}, and has an orbit taking {self.orbit/365:.2f} years to complete. In total, {self.name} can support a population of approximately:  {self.colonization()/1000000000:.0f} billion.")


if __name__ == "__main__":
    #Object definitions
    earth = Planet("Earth", 1, 365)
    mars = Planet("Mars", 1.4, 687)
    halley = Comet("Halley", 35, 28087)
    halebopp = Comet("HaleBopp", 354, 875011)

    #Printing attributes of objects defined above
    earth.printObject()
    mars.printObject()
    halley.printObject()
    halebopp.printObject()