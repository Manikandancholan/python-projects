list = ['car', 'bike', 'bus']

def loop(x):
    print(x*3)
    
def map_func(s, list):
    print("s", list)
    for i in list:
        s(i)
    
map_func(loop, list)