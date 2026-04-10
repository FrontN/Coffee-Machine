from resources_management import Resources
from money_macchine import Money_Machine
from coffee_maker import Coffee_maker
from coffee_machine_art import logo
from menu import Menu
import time
import os

resources = Resources()
money_machine = Money_Machine()
coffee_maker = Coffee_maker()
menu = Menu()

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

def main():
    """
    The main function of the program. It runs an infinite loop until the user chooses to turn off the machine.
    It then prompts the user to choose an option from the menu and performs the corresponding action.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """

    machine_on = True
    change = 0
    options_list = ["off", "admin", *menu.display_drinks()]

    while machine_on:
        choice = get_valid_input(f"What would you like? {menu.display_drinks()}: ", options_list)

        if choice == "off":
            clear_screen()
            machine_on = False
            print("Goodbye!!")
        elif choice == "admin":
            clear_screen()
            resources.manage_resources()
        else:
            recipe = menu.find_drink(choice)['ingredients']
            cost = menu.find_drink(choice)['cost']
            if resources.has_enough_resources(recipe):
                while True:
                    clear_screen()
                    print(f"The cost of a {choice} is {cost}$")
                    time.sleep(1.5)
                    if money_machine.payment_accepted(cost):
                        clear_screen()
                        coffee_maker.make_coffee(resources.get_ingredients, recipe, choice)
                        time.sleep(1.5)
                        change = money_machine.give_change(cost)
                        if change > 0:
                            clear_screen()
                            print(f"Here's your change: {change:.2f}$")
                            time.sleep(3)
                        resources.add_to_piggy_bank(money_machine.money_to_piggy_bank())
                        break
                    else:
                        clear_screen()
                        add_or_refund = get_valid_input("Sorry that's not enough money. (add/refund): ", ["add", "refund"])
                        if add_or_refund == "add":
                            continue
                        else:
                            clear_screen()
                            print("Money refunded")
                            time.sleep(1.5)
                            change = 0
                            break

if __name__ == "__main__":
    main()
