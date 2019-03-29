from datetime import timedelta

def is_red_pencil(last, current, last_red_pencil=None):
    '''Determines if a new red pencil is starting.'''
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

def should_red_pencil_end(last_red_pencil, current, original_price):
    '''Determines if red pencil should end prematurely.'''
    if current[1] > last_red_pencil[1]:
        return True
    if (original_price - current[1]) / original_price < -.3:
        return True
    return False

def red_pencil(time_price_list):
    if not time_price_list or not isinstance(time_price_list, list):
        print('red_pencil takes an array of tuples with datetime and price')
        return None
    last_row = time_price_list[0]
    original_price = last_row[1]
    red_pencil_active = False
    red_pencils = []
    red_pencil_end_dates = []

    for row in time_price_list[1:]:
        if (row[0] - last_row[0]).days > 30:
            # end a red pencil sale at 30 days after start
            if red_pencils and red_pencil_active:
                red_pencil_end_dates.append(red_pencils[-1][0] + timedelta(days=30))
            red_pencil_active = False
        if red_pencil_active:
            red_pencil_active = not should_red_pencil_end(last_row, row, original_price)
            if not red_pencil_active:
                red_pencil_end_dates.append((row[0]))
        else:
            last_red_pencil_time = None
            if red_pencils:
                last_red_pencil_time = red_pencils[-1][0]
            red_pencil_active = is_red_pencil(last_row, row, last_red_pencil_time)
            if red_pencil_active:
                red_pencils.append(row)
        last_row = row
    if red_pencils and len(red_pencils) > len(red_pencil_end_dates):
        red_pencil_end_dates.append(red_pencils[-1][0] + timedelta(days=30))
    return (red_pencils, red_pencil_end_dates)
