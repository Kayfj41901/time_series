import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")
import acquire
from acquire import get_store_item_demand_data


def prep_store_data(df): 
    #convert sale_date feature to datetime dtype
    df.sale_date = pd.to_datetime(df.sale_date)
    #set sale_date to index
    df = df.set_index('sale_date').sort_index()
    #rename sale_amount column
    df = df.rename(columns={'sale_amount': 'quantity'})
    #create a feature with only month from index
    df['month'] = df.index.month
    #create a feature with day name from day index 
    df['day_of_week'] = df.index.day_name()
    #create a feature sales total that is the product of quantity and sale price
    df['sales_total'] = df.quantity * df.item_price
    return df 

def prep_german_electric_data(df): 
    df.Date = pd.to_datetime(df.Date)
    df = df.set_index('Date').sort_index()
    df['month'] = df.index.month
    df['year'] = df.index.year
    return df