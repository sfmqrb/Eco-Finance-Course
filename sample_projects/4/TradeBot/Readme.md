# Trade Bot

## Introduction:
This project elevates trading in the stock market by analysing data through code. by utilising the [pytse-client](https://github.com/Glyphack/pytse-client) package, we are able to get the current price of a stock, as well as its entire history.

# Files:
This project has 2 man files and 2 extra files:
> 1. Functions.py 
> 2. Trade-bot.py
> 3. _Developer.py
> 4. tests.py

The `Functions.py` file contains all the main logic for the code in a class called `Stock`.

The `Trade-bot.py` file is used to run the functions in the `Stock` class from the `Functions.py` file.

The `_Developer.py` file is used to test the functions that will be added to the `Stock` class.

The `tests.py` file is a simpler breakdown of what will be added to the `_Developer.py` file.

# Examples:

to initiate a stock, we can initialize it like so:
```py
from Functions import Stock
stock = Stock("stock name")
```

to sell a specific amount of a stock:
```py
stock.sell(amount)
```

to buy a specific amount of a stock: 
```py
stock.buy(amount)
```

# All functions:
- setHigh
- setLow
- downloadPrice
- getCurrentPrice
- getYesterdaysPrice
- getIndexInCSV
- getSignCSV
- getCurrentCandle
- isGreenCandle
- isRedCande
- getCurrentAmount
- sell
- buy
- getAverage

# Contact Info:

<a href="mailto:info@example.com?subject=subject&cc=cc@example.com">Hossein.Faniii@gmail.com</a>

<a href="https://github.com/Helli3-Hossein-Fani">Formal GitHub</a>

<a href="https://github.com/boat-bold647">Personal GitHub</a>
