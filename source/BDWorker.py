import os
import sqlite3


class BDWorker:
    @staticmethod
    def initialize():
        conn = None
        cursor = None
        if not os.path.exists('database.db'):
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE data
                              (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, current_mode TEXT DEFAULT "zalgo", zalgo_mode TEXT Default "average", messages_count INTEGER Default 0)
                           """)
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        return [conn, cursor]

    @staticmethod
    def add_user(user_id):
        data = BDWorker.initialize()
        conn, cursor = data[0], data[1]
        cursor.execute("""INSERT INTO data (user_id)
                          VALUES ({})""".format(user_id))
        conn.commit()

    @staticmethod
    def getter(user_id):
        data = BDWorker.initialize()
        conn, cursor = data[0], data[1]
        data = cursor.execute(
            """SELECT * FROM data WHERE user_id={}""".format(user_id)).fetchall()
        return {'user_id': data[0][1], 'current_mode': data[0][2], 'zalgo_type': data[0][3],
                'messages_count': data[0][4]}

    @staticmethod
    def messages_increment(user_id):
        data = BDWorker.initialize()
        conn, cursor = data[0], data[1]
        cursor.execute(
            """UPDATE data SET messages_count=messages_count+1 WHERE user_id="{}" """.format(user_id))
        conn.commit()

    @staticmethod
    def changer(user_id, obj):
        data = BDWorker.initialize()
        conn, cursor = data[0], data[1]
        cursor.execute(
            """UPDATE data SET {}="{}" WHERE user_id="{}" """.format(obj[0], obj[1], user_id))
        conn.commit()

    @staticmethod
    def user_exists(user_id):
        data = BDWorker.initialize()
        conn, cursor = data[0], data[1]
        if cursor.execute("""SELECT * FROM data WHERE user_id={}""".format(user_id)).fetchall():
            return True
        return False
