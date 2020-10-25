while True:
    x,y,z= map(int,input("输入3个数").split(","))
    if x<y:
        if y<z:
            print(x,y,z)
        elif z<x:
            print(z,x,y)
        else:
            print(x,z,y)
    else :
        if x<z:
            print(y,x,z)
        if y<z :
            print(y,z,x)
        else:
            print(z,y,x)
