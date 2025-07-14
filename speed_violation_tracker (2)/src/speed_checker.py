SPEED_LIMIT = 80  # km/h
FINE_AMOUNT = 50  # Amount to deduct

def is_speeding(speed):
    return speed > SPEED_LIMIT

def get_fine():
    return FINE_AMOUNT
