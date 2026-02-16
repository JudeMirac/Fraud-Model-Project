from sklearn.preprocessing import FunctionTransformer

def add_interactions(df):
    """
    Add interaction features to capture combined risk signals.
    
    Creates engineered features by combining existing features to better
    capture fraud risk patterns.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Input dataframe with fraud risk features
        
    Returns:
    --------
    pandas.DataFrame
        DataFrame with added interaction features
    """
    df = df.copy()
    df['tenure_x_chargebacks'] = (df['account_tenure_months'] * df['previous_chargebacks'])
    df['tenure_per_transaction'] = (df['account_tenure_months'] / (df['num_transactions_24h'] + 1))
    df['chargeback_x_region'] = (df['previous_chargebacks'] * df['region'])
    df['chargeback_x_device'] = (df['previous_chargebacks'] * df['device_type'])
    df['chargebacks_x_age'] = (df['previous_chargebacks'] * df['customer_age'])
    df['chargebacks_x_international'] = (df['previous_chargebacks'] * df['international'])
    df['youth_risk'] = ((df['customer_age'] < 30) & (df['num_transactions_24h'] >= 5)).astype(int)
    df['high_foreign_amount'] = ((df['transaction_amount'] > 350) & (df['international'] == 1)).astype(int)
    return df

fe_prep = FunctionTransformer(add_interactions, validate=False)