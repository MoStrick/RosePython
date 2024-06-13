

#import requests
import pandas
#import pandas
import urllib.request


lottery_url = "https://data.ny.gov/Government-Finance/Lottery-Powerball-Winning-Numbers-Beginning-2010/d6yy-54nr/data_preview"
urllib.request.urlretrieve(lottery_url, "lottery.csv")




df_lottery = pandas.read_csv("lottery.csv")

