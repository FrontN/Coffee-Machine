from resources import RESOURCES
from prettytable import PrettyTable
from coffee_machine_art import logo
from menu import MENU
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

def resources_checker(resources):
    """
    Print a table of all resources and their quantities.

    This function is used to display all resources and their quantities in a
    table. It uses the PrettyTable library to create the table and
    prints it to the console. It then waits for 5 seconds before
    continuing.

    Parameters
    ----------
    resources : dict
        A dictionary containing all resources and their quantities.

    Returns
    -------
    None
    """
    table = PrettyTable()
    table.field_names= ["Resource", "Quantity"]
    for key, value in resources.items():
        display_value = f"{value:.2f}$" if key == "money" else value
        table.add_row([key.capitalize(), display_value])
    print(table)
    time.sleep(5)

def has_enough_resources(choice):
    """
    Check if there are enough resources to make a drink of the given choice.

    Parameters
    ----------
    choice : str
        The name of the drink to check.

    Returns
    -------
    bool
        True if there are enough resources, False otherwise.

    If there are not enough resources, print a message saying so and return False.
    Otherwise, return True.
    """
    ingredients = MENU[choice]['ingredients']
    for item in ingredients:
        if RESOURCES[item] < ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            time.sleep(1.5)
            return False
    return True

def get_valid_int(prompt):
    """
    Keep asking the user for input until a valid integer is entered.

    Parameters
    ----------
    prompt : str
        The string to be displayed to the user.

    Returns
    -------
    int
        The valid integer entered by the user.
    """
    while True:
        clear_screen()
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("please insert numbers, letters are not allowed")
            time.sleep(1.5)

def coin_machine():
    """
    Calculate the total amount of money inserted by the user.

    Asks the user to input the number of each type of coin they want to insert, then
    calculates the total amount of money.

    Returns
    -------
    float
        The total amount of money inserted by the user.
    """
    options = {
        "Penny": 0,
        "Nickel": 0,
        "Dime": 0,
        "Quarter": 0,
        "Dollars": 0
    }

    change = {
        "Penny": 0.01,
        "Nickel": 0.05,
        "Dime": 0.10,
        "Quarter": 0.25,
        "Dollars": 1
    }
    for option in options:
        options[option] = get_valid_int(f"How many {option} do you want to insert? ") * change[option]
    
    return float(f"{sum(options.values()):.2f}")

def inserted_enough_coins(choice, inserted):     
    """
    Checks if the total amount of money inserted by the user is enough to buy a drink of the given choice.

    Parameters
    ----------
    choice : str
        The name of the drink to check.
    inserted : float
        The total amount of money inserted by the user.

    Returns
    -------
    bool
        True if the amount of money is enough, False otherwise.
    float
        The remainder of the amount of money after buying the drink, or the total amount of money inserted if not enough to buy the drink.
    """
    inserted_val = coin_machine() + inserted
    clear_screen()
    print(f"You've inserted: {inserted_val}$")
    time.sleep(1.5)
    cost = MENU[choice]['cost']
    remainder = inserted_val - cost
    if remainder >= 0:
        return True, remainder
    return False, inserted_val

def coffee_maker(choice):
    """
    Make a drink of the given choice and subtract the required resources.

    Parameters
    ----------
    choice : str
        The name of the drink to make.

    Returns
    -------
    str
        A string containing the name of the drink and a smiling face emoji.
    """
    for i in MENU[choice]['ingredients']:
        RESOURCES[i] -= MENU[choice]['ingredients'][i]
    RESOURCES["money"] += MENU[choice]['cost']
    print("Making your drink", end="")
    for _ in range(3):
        print(".",flush=True, end="")
        time.sleep(1)
    clear_screen()
    return f"Here's your {choice} ☕!"

def display_drinks():
    """
    Returns a tuple containing all available drinks.

    Returns
    -------
    tuple
        A tuple containing all available drinks.
    """
    return tuple(drink for drink in MENU)

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

def main():
    """
    This is the main function of the program. It runs an infinite loop which
    continues to ask the user for input until the user chooses to turn off the
    machine. If the user chooses to report the resources, it will print the
    current amount of resources and continue to the next iteration of the
    loop. If the user chooses a drink, it will check if there are enough
    resources to make the drink. If there are, it will ask the user to insert
    coins until they have inserted enough money. Then it will subtract the
    required resources and print out the drink and the change. If there are
    not enough resources, it will print a message saying so and continue to
    the next iteration of the loop.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    machine_on = True
    inserted = 0
    options_list = ["off", "report", *display_drinks()]

    while machine_on:
        choice = get_valid_input(f"What would you like? {display_drinks()}: ", options_list)

        if choice == "off":
            clear_screen()
            machine_on = False
            print("Goodbye!!")
            break
        elif choice == "report":
            clear_screen()
            resources_checker(RESOURCES)
        else:
            if has_enough_resources(choice):
                while True:
                    clear_screen()
                    print(f"The cost of a {choice} is {MENU[choice]['cost']}$")
                    time.sleep(1.5)
                    payment_accepted, inserted = inserted_enough_coins(choice, inserted)
                    if payment_accepted:
                        clear_screen()
                        print(coffee_maker(choice))
                        time.sleep(1.5)
                        if inserted > 0:
                            clear_screen()
                            print(f"Here's your change: {inserted:.2f}$")
                            inserted = 0
                        break
                    else:
                        clear_screen()
                        add_or_refund = get_valid_input("Sorry that's not enough money. (add/refund): ", ["add", "refund"])
                        if add_or_refund == "add":
                            continue
                        else:
                            clear_screen()
                            print("Money refunded")
                            inserted = 0
                continue

if __name__ == "__main__":
    main()
