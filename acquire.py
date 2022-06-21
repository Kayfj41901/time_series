import os 
import pandas as pd
import numpy as np 
import matplotlib as plt 
import seaborn as sns 
import requests


def get_stores_data_from_api():
    '''
    this function will return the dataset with stores 
    '''
    response = requests.get('https://api.data.codeup.com/api/v1/stores')
    data = response.json()
    stores = pd.DataFrame(data['payload']['stores'])
    stores = pd.DataFrame(stores)
    return data

def get_items_data_from_api():
    domain = 'https://api.data.codeup.com'
    #path or where we are accessing the data inside the url 
    endpoint = '/api/v1/items'
    #create an empty list to place the data within 
    items = []

    while endpoint is not None: 
        #assign url 
        url = domain + endpoint 
        #print(f'Acquiring page {endpoint}')
        #making a request and storing the response to the request as a string 
        response = requests.get(url)
        #taking the json data and converting to Pandas list of dictionaries (python)
        data = response.json()
        # .extends adds elements from a list to another list 
        items.extend(data['payload']['next_page'])
    items = pd.DataFrame(items)
    return items 

def get_sales_data_from_api(): 
    domain = 'https://api.data.codeup.com'
    #path or where we are accessing the data inside the url 
    endpoint = '/api/v1/sales'
    #create an empty list to place the data within 
    sales = []

    while endpoint is not None: 
        #assign url 
        url = domain + endpoint 
        #make a request and store the response to the request as a string 
        response = requests.get(url)
        # taking the json data and converting to Pandas list of dictionaries (python)
        data = response.json()
        # .extend adds elements from a list to another list 
        sales.extend(data['payload']['sales'])
        # reassigning the endpoint variable to have the path to the next page 
        endpoint = data['payload']['next_page']
    sales = pd.DataFrame(sales)
    return sales 


def get_store_data(): 
    filename = 'stores.csv'

    if os.path.exists(filename):
        print('Reading from csv file. . .')
        return pd.read_csv(filename)
    else: 
        df = get_stores_data_from_api()
        df.to_csv(filename)
    return df


def get_items_data():
    filename = 'items.csv'

    if os.path.exists(filename):
        print('Reading from csv file. . .')
        return pd.read_csv(filename)
    else: 
        df = get_items_data_from_api()
        df.to_csv(filename)
    return df

def get_sales_data():
    filename = 'sales.csv'

    if os.path.exists(filename):
        print('Reading from CSV file. . .')
        return pd.read_csv(filename)
    else: 
        df = get_sales_data_from_api()
        df.to_csv(filename)
    return df 

def get_store_item_demand_data():
    
    sales = get_sales_data()
    items = get_items_data()
    stores = get_stores_data()

    sales = sales.rename(columns={'item': 'item_id', 'store': 'store_id'})
    df = pd.merge(sales, items, how= 'left', on='item_id')
    df = pd.merge(df, stores, how='left', on='store_id')
    return df 
     
def german_electric(): 
    if os.path.exists('german_electric.csv'):
        print('Reading from .csv...')
        return pd.read_csv('german_electric.csv')
    df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
    df.to_csv('german_electric.csv', index=False)
    return df 
