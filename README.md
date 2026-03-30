Python Coffee Machine ☕
A sophisticated, console-based Coffee Machine simulator implemented in Python with automated resource management and a multi-currency coin processing system.

Features 🎮
Real-time Resource Tracking: Monitors water, milk, and coffee beans, preventing orders if ingredients are insufficient.

Dynamic Coin Processor: Handles multiple denominations (Pennies, Nickels, Dimes, Quarters, Dollars) with automatic total calculation.

Robust Input Handling: Custom validation loops for both strings and integers to ensure a crash-free user experience.

Modular Architecture: Clean separation of logic for resource checking, payment processing, and drink preparation.

Smart Feedback System: Provides specific alerts when a resource is low (e.g., "Sorry, there is not enough water").

Automated Maintenance: Includes a 'Report' feature to check current machine status and an 'Off' command for maintenance.

Game Rules 📋
Objective: Select a drink and provide enough change to complete the transaction.

Drink Menu: * Espresso: Concentrated coffee (requires water and coffee).

Latte: Coffee with steamed milk.

Cappuccino: Balanced mix of coffee and milk.

Payment:

The machine calculates the total from various coin types.

If the amount is insufficient, you can choose to Add more coins or get a Refund.

If you overpay, the machine calculates and returns the Change (resto).

Resources: Every drink consumed is subtracted from the global inventory. The machine earns money with every successful sale.

Project Structure 📁
Plaintext
Coffee-Machine-Python/
├── Coffee_machine_image.png
├── Coffee_machine_workflow.drawio.pdf
├── main.py                    # Main program logic and entry point
├── coffee_machine_art.py      # ASCII art logo
├── menu.py                    # Drinks recipes and costs
├── resources.py               # Initial machine inventory
└── README.md                  # This file
Main Functions Overview:
clear_screen() - Clears console and displays the machine logo.

get_valid_input() - Validates string options (drink choice, add/refund).

get_valid_int() - Ensures user enters only numbers for coin counts.

has_enough_resources() - Verifies if ingredients are available before starting payment.

coin_machine() - Interactive loop for inserting different coin denominations.

inserted_enough_coins() - Compares total inserted money against drink cost.

coffee_maker() - Deducts ingredients and adds profit to the machine.

resources_checker() - Displays a detailed report of remaining supplies and profit.

Requirements ✅
Python 3.x

No external dependencies required (uses only Python standard library: os, time).

Installation & Setup 🚀
Clone the repository:

Bash
git clone https://github.com/FrontN/Coffee-Machine-Python.git
cd Coffee-Machine-Python
How to Play 🎯
Run the program:

Bash
python main.py
Choose a drink from the menu (espresso/latte/cappuccino).

Type report at any time to see the machine's internal status.

If resources are available, follow the prompts to insert coins.

Collect your drink and any remaining change.

Type off to shut down the machine.

Game Output Example 📺
Plaintext
What would you like? ('espresso', 'latte', 'cappuccino'): latte
The cost of a latte is 2.5$

How many Quarters do you want to insert? 10
You've inserted: 2.5$

Here's your latte ☕!
Technical Highlights 💡
Platform Independent: Works seamlessly on Windows (cls) and Unix-based systems (clear).

Data Driven: Recipes and costs are stored in an external MENU dictionary for easy updates.

Floating Point Precision: Uses formatted strings (:.2f) to handle monetary values accurately.

User-Centric Design: Includes time.sleep() delays to ensure the user has time to read feedback messages.

Future Enhancements 🎯
Daily profit persistence (saving report to a .txt file).

Refill system to restock ingredients without restarting.

Custom drink creation mode.

Graphical User Interface (GUI) version.

Contributing 🤝
Feel free to fork this repository and submit pull requests for any improvements!

Author 👨‍💻
FrontN - Created as a learning project for Python logic and state management.

Enjoy your coffee! ☕
