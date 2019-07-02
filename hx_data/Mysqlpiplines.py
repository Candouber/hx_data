# -*- coding:utf-8 -*-
import pymysql.cursors
class Mysqlpiplines(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'cdb1010110',
            port = 3306,
            db = 'hx_data'
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(
            'insert into hx(name, type, boss, money, address, adven)VALUE (%s,%s,%s,%s,%s,%s)',
            (item['name'], item['type'], item['boss'], item['money'], item['address'], item['adven'])
        )
        self.connect.commit()
        return item