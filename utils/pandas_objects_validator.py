# importing module
import pandas as pd

# a function to prepare dataframe from a given response
def dataframe_validator(response: dict) -> pd.DataFrame:
    df = pd.DataFrame.from_dict(response, orient="index")
    df.columns = [col.title() for col in df.columns]
    df["Date"] = pd.to_datetime(df["Date"])
    df.rename(columns={"Amount": "Amount (in ₹)"}, inplace=True)
    df.index.name = "ID"
    
    return df

# a function to prepare series from a given response
def series_validator(response: dict) -> pd.DataFrame:
    series = pd.Series(response, name=id)
    series.index = [index.title() for index in series.index]
    series["Date"] = pd.to_datetime(series["Date"])
    series.rename(index={"Amount": "Amount (in ₹)"}, inplace=True)
    series.index.name = "ID"
    
    return series