from numpy import average
import pytse_client as tse
import pandas
print ("چند سهام میخواهید؟")
e = int(input())
sum_percent = 0
majmoo = 0
for i in range (1,e+1):
    print("نام سهام",i,"شما چیست؟")
    name = str(input())
    print ("چند درصد از سهام میخواهید؟")
    percent = eval(input())
    df = pandas.read_csv("./tickers_data/"+name + ".csv")
    df ["return"]=df.close - df.close.shift(1)
    df ["return_perc"]=df["return"] / df.close.shift(1) * 100
    df. dropna(inplace=True)
    average = sum(df.return_perc)/ len(df.return_perc)
    sum_percent = sum_percent + percent
    std = df.return_perc.std()
    zarib = std * percent
    majmoo = majmoo + zarib
miangin_kol = majmoo / sum_percent 
print  ("ریسک شما   = ",miangin_kol)