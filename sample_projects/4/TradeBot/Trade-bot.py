from pyclbr import Function
import pytse_client as tse
from Functions import Stock, Sheet
import _Developer

ASP = Stock("ASP", "آ س پ")
ASP.setHight(7720)
ASP.setLow(2813)

VABEMELAT = Stock("VABMELAT", "وبملت")
VABEMELAT.setHight(4646)
VABEMELAT.setLow(2201)

KHAGOSTAR = Stock("KHAGOSTAR", "خگستر")
KHAGOSTAR.setHight(2918)
KHAGOSTAR.setLow(2040)

PAKHSH = Stock("PASKSH", "پخش")
PAKHSH.setHight(32148)
PAKHSH.setLow(17326)

DARAYEKOM = Stock("ASP", "دارا یکم")
DARAYEKOM.setHight(129758)
DARAYEKOM.setLow(99759)

Stocks = [ASP, VABEMELAT, KHAGOSTAR, PAKHSH, DARAYEKOM]

for stock in Stocks:
    if stock.getCurrentPrice() >= stock.high or stock.getCurrentPrice() < stock.low:
        stock.sell(stock.amount)
    low, high = stock.getAverage()
    if stock.getCurrentPrice() > ( high - 0.1 * high ) and stock.getCurrentPrice() < ( high + 0.1 * high ):
        stock.sell(stock.getCurrentAmount())
    if stock.getCurrentPrice() > ( low - 0.1 * low ) and stock.getCurrentPrice() < ( low + 0.1 * low ):
        stock.sell(stock.getCurrentAmount())
     