import pandas as pd

def customers_who_never_order(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # return customers[~customers.id.isin(orders.customerId)].drop(columns=['id']).rename(columns = { 'name':'Customers' }).reset_index(drop=True)
    df = customers[~customers.id.isin(orders.customerId)]
    
    df = df[['name']].rename(columns = { 'name':'Customers' })
    return df.reset_index(drop=True)