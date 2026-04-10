from coffee_machine_art import logo
from prettytable import PrettyTable
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

def get_valid_input(prompt, options):
    """
    Asks the user for input until a valid option is entered.

    Parameters
    ----------
    prompt : str
        The string to be displayed to the user.
    options : list
        A list of valid options.

    Returns
    -------
    str
        The user's input, which is guaranteed to be in options.
    """
    while True:
        clear_screen()
        user_answer = input(prompt).lower()
        if user_answer in options:
            return user_answer
        else:
            print(f"non valid option. Please choose one of these options: {options}")
            time.sleep(1.5)

class Resources:
    INITIAL_VALUES = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0
}
    def __init__(self):
        """
        Initializes the Resources object with the initial values of water, milk, coffee, and money.

        The Resources object is used to manage the resources of the coffee machine.
        It has four attributes: water, milk, coffee, and money, which are
        initialized to the values specified in the INITIAL_VALUES dictionary.
        """
        self.water = self.INITIAL_VALUES["water"]
        self.milk = self.INITIAL_VALUES["milk"]
        self.coffee = self.INITIAL_VALUES["coffee"]
        self.money = self.INITIAL_VALUES["money"]
    
    def report(self):
        """
        Prints a table of all resources and their quantities.

        This function is used to display all resources and their quantities in a
        table. It uses the PrettyTable library to create the table and
        prints it to the console. It then waits for 3 seconds before
        continuing.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        table = PrettyTable()
        table.align = "l"
        table.field_names= ["Resource", "Quantity"]
        for key, value in vars(self).items():
            display_value = f"{value:.2f} $" if key == "money" else f"{value} ml" if key in ["water", "milk"] else f"{value} g"
            table.add_row([key.capitalize(), display_value])
        print(table)
        time.sleep(3)

    def has_enough_resources(self, recipe):
        """
        Checks if there are enough resources to make a drink of the given recipe.

        Parameters
        ----------
        recipe : dict
            A dictionary containing the ingredients and their quantities required to make the drink.

        Returns
        -------
        bool
            True if there are enough resources, False otherwise.

        If there are not enough resources, prints a message saying so and returns False.
        Otherwise, returns True.
        """
        for ingredient in recipe:
            if recipe[ingredient] > getattr(self, ingredient):
                print(f"Sorry, there is not enough *{ingredient}*. Please choose another drink or check the report to see the available resources.")
                time.sleep(3)
                return False
        return True

    def get_ingredients(self, recipe):
        """
        Subtracts the required ingredients from the current resources.

        Parameters
        ----------
        recipe : dict
            A dictionary containing the ingredients and their quantities required to make the drink.

        Returns
        -------
        None
        """
        for ingredient in recipe:
            current_value = getattr(self, ingredient)
            setattr(self, ingredient, current_value - recipe[ingredient])

    def add_to_piggy_bank(self, money):
        """
        Adds the given amount of money to the piggy bank.

        Parameters
        ----------
        money : float
            The amount of money to add to the piggy bank.

        Returns
        -------
        None
        """
        self.money += money

    def add_or_remove_resources(self, max_capacity, selected_resource, choice):
        """
        Adds or removes the given amount of resources from the current resources.

        Parameters
        ----------
        max_capacity : int
            The maximum capacity of the resource.
        selected_resource : str
            The resource to add or remove.
        choice : str
            Whether to add or remove the resource.

        Returns
        -------
        None
        """
        current_value = getattr(self, selected_resource)
        print(f"Current quantity: {current_value}")
        while True:
            while True:
                try:
                    clear_screen()
                    if current_value == max_capacity:
                        if choice == "add" and selected_resource != "money":
                            print(f"Sorry, the {selected_resource} is already at its maximum capacity. Please choose another resource to add.")
                            time.sleep(1.5)
                        else:
                            print(f"Sorry there is no {selected_resource} to remove.")
                            time.sleep(1.5)
                        supply = 0
                        break
                    supply = float(input(f"How much {selected_resource} do you want to {choice}: "))
                    break
                except ValueError:
                    print("please insert a valid number, letters and symbols are not allowed")
                    time.sleep(1.5)
            if supply > 0:
                if choice == "add":
                    formula = current_value + supply
                    compaire = formula > 1000 and selected_resource != "money"
                    text_choice = f"Sorry, adding {supply} {selected_resource} would exceed the maximum capacity. Please try again."
                else:
                    formula = current_value - supply
                    compaire = formula < 0
                    text_choice = f"Sorry, there is not enough {selected_resource} to remove. Please try again"
                if compaire:
                        print(text_choice)
                        time.sleep(1.5)
                else:
                    setattr(self, selected_resource, formula)
                    self.report()
                    break
            else:
                break

    def manage_resources(self):
        """
        Manages the resources of the coffee machine.

        Allows the user to add or remove resources from the machine, view the current resources,
        or go back to the main menu.

        Parameters
        ----------
        None

        Returns
        -------
        None

        """
        self.report()
        options = ("add", "remove", "back", "report")
        while True:
            clear_screen()
            choice = get_valid_input(f"What do you want to do? {options}: ", options)
            if choice == "add":
                text_choice = "what do you want to add? "
                max_capacity = 1000
            elif choice == "remove":
                text_choice = "what do you want to remove? "
                max_capacity = 0
            elif choice == "report":
                clear_screen()
                self.report()
                continue
            else:
                break
            resources = tuple(vars(self).keys())
            clear_screen()
            selected_resource = get_valid_input(f"{text_choice} {resources}: ", resources).lower()
            self.add_or_remove_resources(max_capacity, selected_resource, choice)
