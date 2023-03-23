"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__ (self, start=0):
        """Initiates a serial number generator starting at 0"""
        self.start = self.next = start

    def generate(self):
        """Returns the current serial number and generates the next"""
        self.next +=1
        return self.next -1
        

    def reset(self):
        """Resets the serial number generator back to 0"""
        self.next = self.start



