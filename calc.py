def calc_salt(amount):
    try:
        return amount/100
    except TypeError:
        try:
            return int(amount)/100
        except ValueError:
            print(f"invalid literal for int() with base 10: {int}")
            return 0.0
