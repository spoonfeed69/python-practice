# -*- coding: utf-8 -*-
from datetime import datetime

name=input("Your name: " )

age=input("Your age: ")

time=100 - int(age)

year=datetime.now().year + time

print("In year " + str(year) + " your will become 100")

num=int(input("give me another number: "))

print("returned result is: " + str(num)*10)

print((str(num)+"\n")*10)