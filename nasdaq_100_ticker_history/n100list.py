from n100tickers import tickers_as_of
from datetime import datetime


if __name__ == "__main__":
    # for every year from 2016 to current,
    for year in range(2016, datetime.now().year):
        tickers = tickers_as_of(year, 12, 31)

        # write to a file
        tickers_list = sorted(tickers)
        with open(f"out/NASDAQ100_{year}-12-31.csv", "w") as f:
            for ticker in tickers_list:
                f.write(f"{ticker}\n")
        print(f"Year: {year}")
