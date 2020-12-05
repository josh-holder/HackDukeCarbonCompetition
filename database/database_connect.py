#!/usr/bin/env python

import mysql.connector
from mysql.connector.constants import ClientFlag

config = {
    'user': 'root',
    'password': '2pMdJzGj9kGL31Gi',
    'host': '35.185.8.152',
    'database': 'user_data',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'ssl/server-ca.pem',
    'ssl_cert': 'ssl/client-cert.pem',
    'ssl_key': 'ssl/client-key.pem'
}

def reset_persistent_data():
    cursor.execute("DROP TABLE IF EXISTS PERSISTENT_DATA")
    cursor.execute("CREATE TABLE PERSISTENT_DATA("
        "USERNAME CHAR(20),"
        "PASSWORD CHAR(20),"
        "SCORE INT,"
        "CAR_MODEL CHAR(20),"
        "CAR_MPG INT,"
        "HOUSE_SIZE INT )")
    print("PERSISTENT_DATA initialized.")

def reset_daily_data():
    cursor.execute("DROP TABLE IF EXISTS DAILY_DATA")
    cursor.execute("CREATE TABLE DAILY_DATA("
        "USERNAME CHAR(20),"
        "TODAYS_DATE DATE,"
        "CARBON INT )")
    print("DAILY_DATA initialized.")


a = input("Type YES to destroy ALL DATA: ")
if a == "YES":

    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor()

    reset_persistent_data()
    reset_daily_data()

    cnxn.close()