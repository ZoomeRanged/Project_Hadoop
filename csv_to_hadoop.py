from email import header
import pandas as pd
from mrjob.job import MRJob
from sqlalchemy import false
data_property = pd.read_csv('dataset/dataset/TR_PropertyInfo.csv')
data_user = pd.read_csv('dataset/dataset/TR_UserInfo.csv')
print(data_user)