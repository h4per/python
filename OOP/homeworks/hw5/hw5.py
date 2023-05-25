from decouple import config

money = config("MY_MONEY", default="Unknown")
# print(money)