class DataAirtimeApp:
    def __init__(self):
        self.balance = 0
        self.data_balance = 0

    def deposit_airtime(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: {amount} units, New Airtime Balance: {self.balance} units"
        else:
            return "Invalid deposit amount"

    def buy_data(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.data_balance += amount * 10  # Assuming 1 unit of airtime buys 10MB of data
            return f"Bought: {amount * 10}MB, New Data Balance: {self.data_balance}MB, Remaining Airtime Balance: {self.balance} units"
        else:
            return "Invalid amount or insufficient airtime balance"

    def check_airtime_balance(self):
        return f"Current Airtime Balance: {self.balance} units"

    def check_data_balance(self):
        return f"Current Data Balance: {self.data_balance}MB"

if __name__ == "__main__":
    app = DataAirtimeApp()
    print(app.deposit_airtime(100))  # Deposited: 100 units, New Airtime Balance: 100 units
    print(app.buy_data(20))  # Bought: 200MB, New Data Balance: 200MB, Remaining Airtime Balance: 80 units
    print(app.check_airtime_balance())  # Current Airtime Balance: 80 units
    print(app.check_data_balance())  # Current Data Balance: 200MB
    print(app.buy_data(100))  # Invalid amount or insufficient airtime balance
    print(app.deposit_airtime(-10))  # Invalid deposit amount