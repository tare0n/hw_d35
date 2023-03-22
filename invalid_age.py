class InvalidAgeError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = "This age is incorrect"

    def __str__(self):
        return self.message


def age_check():
    try:
        age = int(input('Please, print your age: '))
        if age < 0 or age >= 120:
            raise InvalidAgeError('Sorry, this age is incorrect')
        print(f"You're {age} years old")
    except ValueError:
        print('Age must be int number')
    except InvalidAgeError as e:
        print(e)

