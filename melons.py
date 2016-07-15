"""This file should have our order classes in it."""
from random import randint

class AbstractMelonOrder(object):
    """ A generic melon order """

    def __init__(self, species, qty, order_type, tax=0.09):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = tax
        self.order_type = order_type

    
    def get_base_price(self):
        """Return a random base price between 5-9"""

        random_base_price = randint(5,9)
        return random_base_price


    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()

        if self.species == "Christmas melon":
            base_price *= 1.5
        total = (1 + self.tax) * self.qty * base_price

        return total


    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)
        self.country_code = country_code


    def get_total(self):
        """Calculate price."""

        total = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            total += 3

        return total


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """Governmental melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
  
        self.species = species
        self.qty = qty
        self.tax = 0

   

    def mark_inspection(self, passed):
        """ Update passed_inspection to true if inspection passed """

        passed_inspection = False

        if passed is True:
            passed_inspection = True
            print True
        


