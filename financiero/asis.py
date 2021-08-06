from neuralintents import GenericAssistant
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web 
import mplfinance as mpf

import pickle
import sys 
import datetime as dt

def myfunction():
    pass

mappings = {
     'greetings': myfunction
}
   
assistant = GenericAssistant('intents.json', intent_methods=mappings)

assistant.train_model()

assistant.request("Hello")



portfolio = {'AAPL': 20, 'TSLA': 5, "GS": 10}

with open('portfolio.pkl', 'wb') as f:
    pickle.dumb ( portfolio, f)
    
print(portfolio) 

def save_portfolio():
    with open('portfolio.pkl', 'wb') as f:
        pickle.dump (portfolio, f)

def add_portfolio():
    ticker = input ("which stock do toy want to add: ")
    amount = input ("how many shares do toy want to add: ")
    
    if ticker in portfolio.keys():
        portfolio[ticker] += int(amount)
    else:
        portfolio[ticker] = int(amount)
        
    save_portfolio()        
    
def remove_portfolio():
    ticker = input ("which stock do toy want to sell: ")
    amount = input ("how many shares do toy want to sell: ")
    
    if ticker in portfolio.keys():
        if amount <= portfolio[ticker]:
            portfolio[ticker] -= int(amount)
            save_portfolio()
        else:
            print ("you don't have enough shares")
    else :
        print (f"you don't own any shares of {ticker}")


def show_portfolio():
    print ("your portfolio:")
    for ticker in portfolio.keys():
        print (f"you own {portfolio[ticker]} shares of {ticker}")


def portfolio_worth():
    sum = 0
    for ticker in portfolio.keys():
        data = web.DataReader(ticker,'yahoo')
        price = data ['Close'].iloc[-1]
        sum +=price
    print(f"your portfolio is worth {sum} USD")


def portfolio_gains():
    starting_date = input("enter a date for comparison (yyyy-mm-dd):")
    
    sum_now = 0
    sum_then = 0
    
    try:
        for ticker in portfolio.keys():
            data= web.DataReader(ticker,'yahoo')
            price_now = data['close'].iloc[-1]
            price_then = data.loc[data.index == starting_date]['close'].values[0]
            sum_now += price_now
            sum_then += price_then
            
        print(f"relative gains: {((sum_now-sum_then)/sum_then)*100}%")
        print(f"absolute gains: {sum_now-sum_then}USD")
    except IndexError:
        print("there was no trading on this day!")

def bye ():
    print ("goodbye")
    sys.exit(0)


mappings= {
    'plot_chart': plot_chart,
    'add_portfolio': add_portfolio,
    'remove_portfolio': remove_portfolio,
    'show_portfolio': show_portfolio,
    'portfolio_worth': portfolio_worth,
    'portfolio_gains': portfolio_gains,
    'bye': bye
    
}


assistant = GenericAssistant('intents.json',mappings,"financial_assistant_model")

assistant.load_model()

while True:
    message = input ("")
    assistant.request(message)