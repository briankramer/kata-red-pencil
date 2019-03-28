def is_red_pencil(last, current):
    if not isinstance(last, tuple) or not isinstance(current, tuple):
        print('is_red_pencil needs two tuples.')
        return None
    if current[1] >= last[1]:
        return False
