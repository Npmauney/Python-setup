print("Hello from inside a file!")

def hello():
    print("Hello there!")

def pack(x,y,z):
    return [x,y,z]

def eat_lunch(list):
    if len(list)==0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"First I eat {list[0]}")
            else:
                print(f"Next I eat {list[i]}")

hello()
print(pack("x", "y", "z"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["orange", "carrots", "salad", "pudding"])