#thes is in function which use when we we have to run half function and save some runing code i n memory
# mostly use when hevy ML mpudel take time to load
def searcher():
    """function which search some text in given string"""
    import time
    time.sleep(3)#dekey of some time which is taken by some work or imporing any module
    book = "any large string"
    #code written up will take time only one time then if we run same function at same time the it will not take time again
    
    while True:
        """code which will run every time"""
        text = (yield)
        if text in book:
            print("in string")
        else:
            print("not in string")
    book.close()


search = searcher()#maked intance of search 
next(searcher())#to start function 
search.send("q")#to give command
search.send("q")
search.close()#to close the instance
#Note:- if you will give command to this function will show error becuse this function run with making it instance