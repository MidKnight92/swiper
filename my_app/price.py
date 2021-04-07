
def get_current_price(data):
    price_str = data["price"][1:]
    price_float = float(price_str)
    return price_float

def assess_price(current, desired):
    if current <= desired:
        print("Todo")

def get_desired_price(str):
    return 'todo'