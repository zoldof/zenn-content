#モジュール
import time
import tracemalloc
import random
import json
#from datetime import datetime
#from datetime import timedelta
#from dateutil import parser
#import pytz
#import pandas as pd
##import psutil, os, time

#データ作成
n = 1000
min_val = 0
max_val = 999
data = [random.randint(min_val, max_val) for _ in range(n)]
