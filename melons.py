"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """ A generic melon order """

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = 0.09


    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total


    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        
        self.species = species
        self.qty = qty
        self.order_type = "domestic"
        self.tax = 0.08


    def get_total(self):
        """Calculate price."""

        base_price = 5
        if self.species == "Christmas melon":
            base_price *= 1.5
        total = (1 + self.tax) * self.qty * base_price
        return total



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        
        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17


    def get_total(self):
        """Calculate price."""

        base_price = 5
        if self.species == "Christmas melon":
            base_price *= 1.5
            
        total = (1 + self.tax) * self.qty * base_price

        if self.qty < 10:
            total += 3

        return total


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
