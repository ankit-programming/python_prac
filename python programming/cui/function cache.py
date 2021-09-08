import time
from functools import lru_cache

#cache how many time you want to sotre
@lru_cache(maxsize=5)

def some_work(n):
    time.sleep(n)
    return n 

if __name__ == "__main__":
    print("now runing some_work")
    some_work(3)
    print("started deleyaing for next 3 sec")
    some_work(3)
    print("deleying for 2 sec")
    some_work(2)
    print("deleying for next 2 sec")
    some_work(2)
    print("deleying for 1 sec")
    some_work(1)

#Note:- if 3sec complet once then if use ohter 3sec then it will not take 3sec
