# @Time     : 2017/12/23 14:44
# @Author   : Johnny Mo
# @File     : MySQLConnector.py

import mysql.connector as connector
from model.Console import *

class MySQLConnector(object):

    def __init__(self):
         self.connection = connector.connect(host='120.79.39.221', port=3306, user='root', password='root', database='python_data')

    def selectOneData(self, sqlStr):
        """Select one data from Mysql database"""
        cursor = self.connection.cursor()
        cursor.execute(sqlStr)
        console = Console()
        if(cursor.rowcount == 1):
            result = cursor.fetchone()
            console.id = result[0]
            console.console = result[1]
            console.time = result[2]
            console.commit = result[3]
        return console

    def insertData(self, console):
        """Insert one data from Mysql database"""
        cursor = self.connection.cursor()
        sqlStr = """insert into console_data (console, time, commit) VALUES (%s, %s, %s)"""
        data = (console.console, console.time, console.commit)
        try:
            cursor.execute(sqlStr, data)
            self.connection.commit();
        except connector.Error as e:
            print('插入数据错误{}'.format(e))
        finally:
            cursor.close()

    def deleteData(self, consoleId):
        """Delete one data from Mysql database"""
        cursor  = self.connection.cursor()
        sqlStr = """DELETE FROM console_data WHERE id = %d"""
        try:
            cursor.execute(sqlStr, consoleId)
            self.connection.commit()
        except connector.Error as e:
            print('删除数据错误{}'.format(e))
        finally:
            cursor.close()

    def updateData(self, console):
        """Update one data from Mysql database"""
        cursor = self.connection.cursor()
        sqlStr = """UPDATE console_data SET console = %s, time = %s, commit = %s where id = %d"""
        data = (console.console, console.time, console.commit, console.id)
        try:
            cursor.execute(sqlStr, data)
            self.connection.commit()
        except connector.Error as e:
            print('更新数据错误{}'.format(e))
        finally:
            cursor.close()

    def closeConnection(self):
        """Close current Mysql Connection"""
        self.connection.close()




