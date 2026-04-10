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

class Money_Machine:
    COIN_TO_DOLLARS = {
        "Penny": 0.01,
        "Nickel": 0.05,
        "Dime": 0.10,
        "Quarter": 0.25
}
    def __init__(self):
        """
        Initializes the Money_Machine object with the initial values of
        Penny, Nickel, Dime, Quarter, and Dollars attributes.
        
        The Money_Machine object is used to manage the coins inserted into
        the coffee machine.
        """
        self.Penny = 0
        self.Nickel = 0
        self.Dime = 0
        self.Quarter = 0
        self.Dollars = 0

    def insert_coins(self):
        """
        Asks the user to insert coins until they choose to pay or insert
        non valid option.

        Parameters
        ----------
        None

        Returns
        -------
        float
            The total amount of money inserted by the user.
        """

        options = tuple([option for option in vars(self)])
        while True:
            user_answer = input(f"What do you want to insert? {options} or 'Pay' to pay: ").capitalize()
            if user_answer in options:
                self.money_changer(user_answer)
            elif user_answer == "Pay":
                return round(self.Dollars,2)
            else:
                print(f"non valid option. Please choose one of these options: {options} or 'Pay' to pay")
                time.sleep(1.5)
                clear_screen()
                

    def money_changer(self, coin):
        """
        Asks the user to insert a given coin until a valid option is entered.

        Parameters
        ----------
        coin : str
            The type of coin to insert.

        Returns
        -------
        None
        """
        while True:
            try:
                clear_screen()
                inserted_coin = int(input(f"How many {coin} do you want to insert? "))
                if coin == "Dollars":
                    self.Dollars += inserted_coin
                    break
                else:
                    self.Dollars += inserted_coin * Money_Machine.COIN_TO_DOLLARS[coin]
                    break
            except ValueError:
                print("please insert numbers, letters are not allowed")
                time.sleep(1.5)

    def payment_accepted(self, cost):
        """
        Checks if the total amount of money inserted is enough to pay for the given drink.

        Parameters
        ----------
        cost : float
            The cost of the drink to check.

        Returns
        -------
        bool
            True if the total amount of money inserted is enough to pay for the drink, False otherwise.
        """
        return self.insert_coins() >= cost

    def give_change(self, cost):
        """
        Calculate the change owed to the user after paying for a drink.

        Parameters
        ----------
        cost : float
            The cost of the drink to calculate the change for.

        Returns
        -------
        float
            The change owed to the user, or 0 if the user does not have enough money to pay for the drink.
        """
        if self.Dollars > cost:
            change = self.Dollars - cost
            self.Dollars -= change
            return change
        return 0
    
    def money_to_piggy_bank(self):
        """
        Transfer all the money from the money machine to the piggy bank.

        Returns
        -------
        float
            The amount of money transferred to the piggy bank.
        """
        money = self.Dollars
        self.Dollars = 0
        return money