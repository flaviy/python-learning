class Numbers:
    def __init__(self, area_letter, area_name):
        self.area_letter = area_letter
        self.area_name = area_name
        self.current_order_number_generator = self.get_current_order_number_generator()

    def __str__(self):
        return f'{self.area_name} - {self.area_letter}'

    @staticmethod
    def get_current_order_number_generator():
        current_order_number = 0
        while True:
            current_order_number = current_order_number + 1
            yield current_order_number

    def get_current_order_number(self):
        return next(self.current_order_number_generator)

    def get_current_order_number_decorator(self, function):
        def wrapper(*args, **kwargs):
            print(f'Your number: {self.area_letter} -  {function(*args, **kwargs)}')
            print('Wait and someone will be with you shortly')

        return wrapper

