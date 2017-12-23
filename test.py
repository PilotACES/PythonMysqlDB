# @Time     : 2017/12/23 16:07
# @Author   : Johnny Mo
# @File     : test.py

from model.Console import *
from dao.MySQLConnector import *

xbox = Console()
xbox.time = "2017-11-07"
xbox.console = "xbox one X"
xbox.commit = "Good"
connector = MySQLConnector()
connector.insertData(xbox)
connector.closeConnection()
