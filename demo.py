import os,sys


def myFunction( a,b ):
    x=1+  2
    if(a> b):
        print( "A is greater" )
    else:
     print("B is greater")
    unused_var = 123
    return  x


class myclass:
    def __init__(self,name):
        self.Name=name

    def SayHello(self):
        print("hello "+self.Name)


def divide(a,b):
    try:
        result=a/b
    except:
        print("error")
    return result


for i in range(0,10):
    print(i)
