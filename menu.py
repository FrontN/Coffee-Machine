import time
class Menu:
    DATA = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
}
    def display_drinks(self):
        """
        Returns a tuple containing all the available drinks in the menu.

        Returns
        -------
        tuple
            A tuple containing all the available drinks in the menu.
        """
        return tuple(drink for drink in self.DATA)
    
    def find_drink(self, order_name):
        """
        Returns a dictionary containing the ingredients and their quantities required to make the given drink,
        as well as the cost of the drink.

        Parameters
        ----------
        order_name : str
            The name of the drink to find.

        Returns
        -------
        dict
            A dictionary containing the ingredients and their quantities required to make the given drink,
            as well as the cost of the drink.
        """
        return self.DATA[order_name]