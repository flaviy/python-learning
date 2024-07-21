"""
Create a class called Customer. The Customer class should have the following attributes:
"""

from customer import Customer


def create_customer():
    customer = Customer(
        input('Enter first name: '),
        input('Enter last name: '),
        input('Enter account number: '),
        float(input('Enter balance: '))
    )
    return customer


def main():
    customer = create_customer()
    print(customer)

    while True:
        print('^' * 50)
        print('Main menu: ')
        print('1. Deposit')
        print('2. Withdraw')
        print('3. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter the amount to deposit: '))
            customer.deposit(amount)
        elif choice == '2':
            amount = float(input('Enter the amount to withdraw: '))
            customer.withdraw(amount)
        elif choice == '3':
            break
        else:
            print('Invalid choice')


main()




