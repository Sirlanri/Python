from enum import Enum

month=Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in month.__members__.items():#有BUG
    print(name, '=>', member, ',', member.value)