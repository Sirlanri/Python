class User():
    def __init__(self, name, email):
        self.name=name
        self.email=email
class Anony(User):
    def __init__(self):
        self.name=None
        self.email=None
    def __nonzero__(self):
        return 0

import functools
def requires(func):
    @functools.wraps
    def inner(user,*args,**kwargs):
        if uesr and isinstance(user,User):
            return func(user,*args,**kwargs)
        else:
            raise ValueError('需要有效的用户')
    return inner