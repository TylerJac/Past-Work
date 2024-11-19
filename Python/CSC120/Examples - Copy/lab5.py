
class FootMeasure:
    """
    A class to represent a linear measurement of feet and inches.

    Attributes: feet (int): The number of feet in the measurement.
        inches (int): The number of inches in the measurement.
    """

    def __init__(self, feet=0, inches=0):
        """
        Initializes a FootMeasure object.

        Args: feet (int, optional): The number of feet. Defaults to 0.
            inches (int, optional): The number of inches. Defaults to 0.
        """
        self.feet = feet
        self.inches = inches

    def __repr__(self):
        """
        Returns a string representation of the FootMeasure object.

        Returns: String representation of the object.
        """
        return f"{self.feet} ft. {self.inches} in." if self.feet != 0 or self.inches != 0 else "0 ft. 0 in."

    def __str__(self):
        """
        Returns a string representation of the FootMeasure object.

        Returns: String representation of the object.
        """
        return f"{self.feet} ft. {self.inches} in." if self.feet != 0 or self.inches != 0 else "0 ft. 0 in."

    def __add__(self, other):
        """
        Adds two FootMeasure objects together.

        Args: other (FootMeasure): Another FootMeasure object to add.

        Returns: A new FootMeasure object representing the sum.
        """
        total_inches = self.feet * 12 + self.inches + other.feet * 12 + other.inches
        feet = total_inches // 12
        inches = total_inches % 12
        return FootMeasure(feet, inches)

    def __eq__(self, other):
        """
        Checks if two FootMeasure objects are equal.

        Args: other (FootMeasure): Another FootMeasure object to compare.

        Returns: True if the objects are equal, False otherwise.
        """
        return (self.feet, self.inches) == (other.feet, other.inches)

    def __ne__(self, other):
        """
        Checks if two FootMeasure objects are not equal.

        Args: other (FootMeasure): Another FootMeasure object to compare.

        Returns: True if the objects are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Checks if the current FootMeasure object is less than another.

        Args: other (FootMeasure): Another FootMeasure object to compare.

        Returns: True if the current object is less than the other, False otherwise.
        """
        return (self.feet, self.inches) < (other.feet, other.inches)

    def __le__(self, other):
        """
        Checks if the current FootMeasure object is less than or equal to another.

        Args: other (FootMeasure): Another FootMeasure object to compare.

        Returns:  True if the current object is less than or equal to the other, False otherwise.
        """
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        """
        Checks if the current FootMeasure object is greater than another.

        Args: other (FootMeasure): Another FootMeasure object to compare.

        Returns:  True if the current object is greater than the other, False otherwise.
        """
        return not self.__le__(other)

    def __ge__(self, other):
        """
        Checks if the current FootMeasure object is greater than or equal to another.

        Args: other (FootMeasure): Another FootMeasure object to compare.

        Returns:  True if the current object is greater than or equal to the other, False otherwise.
        """
        return not self.__lt__(other)
