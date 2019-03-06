#导入car.py中的对象并使用
from car import Car
bus1=Car('japan','paoche','2020')
print(bus1.getname())#可以正常使用car类

from car import battery
bike=battery(battery=91)
bike.readbat()