def is_red_pencil(last, current, last_red_pencil=None):
    if not isinstance(last, tuple) or not isinstance(current, tuple):
        print('is_red_pencil needs two tuples.')
        return None
    percent_decrease = (last[1] - current[1]) / last[1]
    if percent_decrease < .05 or percent_decrease > .3:
        return False
    if (current[0] - last[0]).days < 30:
        return False
    if last_red_pencil and (current[0] - last_red_pencil).days < 30:
        return False
    return True
