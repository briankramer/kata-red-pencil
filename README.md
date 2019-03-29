# kata-red-pencil

Kata Requirements: https://stefanroock.wordpress.com/2011/03/04/red-pencil-code-kata/

This project uses Python 3 with no extra libraries.

# Run tests:
  python3 -m unittest discover

# Run red_pencil function:
  Go into python shell
  > python3

  Type
  > from datetime import datetime as dt
  > from red_pencil import red_pencil

  Use red_pencil to calculate when red pencil promotions start and stop

  Example:
  > red_pencil[(dt(1, 1, 1), 10.00), (dt(2, 1, 1), 5.00)]

  The input is a list of tuples where the first part of the tuple is a datetime and the second part is a price.

  The output will be a tuple of two lists. The first list is a tuple of a datetime and price for when the red pencils started. The second list is a list of dates when the red pencils ended.

# Implementation details:
  Assumed that we will never get the same price twice in a row.
  "Stable for 30 days" is defined as the price has not changed in 30 days.
  "Original price" is defined as the first price given in the input.
  There is only one price change per day.
  
  Enjoy!
