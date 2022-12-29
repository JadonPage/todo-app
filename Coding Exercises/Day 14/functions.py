FREEZING_POINT = 0
BOILING_POINT = 100


def get_state(temp_arg):
    temp_arg = float(temp_arg)
    if temp_arg >= BOILING_POINT:
        return "Gas"
    elif temp_arg > FREEZING_POINT:
        return "Liquid"
    else:
        return "Solid"
