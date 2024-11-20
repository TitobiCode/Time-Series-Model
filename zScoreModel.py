import pandas as pd
import yfinance as yf

def calculate_Xyear_Country_Z_code(start_date, end_date):
    symbol = "^TNX" 
    data = yf.download(symbol, start_date, end_date)
    data.dropna(inplace=True)
    
    close_values = data.iloc[:, 1].values

    rollingWindow = 20

    rolling_mean = pd.Series(close_values).rolling(rollingWindow).mean()
    rolling_std = pd.Series(close_values).rolling(rollingWindow).std()

    z_score = (close_values - rolling_mean) / rolling_std

    output = pd.DataFrame({
        'Yield': close_values,
        'Rolling_Mean': rolling_mean,
        'Rolling_Standard_Deviation': rolling_std,
        'Z_Score': z_score
    })

    return output

result = calculate_Xyear_Country_Z_code('2000-12-25', '2023-12-25')
print(result)