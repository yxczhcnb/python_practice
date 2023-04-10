from enum import Enum
from enum import IntEnum

#枚举
class DBTYPE(IntEnum):
    MYSQL = 0
    ORACLE = 1
    MSSQL = 2
    SQLITE = 3

if "__main__" == __name__:
    print(DBTYPE.MYSQL.name)
    print(DBTYPE.MYSQL.value)