class User(object):
    def __init__(self, user_id: int, current_mode=None, messages_count=None, status=None, subtype=None,
                 token=None):
        self.id = None
        self.user_id = user_id
        self.current_mode = current_mode
        self.messages_count = messages_count
        self.status = status
        self.subtype = subtype
        self.token = token

    def __repr__(self):
        return f'<User {self.user_id}>'

    def __iter__(self):
        yield 'id', self.id
        yield 'user_id', self.user_id
        yield 'current_mode', self.current_mode
        yield 'messages_count', self.messages_count
        yield 'status', self.status
        yield 'subtype', self.subtype
        yield 'token', self.token
