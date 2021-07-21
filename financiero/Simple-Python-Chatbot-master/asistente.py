from neuralintets import GenericAssistant
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
    