![CoffeeMoccamasterGIF (2)](https://github.com/user-attachments/assets/3f9a3ed5-ffc3-4380-b881-384480f2b925)

# Coffee Machine

A Python-based coffee machine program that simulates making espresso, latte, or cappuccino by managing resources (water, milk, coffee) and handling coin payments. The program also provides a report of available resources and can be turned off gracefully by the user.

## Features

- **Coffee Options**: The program offers three types of coffee: 
  - Espresso
  - Latte
  - Cappuccino
- **Resource Management**: The machine keeps track of available water, milk, and coffee. If resources are insufficient for the selected coffee, the user is notified.
- **Coin Payment System**: Users are prompted to insert coins, and the program calculates whether enough money was inserted, provides change if necessary, and refunds the money if the payment is insufficient.
- **Report Function**: Users can type `report` to get the current status of resources and the total money earned by the machine.
- **Shutdown Option**: Type `off` to gracefully turn off the coffee machine.

## How It Works

1. **Select Coffee**: The user is prompted to select a drink from `espresso`, `latte`, or `cappuccino`.
2. **Check Resources**: The machine checks if there are enough resources (water, milk, and coffee) to make the selected coffee. If not, it notifies the user.
3. **Insert Coins**: If resources are sufficient, the user is asked to insert coins (quarters, dimes, nickels, pennies).
4. **Payment Processing**: The machine checks if the inserted amount covers the coffee's cost. If it does, it makes the coffee and gives change if needed. If not, it refunds the money.
5. **Update Resources**: After making the coffee, the machine updates the available resources.
6. **Report**: At any time, the user can check the current resources and total money earned by typing `report`.
7. **Turn Off**: The user can type `off` to turn off the machine and end the program.

## How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/coffee-machine.git
   ```

2. Navigate to the project directory:

   ```bash
   cd coffee-machine
   ```

3. Run the program:

   ```bash
   python main.py
   ```

4. Follow the prompts in the terminal to interact with the coffee machine.

## Example Output

```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins
How many quarters: 10
How many dimes: 0
How many nickles: 0
How many pennies: 0
Here is $0.0 in change.
Here is your latte ☕. Enjoy!

What would you like? (espresso/latte/cappuccino): report
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
```

## Project Structure

- `main.py`: Main Python file containing the coffee machine code.
- `art.py`: This file containing the logo.

## Future Improvements

- Add more drink options (e.g., Mocha, Americano).
- Implement user authentication and a management system for the machine.
- Create a graphical user interface (GUI) for better user experience.

## License

This project is licensed under the MIT License.

---
