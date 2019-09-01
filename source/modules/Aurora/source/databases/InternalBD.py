import os
import sqlite3

from source.modules.Aurora.source.vk_api.UserAPI import UserAPI


class InternalBD:
    @staticmethod
    def initialize():
        conn = None
        cursor = None
        if not os.path.exists('./aurora.db'):
            conn = sqlite3.connect("./aurora.db")
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE userdata
                              (id INTEGER PRIMARY KEY AUTOINCREMENT,
                               user_id INTEGER,
                               friends TEXT DEFAULT NULL,
                               token TEXT DEFAULT NULL)
                           """)
        conn = sqlite3.connect("./aurora.db")
        cursor = conn.cursor()
        return [conn, cursor]

    @staticmethod
    def add_user(user_id, token):
        if InternalBD.user_exists(user_id):
            return
        data = InternalBD.initialize()
        conn, cursor = data[0], data[1]
        vk = UserAPI(token)

        cursor.execute("""INSERT INTO userdata (user_id, friends, token)
                          VALUES ({user_id},"{friends}", "{token}")""".format(user_id=user_id, token=token,
                                                                              friends=",".join(
                                                                                  "{0}".format(n) for n in
                                                                                  vk.get_friends()['items'])))
        conn.commit()

    @staticmethod
    def update_friends(user_id, friends):
        data = InternalBD.initialize()
        conn, cursor = data[0], data[1]
        cursor.execute('UPDATE userdata SET friends="{friends}" WHERE user_id={user_id}'.format(
            friends=",".join("{}".format(n) for n in friends), user_id=user_id))
        conn.commit()

    @staticmethod
    def getter(user_id):
        data = InternalBD.initialize()
        conn, cursor = data[0], data[1]
        data = cursor.execute(
            """SELECT * FROM userdata WHERE user_id={}""".format(user_id)).fetchall()
        data = list(data[0])
        return {'user_id': data[1], 'friends': [int(i) for i in data[2].split(',')],
                'token': data[3]}

    @staticmethod
    def delete_user(user_id):
        data = InternalBD.initialize()
        conn, cursor = data[0], data[1]
        cursor.execute(f'DELETE FROM userdata WHERE user_id={user_id}')
        conn.commit()

    @staticmethod
    def get_token(user_id):
        token = InternalBD.getter(user_id)['token']
        if not token:
            return False
        return token

    @staticmethod
    def user_exists(user_id):
        data = InternalBD.initialize()
        conn, cursor = data[0], data[1]
        if cursor.execute("""SELECT * FROM userdata WHERE user_id={}""".format(user_id)).fetchall():
            return True
        return False

    @staticmethod
    def get_users():
        data = InternalBD.initialize()
        conn, cursor = data[0], data[1]
        return cursor.execute("""SELECT user_id FROM userdata""").fetchall()[0]
