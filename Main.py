import PolyGoogleTrends as trends

df = trends.get_historical_interest(['Table','Hi', 'Hello', 'Java', 'Ed Sheeran', 'Jupyter', 'Kardashian',
           'Trump', 'Mozilla', 'Llusx', 'Obama', 'Germany', 'Sweden', 'Mouse',
           'Wallet', 'Keys', 'Mug', 'Paper', 'Speakers', 'Moon'])



trends.plotDataFrame(df)