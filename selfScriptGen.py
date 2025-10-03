import datetime as dt
name = input("What is your name?").split() #by using split 10 20 30 is taken as [10, 20, 30]
age = input("What is your age?").split()
city = input("What is your city?").split()
profession = input("What do you do?").split()
hobby = input("Tell us you favourite hobby!").split()
print(f"{name} is a very fascinating {age} years old individual who lives in the bustling city of {city} plying their trade as a {profession} with penchant for {hobby}.Logged on {dt.date.today().isoformat()}")