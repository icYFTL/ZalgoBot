import sqlite3


class InternalBD:
    @staticmethod
    def initialize():
        conn = sqlite3.connect("./zalgo.db")
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS data 
                              (id INTEGER PRIMARY KEY AUTOINCREMENT,
                               user_id INTEGER,
                                current_mode TEXT DEFAULT "zalgo",
                                 messages_count INTEGER Default 0,
                                  status TEXT Default "None",
                                  subtype TEXT Default "Базовая",
                                   token TEXT DEFAULT NULL)
                           """)
        conn.commit()
        return [conn, cursor]

    @staticmethod
    def add_user(user_id):
        if InternalBD.user_exists(user_id):
            return
        data = InternalBD.initialize()
        conn, cursor = data[0], data[1]
        cursor.execute(f'INSERT INTO data (user_id) VALUES ({user_id})')
        conn.commit()

    @staticmethod
    def getter(user_id):
        data = InternalBD.initialize()
        conn, cursor = data[0], data[1]
        data = cursor.execute(f'SELECT * FROM data WHERE user_id={user_id}').fetchall()
        data = list(data[0])
        return {'user_id': data[1], 'current_mode': data[2],
                'messages_count': data[3], 'status': data[4], 'subtype': data[5], 'token': data[6]}

    @staticmethod
    def get_token(user_id):
        token = InternalBD.getter(user_id)['token']
        return False if not token else token

    # @staticmethod
    # def messages_increment(user_id):
    #     data = InternalBD.initialize()
    #     conn, cursor = data[0], data[1]
    #     cursor.execute(f'UPDATE data SET messages_count=messages_count+1 WHERE user_id={user_id}')
    #     conn.commit()

    @staticmethod
    def status_changer(user_id, obj):
        data = InternalBD.initialize()
        conn, cursor = data[0], data[1]
        cursor.execute(f'UPDATE data SET status="{obj}" WHERE user_id={user_id}')
        conn.commit()

    @staticmethod
    def mode_changer(user_id, obj):
        data = InternalBD.initialize()
        conn, cursor = data[0], data[1]
        cursor.execute(f'UPDATE data SET current_mode="{obj}" WHERE user_id={user_id}')
        conn.commit()

    @staticmethod
    def status_cleaner_emergency():
        data = InternalBD.initialize()
        conn, cursor = data[0], data[1]
        cursor.execute(f'UPDATE data SET status="None" WHERE status != "None"')
        conn.commit()

    @staticmethod
    def update_token(user_id, token):
        data = InternalBD.initialize()
        conn, cursor = data[0], data[1]
        cursor.execute(f'UPDATE data SET token="{token}" WHERE user_id={user_id}')
        conn.commit()

    @staticmethod
    def user_exists(user_id):
        data = InternalBD.initialize()
        conn, cursor = data[0], data[1]
        return True if cursor.execute(f'SELECT * FROM data WHERE user_id={user_id}').fetchall() else False
