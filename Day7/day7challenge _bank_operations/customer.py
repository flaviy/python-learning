from person import Person


class Customer(Person):
    def __init__(self, first_name, last_name, account_number, balance):
        super().__init__(first_name, last_name)
        self.account = account_number
        self.balance = balance

    def __str__(self):
        return f'{super().__str__()} - {self.account} - {self.balance}'

    def deposit(self, amount):
        self.balance += amount
        print(f'{self.first_name} {self.last_name} deposited {amount}. New balance is {self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= amount
            print(f'{self.first_name} {self.last_name} withdrew {amount}. New balance is {self.balance}')
