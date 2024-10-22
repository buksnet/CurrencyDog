import datetime as dt
import pandas as pd

today = dt.datetime.now()
then = today - dt.timedelta(days=30)
pd.set_option('display.max_columns', None)
