import yfinance as yf
import pandas as pd
import numpy as np

# Function to calculate percentage change over the last three months
def calculate_percentage_change(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    
    # Get historical data for the last 3 months
    df = stock.history(period="3mo")
    
    # Calculate the percentage change
    if len(df) > 0:
        start_price = df['Close'].iloc[0]
        end_price = df['Close'].iloc[-1]
        percentage_change = ((end_price - start_price) / start_price) * 100
    else:
        percentage_change = np.nan  # In case there is no data
    
    return percentage_change

# List of 200 stock symbols
stock_symbols = ['AARTIIND.NS', 'ABB.NS', 'ABBOTINDIA.NS', 'ABCAPITAL.NS', 'ABFRL.NS', 'ACC.NS', 'ADANIENT.NS', 'ADANIPORTS.NS',
                 'AMBUJACEM.NS', 'APOLLOHOSP.NS', 'APOLLOTYRE.NS', 'ASHOKLEY.NS', 'ASTRAL.NS', 'ATUL.NS', 'AUBANK.NS', 'AUROPHARMA.NS',
                 'BAJAJFINSV.NS', 'BAJFINANCE.NS', 'BALKRISIND.NS', 'BALRAMCHIN.NS', 'BANDHANBNK.NS', 'BANKBARODA.NS', '^NSEBANK', 
                 'BEL.NS', 'BHARATFORG.NS', 'BHARTIARTL.NS', 'BHEL.NS', 'BIOCON.NS', 'BOSCHLTD.NS', 'BPCL.NS', 'BRITANNIA.NS', 'BSOFT.NS',
                 'CANBK.NS', 'CHAMBLFERT.NS', 'CHOLAFIN.NS', 'CIPLA.NS', 'COALINDIA.NS', 'COFORGE.NS', 'CONCOR.NS', 'COROMANDEL.NS', 'CROMPTON.NS',
                 'CUB.NS', 'DABUR.NS', 'DALBHARAT.NS', 'DEEPAKNTR.NS', 'DLF.NS', 'EICHERMOT.NS', 'ESCORTS.NS', 'GAIL.NS', 'GLENMARK.NS',
                 'GMRINFRA.NS', 'GNFC.NS', 'GODREJCP.NS', 'GODREJPROP.NS', 'GRASIM.NS', 'GUJGASLTD.NS', 'HAL.NS', 'HDFCBANK.NS', 'HDFCLIFE.NS',
                 'HEROMOTOCO.NS', 'HINDPETRO.NS', 'HINDUNILVR.NS', 'ICICIBANK.NS', 'ICICIGI.NS', 'ICICIPRULI.NS', 'IDEA.NS', 'IDFC.NS',
                 'IDFCFIRSTB.NS', 'IEX.NS', 'INDHOTEL.NS', 'INDIACEM.NS', 'INDIAMART.NS', 'INDIGO.NS', 'INDUSINDBK.NS', 'INDUSTOWER.NS',
                 'IOC.NS', 'IPCALAB.NS', 'IRCTC.NS', 'ITC.NS', 'JINDALSTEL.NS', 'JKCEMENT.NS', 'JSWSTEEL.NS', 'JUBLFOOD.NS', 
                 'KOTAKBANK.NS', 'LICHSGFIN.NS', 'LT.NS', 'LTF.NS', 'LTTS.NS', 'M&MFIN.NS', 'MANAPPURAM.NS', 'MARICO.NS',
                 'MARUTI.NS', 'MCX.NS', 'METROPOLIS.NS', 'MFSL.NS', 'MGL.NS', 'MOTHERSON.NS', 'MPHASIS.NS', 'NATIONALUM.NS',
                 'NAVINFLUOR.NS', 'NESTLEIND.NS', '^NSEI', 'NMDC.NS', 'NTPC.NS', 'OBEROIRLTY.NS', 'ONGC.NS', 'PEL.NS', 
                 'PETRONET.NS', 'PFC.NS', 'PIDILITIND.NS', 'PIIND.NS', 'PNB.NS', 'POLYCAB.NS', 'POWERGRID.NS', 'PVRINOX.NS',
                 'RAMCOCEM.NS', 'RBLBANK.NS', 'RECLTD.NS', 'RELIANCE.NS', 'SAIL.NS', 'SBICARD.NS', 'SBILIFE.NS', 'SBIN.NS',
                 'SHRIRAMFIN.NS', 'SRF.NS', 'SUNTV.NS', 'TATACHEM.NS', 'TATACOMM.NS', 'TATACONSUM.NS', 'TATAMOTORS.NS',
                 'TATAPOWER.NS', 'TATASTEEL.NS','TCS.NS', 'TORNTPHARM.NS', 'UBL.NS', 'ULTRACEMCO.NS','UPL.NS', 'VEDL.NS', 'VOLTAS.NS', 'ZYDUSLIFE.NS'
                ]

# Dictionary to store the percentage change for each stock
stock_performance = {}

# Calculate percentage change for each stock
for symbol in stock_symbols:
    stock_performance[symbol] = calculate_percentage_change(symbol)

# Convert the dictionary to a pandas DataFrame for better readability
df_performance = pd.DataFrame(list(stock_performance.items()), columns=['Stock Symbol', '3-Month % Change'])

# Display the DataFrame
print(df_performance)

# Save to a CSV file
df_performance.to_csv('stock_performance_3months.csv', index=False)
