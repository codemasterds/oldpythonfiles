import sys
sys.setrecursionlimit(2000)

i=0
def sai():
    global i
    i=i+1
    print("hello",i)
    sai()
sai()
