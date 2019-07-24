import os
import sqlite3


class InternalBD:
    @staticmethod
    def initialize():
        conn = None
        cursor = None
        if not os.path.exists('./database.db'):
            conn = sqlite3.connect("./database.db")
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE data
                              (id INTEGER PRIMARY KEY AUTOINCREMENT,
                               user_id INTEGER,
                                current_mode TEXT DEFAULT "zalgo",
                                 messages_count INTEGER Default 0,
                                  status TEXT Default "None",
                                  subtype TEXT Default "Базовая",
                                   token TEXT DEFAULT NULL)
                           """)
        conn = sqlite3.connect("./database.db")
        cursor = conn.cursor()
        return [conn, cursor]

    @staticmethod
    def add_user(user_id):
        if InternalBD.user_exists(user_id):
            return
        data = InternalBD.initialize()
        conn, cursor = data[0], data[1]
        cursor.execute("""INSERT INTO data (user_id)
                          VALUES ({})""".format(user_id))
        conn.commit()

    @staticmethod
    def getter(user_id):
        data = InternalBD.initialize()
        conn, cursor = data[0], data[1]
        data = cursor.execute(
            """SELECT * FROM data WHERE user_id={}""".format(user_id)).fetchall()
        data = list(data[0])
        return {'user_id': data[1], 'current_mode': data[2],
                'messages_count': data[3], 'status': data[4], 'subtype': data[5], 'token': data[6]}

    @staticmethod
    def get_token(user_id):
        token = InternalBD.getter(user_id)['token']
        if not token:
            return False
        return token

    @staticmethod
    def messages_increment(user_id):
        data = InternalBD.initialize()
        conn, cursor = data[0], data[1]
        cursor.execute(
            """UPDATE data SET messages_count=messages_count+1 WHERE user_id={} """.format(user_id))
        conn.commit()

    @staticmethod
    def changer(user_id, obj):
        data = InternalBD.initialize()
        conn, cursor = data[0], data[1]
        cursor.execute(
            """UPDATE data SET {}="{}" WHERE user_id={}""".format(obj[0], obj[1], user_id))
        conn.commit()

    @staticmethod
    def status_cleaner_emergency():
        data = InternalBD.initialize()
        conn, cursor = data[0], data[1]
        cursor.execute(
            """UPDATE data SET status="None" WHERE status != "None" """)
        conn.commit()

    @staticmethod
    def add_token(user_id, token):
        data = InternalBD.initialize()
        conn, cursor = data[0], data[1]
        cursor.execute(
            """UPDATE data SET token="{token}" WHERE user_id={user_id}""".format(token=token, user_id=user_id))
        conn.commit()

    @staticmethod
    def user_exists(user_id):
        data = InternalBD.initialize()
        conn, cursor = data[0], data[1]
        if cursor.execute("""SELECT * FROM data WHERE user_id={}""".format(user_id)).fetchall():
            return True
        return False
