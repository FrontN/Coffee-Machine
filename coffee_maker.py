from coffee_machine_art import logo
import time
import os

def clear_screen():
    """
    Clears the screen and prints the logo.

    This function is used to clear the command line interface screen and
    print the logo of the coffee machine. It uses the os module to
    determine the correct command to use based on the operating system.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

class Coffee_maker:
    def make_coffee(self, get_ingredients, recipe, choice):
        """
        Makes a coffee drink given the recipe and choice of drink.

        Parameters
        ----------
        get_ingredients : function
            A function that takes a recipe and subtracts the required resources from the current resources.
        recipe : dict
            A dictionary containing the ingredients and their quantities required to make the drink.
        choice : str
            The name of the drink to make.

        Returns
        -------
        None
        """
        get_ingredients(recipe)
        print(f"Preparing your {choice}", end="")
        for _ in range(3):
            print(".",flush=True, end="")
            time.sleep(2)
        clear_screen()
        print(self.coffee_serving(choice))

    def coffee_serving(self, choice):
        """
        Returns a string containing the name of the drink and a smiling face emoji.

        Parameters
        ----------
        choice : str
            The name of the drink to make.

        Returns
        -------
        str
            A string containing the name of the drink and a smiling face emoji.
        """
        return f"Here's your {choice} ☕!"