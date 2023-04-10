from DBTYPE_ENUM import DBTYPE


#magic method

#__call__
class class_call_method:
    def __call__(self, *args, **kwargs):
        print("class_call_method")
class_call_method()()
#判断是否可调用callable()
print(callable(class_call_method))

def decorator(func):
    def wrapper(*args, **kwargs):
        print("decorator")
        return func(*args, **kwargs)
    return wrapper

def decorator_fun(func):
    def func_wrapper(*args, **kwargs):
        print(f"*args:{args}")
        print("decorator_fun")
        return func(*args, **kwargs)
    return func_wrapper

@decorator
@decorator_fun
def func_DB(y):
    if DBTYPE.MYSQL.value == y:
        print("MYSQL")
        # 海象运算符
    if (x:=DBTYPE.ORACLE.value) == y:
        print(x)

func_DB(1)


class User(object):
    def __init__(self, username, password):

        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    def __enter__(self):
        print('before：auto do something before statements body of with executed')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('after：auto do something after statements body of with executed')
        # return True


if __name__ == '__main__':
    boy = User('faker', 'faker2021')
    print(boy.password)
    print("上下文管理器with语句：")
    with User('faker', 'faker2021') as user:
        print(user.password)
    print('---------end-----------')

if __name__ == '__main__':
    boy = User('faker', 'faker2021')
    print(boy.password)
    print("上下文管理器with语句：")
    with User('faker', 'faker2021') as user:
        print(user.password)
        12/0
        print('after execption')
    print('---------end-----------')