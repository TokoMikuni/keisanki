from threading import Thread,Semaphore

def my_function1():
  for i in range(10000):
    with semaphore:
        print("123")
        print("456")
        print("789")

def my_function2():
  for i in range(10000):
    with semaphore:
        print("abc")
        print("def")
        print("ghi")

def my_function3():
  for i in range(10000):
    with semaphore:
        print("ABC")
        print("DEF")
        print("GHI")

from threading import Semaphore, Thread
if __name__=="__main__":
    semaphore=Semaphore(2)
    m=Thread(target=my_function1)
    n=Thread(target=my_function2)
    o=Thread(target=my_function3)
    m.start()
    n.start()
    o.start()
